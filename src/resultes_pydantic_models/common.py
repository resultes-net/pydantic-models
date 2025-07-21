import datetime as _dt
import pathlib as _pl
import typing as _tp

import pydantic as _pyd


def utc_now() -> _dt.datetime:
    return _dt.datetime.now(_dt.UTC)


def is_timezone_aware_in_past(datetime: _dt.datetime) -> _dt.datetime:
    if datetime.tzinfo is None:
        raise ValueError("Datetime must have an explicit time zone.", datetime)

    if datetime >= utc_now():
        raise ValueError("Datetime must be in the past.", datetime)

    return datetime


AwarePastDatetime = _tp.Annotated[
    _dt.datetime, _pyd.AfterValidator(is_timezone_aware_in_past)
]


def _deserialize_pure_windows_path(serialized_path: str) -> _pl.PureWindowsPath:
    return _pl.PureWindowsPath(serialized_path)


def _serialize_pure_windows_path(path: _pl.PureWindowsPath) -> str:
    return str(path)


PureWindowsPath = _tp.Annotated[
    _pl.PureWindowsPath,
    _pyd.PlainValidator(_deserialize_pure_windows_path),
    _pyd.PlainSerializer(_serialize_pure_windows_path),
]
