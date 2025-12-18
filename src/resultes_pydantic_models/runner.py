import abc as _abc
import collections.abc as _cabc
import pathlib as _pl
import typing as _tp

import pydantic as _pyd
import resultes_pydantic_models.common as _pcom


class RunnerOptions(_pyd.BaseModel):
    log_level: str
    shall_remove_completed_jobs: bool


class ObjectStorageFilePathBase(_pyd.BaseModel, _abc.ABC):
    container: str
    path: str


class ObjectStorageInputFilePath(ObjectStorageFilePathBase):
    version: str | None = None


class ObjectStorageInputZipFilePath(ObjectStorageInputFilePath):
    @_pyd.field_validator("path", mode="after")
    @classmethod
    def _validate_path(cls, value: str) -> str:
        if not value.endswith(".zip"):
            raise ValueError("Path must point to .zip file.", value)

        return value


class ObjectStorageOutputFilePath(ObjectStorageFilePathBase):
    pass


class ObjectStorageOutputZipFilePath(ObjectStorageOutputFilePath):
    @_pyd.field_validator("path", mode="after")
    @classmethod
    def _validate_path(cls, value: str) -> str:
        if not value.endswith(".zip"):
            raise ValueError("Path must point to .zip file.", value)

        return value


class SingleFileResult(_pyd.BaseModel):
    discriminator: _tp.Literal["single"] = "single"
    file_path: _pcom.PureWindowsPath
    object_storage_output_file_path: ObjectStorageOutputFilePath

    @_pyd.field_validator("file_path", mode="after")
    @classmethod
    def _validate_file_path(cls, value: _pcom.PureWindowsPath) -> _pcom.PureWindowsPath:
        if value.is_absolute():
            raise ValueError("File path must not be absolute.", value)

        return value


class GlobPatterns(_pyd.BaseModel):
    include: _cabc.Sequence[str]
    exclude: _cabc.Sequence[str] | None = None


class MultipleFilesResult(_pyd.BaseModel):
    discriminator: _tp.Literal["multiple"] = "multiple"
    glob_patterns: GlobPatterns
    object_storage_output_file_path: ObjectStorageOutputZipFilePath


type Result = SingleFileResult | MultipleFilesResult


class GeneralCommand(_pyd.BaseModel):
    discriminator: _tp.Literal["general-command"] = "general-command"

    program: _pcom.PureWindowsPath
    args: _cabc.Sequence[str]
    working_dir: _pcom.PureWindowsPath | None = None
    relative_log_file_path: _pcom.PureWindowsPath | None = None


class RunTrnsysCommand(_pyd.BaseModel):
    discriminator: _tp.Literal["run-trnsys-command"] = "run-trnsys-command"
    trnsys_exe_path: _pcom.PureWindowsPath
    relative_deck_file_path: _pcom.PureWindowsPath
    relative_temperatures_step_prt_file_path: _pcom.PureWindowsPath
    n_total_timesteps: int

    @_pyd.field_validator("n_total_timesteps")
    @classmethod
    def _validate_n_total_timesteps(cls, value: int) -> int:
        if value <= 0:
            raise ValueError("Total number of timesteps must be positive.", value)

        return value

    @_pyd.field_validator("trnsys_exe_path")
    @classmethod
    def _validate_trnsys_exe_path(
        cls, value: _pcom.PureWindowsPath
    ) -> _pcom.PureWindowsPath:
        if value.name != "TrnEXE.exe":
            raise ValueError("TRNSYS executable path must end in TrnEXE.exe", value)

        return value


type Command = GeneralCommand | RunTrnsysCommand


class RunnerJob(_pyd.BaseModel):
    id: str
    parameters: _pyd.JsonValue | None = None
    object_storage_input_path: ObjectStorageInputZipFilePath
    commands: _cabc.Sequence[
        _tp.Annotated[Command, _pyd.Field(discriminator="discriminator")]
    ]
    results: _cabc.Sequence[
        _tp.Annotated[Result, _pyd.Field(discriminator="discriminator")]
    ]
    return_paths_glob_pattern: str | None = None


class JobProgress(_pyd.BaseModel):
    type: _tp.Literal["progress"] = "progress"
    progress: int
    command_number: int | None = None

    @_pyd.field_validator("progress", mode="after")
    @classmethod
    def _validate_progress(cls, value: int) -> int:
        if not 0 <= value <= 100:
            raise ValueError("Progress must between 0 and 100, inclusive.")

        return value


class JobSuccess(_pyd.BaseModel):
    type: _tp.Literal["success"] = "success"
    result: _pyd.JsonValue | None = None


class JobError(_pyd.BaseModel):
    type: _tp.Literal["error"] = "error"
    message: str
    command_number: int | None = None


class LogMessage(_pyd.BaseModel):
    type: _tp.Literal["log-message"] = "log-message"
    level: int
    message: str
    command_number: int | None = None


type JobSuccessfulPayload = LogMessage | JobProgress | JobSuccess


class JobNotification(_pyd.BaseModel):
    job_id: str
    payload: JobSuccessfulPayload | JobError = _pyd.Field(discriminator="type")

    @staticmethod
    def from_error(job_id: str, error_message: str) -> "JobNotification":
        payload = JobError(message=error_message)
        notification = JobNotification(job_id=job_id, payload=payload)
        return notification
