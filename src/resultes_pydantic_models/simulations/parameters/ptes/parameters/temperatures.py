import pydantic as _pc


class Temperatures(_pc.BaseModel):
    demand_setpoint_degC: float
    boiler_output_setpoint_degC: float
    heat_pump_output_setpoint_degC: float
    storage_maximum_degC: float
    collector_output_setpoint_degC: float
