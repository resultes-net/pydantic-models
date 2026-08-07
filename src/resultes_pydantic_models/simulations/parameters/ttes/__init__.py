import typing as _tp

import pydantic as _pyd

from .. import common as _com
from .parameters import thermal_energy_storage as _tes


class TtesSpecificParameters(_pyd.BaseModel):
    storage: _tes.TtesStorage


class TtesParameters(_com.CommonParameters, TtesSpecificParameters):
    type: _tp.Literal["ttes"]
