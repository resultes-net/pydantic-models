import typing as _tp

from ..common import parameters_base as _pb
from .parameters import thermal_energy_storage as _tes


class TtesParameters(_pb.ParametersBase):
    type: _tp.Literal["ttes"]
    storage: _tes.TtesStorage
