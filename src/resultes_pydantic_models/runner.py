import collections.abc as _cabc

import resultes_pydantic_models.common as _pcom

import pydantic as _pyd


class ObjectStorageZipPath(_pyd.BaseModel):
    container: str
    path: str
    version: str | None = None

    @_pyd.field_validator("path", mode="after")
    @classmethod
    def _validate_path(cls, value: str) -> str:
        if not value.endswith(".zip"):
            raise ValueError("Path must point to .zip file.")

        return value


class RunnerJob(_pyd.BaseModel):
    id: str
    object_storage_path: ObjectStorageZipPath
    program: _pcom.PureWindowsPath
    args: _cabc.Sequence[_pcom.PureWindowsPath | str]
    working_dir: _pcom.PureWindowsPath | None = None
    results_glob_pattern: str | None = None
