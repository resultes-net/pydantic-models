import typing as _tp

import pydantic as _pc

from . import profiles as _pprofs


class Demand(_pc.BaseModel):
    name: str
    scaling_factor: _pc.NonNegativeFloat
    hourly_heat_demand_MW: _tp.Annotated[
        list[float],
        _pc.Field(
            min_length=_pprofs.N_HOURS_PER_YEAR,
            max_length=_pprofs.N_HOURS_PER_YEAR,
        ),
    ]
