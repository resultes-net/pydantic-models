import pydantic as _pc


class Control(_pc.BaseModel):
    demand_temperature_setpoint_degC: float
    demand_delta_T_degC: float
    storage_temperature_maximum_degC: float
