import typing as _tp
import collections.abc as _cabc

import pydantic as _pc

N_HOURS_PER_YEAR = 365 * 24


class Demand(_pc.BaseModel):
    name: str
    scaling_factor: _pc.NonNegativeFloat
    hourly_heat_demand_MW: _tp.Annotated[
        _cabc.Sequence[float],
        _pc.Field(min_length=N_HOURS_PER_YEAR, max_length=N_HOURS_PER_YEAR),
    ]
