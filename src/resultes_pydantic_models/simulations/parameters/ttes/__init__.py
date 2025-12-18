import typing as _tp

import pydantic as _pc

from ..common import collector_field as _cf
from ..common import demand as _demand
from ..common import time as _time
from .parameters import thermal_energy_storage as _tes


class TtesParameters(_pc.BaseModel):
    type: _tp.Literal["ttes"]
    time: _time.Time
    demand: _demand.Demand
    collector_field: _cf.CollectorField
    storage: _tes.TtesStorage
