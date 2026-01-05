import typing as _tp

import pydantic as _pc
import resultes_pydantic_models.simulations.parameters.common as _common


class PtesPortRelativeHeights(_pc.BaseModel):
    """The heights ar relative: 1 is at the very top, 0.5 in the middle, etc."""

    top: float
    middle: float
    bottom: float

    @_pc.model_validator(mode="after")
    def _validate_port_heights_order(self) -> _tp.Self:
        if not (self.top > self.middle > self.bottom):
            raise ValueError("Port heights must decrease from top to bottom.")

        return self


class PtesStorage(_pc.BaseModel):
    volume: _common.ScaledValue[
        _tp.Literal["absolute_m3", "relative_to_demand_m3_per_MWh"]
    ]
    ports_relative_heights_1: PtesPortRelativeHeights = _pc.Field(
        description="The heights are relative: 1 means at the very top, 0.5 in the middle, etc."
    )
