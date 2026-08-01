import typing as _tp

import pydantic as _pc

from ..common import collector_field as _cf
from ..common import control as _ctrl
from ..common import demand as _demand
from ..common import time as _time
from ..common import waste_heat_recovery_source as _whrs
from .parameters import thermal_energy_storage as _tes


class TtesParameters(_pc.BaseModel):
    type: _tp.Literal["ttes"]
    time: _time.Time
    demand: _demand.Demand
    collector_field: _cf.CollectorField
    waste_heat_recovery_source: _whrs.WasteHeatRecoverySource
    storage: _tes.TtesStorage
    control: _ctrl.Control
