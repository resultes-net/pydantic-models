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
    def _validate_file_path(cls, value: _pl.PureWindowsPath) -> _pl.PureWindowsPath:
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


class Command(_pyd.BaseModel):
    program: _pcom.PureWindowsPath
    args: _cabc.Sequence[str]
    working_dir: _pcom.PureWindowsPath | None = None
    relative_log_file_path: _pcom.PureWindowsPath | None = None


class RunnerJob(_pyd.BaseModel):
    id: str
    parameters: _pyd.JsonValue | None = None
    object_storage_input_path: ObjectStorageInputZipFilePath
    commands: _cabc.Sequence[Command]
    results: _cabc.Sequence[
        _tp.Annotated[Result, _pyd.Field(discriminator="discriminator")]
    ]
    return_paths_glob_pattern: str | None = None


class JobProgress(_pyd.BaseModel):
    progress: int

    @_pyd.field_validator("progress", mode="after")
    @classmethod
    def _validate_progress(cls, value: int) -> int:
        if not 0 <= value <= 100:
            raise ValueError("Progress must between 0 and 100, inclusive.")

        return value


class JobSuccess(_pyd.BaseModel):
    result: _tp.Any


class JobError(_pyd.BaseModel):
    message: str


class LogMessage(_pyd.BaseModel):
    level: int
    message: str


type JobSuccessfulPayload = LogMessage | JobProgress | JobSuccess


class JobNotification(_pyd.BaseModel):
    job_id: str
    payload: JobSuccessfulPayload | JobError
