import typing as _tp

import pydantic as _pc
import resultes_pydantic_models.simulations.parameters.common.scaled_value as _common


class HeatExchanger(_pc.BaseModel):
    fluid_to_ground_resistance_m_K_per_W: float
    pipe_to_pipe_resistance_m_K_per_W: float


class BtesStorage(_pc.BaseModel):
    n_boreholes: _common.ScaledValue[
        _tp.Literal[
            "absolute_1",
            "relative_to_demand_1_per_MWh",
            "relative_to_collector_area_1_per_m2",
        ]
    ]
    borehole_spacing_m: float
    borehole_depth_m: float
    heat_exchanger: HeatExchanger
