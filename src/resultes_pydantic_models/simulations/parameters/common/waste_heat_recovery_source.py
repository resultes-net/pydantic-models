import collections.abc as _cabc
import typing as _tp

import pydantic as _pc
from resultes_pydantic_models.simulations.parameters.common.profiles import (
    N_HOURS_PER_YEAR,
)


class MassFlowRateAndTemperature(_pc.BaseModel):
    mass_flow_rate_kg_per_h: _pc.NonNegativeFloat
    temperature_deg_C: _tp.Annotated[float, _pc.Field(ge=0, le=100)]


class WasteHeatRecoverySource(_pc.BaseModel):
    name: str
    hourly_values: _tp.Annotated[
        _cabc.Sequence[MassFlowRateAndTemperature],
        _pc.Field(
            min_length=N_HOURS_PER_YEAR,
            max_length=N_HOURS_PER_YEAR,
        ),
    ]
