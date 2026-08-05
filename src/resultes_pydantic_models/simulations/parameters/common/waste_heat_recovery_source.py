import typing as _tp

import pydantic as _pc

from .profiles import N_HOURS_PER_YEAR


class WasteHeatRecoverySource(_pc.BaseModel):
    name: str
    mass_flow_rates_kg_per_h: _tp.Annotated[
        list[_pc.NonNegativeFloat],
        _pc.Field(
            min_length=N_HOURS_PER_YEAR,
            max_length=N_HOURS_PER_YEAR,
        ),
    ]
    temperatures_deg_C: _tp.Annotated[
        list[_tp.Annotated[float, _pc.Field(ge=0, le=100)]],
        _pc.Field(
            min_length=N_HOURS_PER_YEAR,
            max_length=N_HOURS_PER_YEAR,
        ),
    ]
