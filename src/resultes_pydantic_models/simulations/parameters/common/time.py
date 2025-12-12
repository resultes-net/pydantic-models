import math as _math
import typing as _tp

import pydantic as _pyd


class Time(_pyd.BaseModel):
    start: _pyd.NonNegativeInt
    stop: _pyd.PositiveInt
    dt_sim: _pyd.PositiveFloat

    @_pyd.model_validator(mode="after")
    def _validate(self) -> _tp.Self:
        if not (self.start < self.stop):
            raise ValueError("Stop must be larger than start.")

        return self

    @property
    def n_steps(self) -> int:
        duration = self.stop - self.start
        n_steps = _math.ceil(duration / self.dt_sim)
        return n_steps
