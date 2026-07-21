import collections.abc as _cabc
import typing as _tp

import pydantic as _pc
import resultes_pydantic_models.simulations.parameters.common.profiles as _pprofs


class MassFlowRateAndTemperature(_pc.BaseModel):
    mass_flow_rate_kg_per_h: float
    temperature_deg_C: float


class WasteHeatRecoverySource(_pc.BaseModel):
    name: str
    values: _tp.Annotated[
        _cabc.Sequence[MassFlowRateAndTemperature],
        _pc.Field(
            min_length=_pprofs.N_HOURS_PER_YEAR,
            max_length=_pprofs.N_HOURS_PER_YEAR,
        ),
    ]
