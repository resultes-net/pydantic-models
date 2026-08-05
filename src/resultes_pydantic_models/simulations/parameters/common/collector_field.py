import typing as _tp

import pydantic as _pc

from . import scaled_value as _sv


class PerformanceCoefficients(_pc.BaseModel):
    a0_1: float
    a1_kW_per_m2_per_K: float
    a2_kW_per_m2_per_K2: float
    a3_kJ_per_m3_per_K: float
    a4_1: float
    a5_kJ_per_m2_per_K: float


class IAM(_pc.BaseModel):
    name: str
    transversal_angles_degC: _tp.Annotated[
        list[float], _pc.Field(min_length=1, max_length=100)
    ]
    longitudinal_angles_degC: _tp.Annotated[
        list[float], _pc.Field(min_length=1, max_length=100)
    ]
    values: _tp.Annotated[list[float], _pc.Field(min_length=1, max_length=100 * 100)]

    @_pc.model_validator(mode="after")
    def _validate_n_values(self) -> _tp.Self:
        expected_n_values = len(self.transversal_angles_degC) * len(
            self.longitudinal_angles_degC
        )
        actual_n_values = len(self.values)

        if actual_n_values != expected_n_values:
            raise ValueError(
                f"Expected {expected_n_values} values but got {actual_n_values} values."
            )

        return self


class CollectorField(_pc.BaseModel):
    area: _sv.ScaledValue[_tp.Literal["absolute_m2", "relative_to_demand_m2_per_MWh"]]
    inclination_deg: float
    orientation_east_west_deg: float
    type: _tp.Literal["flat-plate", "parallel-trough"]
    performance_coefficients: PerformanceCoefficients
    nominal_massflow: _sv.ScaledValue[
        _tp.Literal["absolute_kg_per_h", "relative_to_collector_area_kg_per_h_m2"]
    ]
    iam: IAM
