import typing as _tp

import pydantic as _pyd

from .. import common as _com
from .parameters import thermal_energy_storage as _tes


class PtesSpecificParameters(_pyd.BaseModel):
    storage: _tes.PtesStorage


class PtesParameters(_com.CommonParameters, PtesSpecificParameters):
    type: _tp.Literal["ptes"]
