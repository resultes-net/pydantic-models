import pydantic as _pc

from . import collector_field as _cf
from . import control as _ctrl
from . import demand as _demand
from . import time as _time
from . import waste_heat_recovery_source as _whrs


class CommonParameters(_pc.BaseModel):
    time: _time.Time
    demand: _demand.Demand
    collector_field: _cf.CollectorField
    waste_heat_recovery_source: _whrs.WasteHeatRecoverySource
    control: _ctrl.Control
