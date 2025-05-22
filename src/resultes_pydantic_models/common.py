import datetime as _dt
import typing as _tp

import pydantic as _pyd


def utc_now() -> _dt.datetime:
    return _dt.datetime.now(_dt.UTC)


def is_timezone_aware_in_past(datetime: _dt.datetime) -> bool:
    if datetime.tzinfo is None:
        return False

    return datetime <= utc_now()


AwarePastDatetime = _tp.Annotated[
    _dt.datetime, _pyd.AfterValidator(is_timezone_aware_in_past)
]