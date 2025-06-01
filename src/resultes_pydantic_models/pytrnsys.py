import pathlib as _pl

import pydantic as _pyd


class ObjectStoragePath(_pyd.BaseModel):
    container: str
    path: str

class RunnerJob(_pyd.BaseModel):
    object_storage_path: ObjectStoragePath
    script_to_run_path: _pl.Path
