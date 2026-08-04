import abc as _abc

import pydantic as _pc

from ..common import collector_field as _cf
from ..common import control as _ctrl
from ..common import demand as _demand
from ..common import time as _time
from ..common import waste_heat_recovery_source as _whrs


class ParametersBase(_pc.BaseModel, _abc.ABC):
    time: _time.Time
    demand: _demand.Demand
    collector_field: _cf.CollectorField
    waste_heat_recovery_source: _whrs.WasteHeatRecoverySource
    control: _ctrl.Control
