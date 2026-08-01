import typing as _tp

import pydantic as _pc


class TesRelativePortHeights(_pc.BaseModel):
    """The heights ar relative: 1 is at the very top, 0.5 in the middle, etc."""

    top: float
    middle: float
    bottom: float

    @_pc.model_validator(mode="after")
    def _validate_port_heights_order(self) -> _tp.Self:
        if not (self.top > self.middle > self.bottom):
            raise ValueError("Port heights must decrease from top to bottom.")

        return self
