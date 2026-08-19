import typing as _tp

import pydantic as _pyd

from .. import common as _com
from .parameters import thermal_energy_storage as _tes


class BtesSpecificParameters(_pyd.BaseModel):
    storage: _tes.BtesStorage


class BtesParameters(_com.CommonParameters, BtesSpecificParameters):
    type: _tp.Literal["btes"]
