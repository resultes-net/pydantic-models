import pathlib as _pl

import pydantic as _pyd
import resultes_pydantic_models.common as _pcom


def test_create_pure_windows_path() -> None:
    type_adapter = _pyd.TypeAdapter(_pcom.PureWindowsPath)
    path = type_adapter.validate_strings(r"C:\path\to\file")
    assert isinstance(path, _pl.PureWindowsPath)
    assert str(path) == r"C:\path\to\file"
