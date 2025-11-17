import typing as _tp

import pydantic as _pc
import resultes_pydantic_models.simulations.parameters.common as _common


class PtesStorage(_pc.BaseModel):
    volume: _common.ScaledValue[
        _tp.Literal["absolute_m3", "relative_to_demand_m3_per_MWh"]
    ]
