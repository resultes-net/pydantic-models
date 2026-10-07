import typing as _tp

import pydantic as _pc


class PowerLawCost(_pc.BaseModel):
    """A specific cost of `a * x**b`, in the cost region's currency per unit of `x`."""

    a: _pc.NonNegativeFloat
    b: float


class Financial(_pc.BaseModel):
    """The parameters of the levelized cost of heat (LCOH).

    All prices and costs are in today's money of the cost region's currency. The systems
    don't know about cost regions: only the client uses `cost_region`, for the defaults and
    to label prices and results with its currency.
    """

    cost_region: _tp.Literal["eu", "ch"]
    real_discount_rate_1: float = _pc.Field(
        gt=-1,
        description=(
            "Real, i.e., without inflation. A nominal rate n converts to a real rate r with"
            " inflation π as 1 + r = (1 + n) / (1 + π)."
        ),
    )
    fuel_price_per_kWh: _pc.NonNegativeFloat
    electricity_price_per_kWh: _pc.NonNegativeFloat
    lifetime_a: _pc.PositiveInt
    maintenance_rate_1: _pc.NonNegativeFloat = _pc.Field(
        description="Yearly maintenance costs as share of the investment."
    )
    boiler_efficiency_1: _pc.PositiveFloat
    storage_cost: PowerLawCost = _pc.Field(
        description="Per m³ of water equivalent storage volume, which is `x`."
    )
    collector_field_cost: PowerLawCost = _pc.Field(
        description="Per m² of collector aperture area, which is `x`."
    )
    heat_pump_cost_per_kW: _pc.NonNegativeFloat = _pc.Field(
        description="Per kW of thermal (condenser) power."
    )
    boiler_cost_per_kW: _pc.NonNegativeFloat = _pc.Field(
        description="Per kW of thermal power."
    )
