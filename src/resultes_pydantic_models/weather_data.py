import pydantic as _pyd


class TM2File(_pyd.BaseModel):
    name: str | None
    file_name: str
    contents: _pyd.Base64Str
