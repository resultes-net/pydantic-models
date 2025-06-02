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
    script_to_run: str
    working_dir: str | None = None
    results_dir_to_list: str | None = None
