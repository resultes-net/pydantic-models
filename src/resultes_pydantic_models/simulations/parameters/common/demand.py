import typing as _tp
import collections.abc as _cabc

import pydantic as _pc

N_HOURS_PER_YEAR = 365 * 24


class PreDefinedProfile(_pc.BaseModel):
    profile_type: _tp.Literal["predefined"]
    name: str


class UserProvidedProfile(_pc.BaseModel):
    profile_type: _tp.Literal["user-provided"]
    hourly_heat_demand_kW: _tp.Annotated[
        _cabc.Sequence[float],
        _pc.Field(min_length=N_HOURS_PER_YEAR, max_length=N_HOURS_PER_YEAR),
    ]


class Demand(_pc.BaseModel):
    profile: _tp.Union[PreDefinedProfile, UserProvidedProfile] = _pc.Field(
        discriminator="profile_type"
    )
