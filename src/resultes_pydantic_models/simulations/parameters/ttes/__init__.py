import typing as _tp

from .. import common as _com
from .parameters import thermal_energy_storage as _tes


class TtesParameters(_com.CommonParameters):
    type: _tp.Literal["ttes"]
    storage: _tes.TtesStorage
