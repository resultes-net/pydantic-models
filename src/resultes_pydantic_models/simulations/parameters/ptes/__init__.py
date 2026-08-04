import typing as _tp

from ..common import parameters_base as _pb
from .parameters import thermal_energy_storage as _tes


class PtesParameters(_pb.ParametersBase):
    type: _tp.Literal["ptes"]
    storage: _tes.PtesStorage
