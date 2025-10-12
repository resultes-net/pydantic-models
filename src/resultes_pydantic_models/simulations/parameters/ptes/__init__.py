import typing as _tp

import pydantic as _pc

from .parameters import thermal_energy_storage as _tes
from ..common import collector_field as _cf
from ..common import demand as _demand


class PtesParameters(_pc.BaseModel):
    type: _tp.Literal["ptes"]
    demand: _demand.Demand
    collector_field: _cf.CollectorField
    storage: _tes.PtesStorage
