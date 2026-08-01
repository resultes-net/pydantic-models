import typing as _tp

import pydantic as _pc
import resultes_pydantic_models.simulations.parameters.common as _common
import resultes_pydantic_models.simulations.parameters.common.tes_relative_port_heights as _trph


class TtesStorage(_pc.BaseModel):
    volume: _common.ScaledValue[
        _tp.Literal[
            "absolute_m3",
            "relative_to_demand_m3_per_MWh",
            "relative_to_collector_area_m3_per_m2",
        ]
    ]
    height_to_diameter_ratio_1: float
    location: _tp.Literal["above-ground-free-standing", "below-ground-buried"]
    heat_conductance_kW_per_m2_per_K: float
    ports_relative_heights_1: _trph.TesRelativePortHeights = _pc.Field(
        description="The heights are relative: 1 means at the very top, 0.5 in the middle, etc."
    )
