import enum as _enum
import typing as _tp

import pydantic as _pyd
import resultes_pydantic_models.common as _pcom
import resultes_pydantic_models.simulations.parameters as _params
import resultes_pydantic_models.simulations.variation as _pvar


@_enum.verify(_enum.UNIQUE)
class Type(_enum.Enum):
    TTES = "ttes"
    PTES = "ptes"
    BTES = "btes"


@_enum.verify(_enum.UNIQUE)
class SimulationState(str, _enum.Enum):
    WAITING_FOR_VARIATIONS_CREATION = "waiting-for-variations-creation"
    CREATING_VARIATIONS = "creating-variations"
    WAITING_FOR_VARIATION_RUNS = "waiting-for-variation-runs"
    RUNNING_VARIATIONS = "running-variations"
    WAITING_FOR_CROSS_VARIATION_PROCESSING = "waiting-for-cross-variation-processing"
    CROSS_PROCESSING_VARIATIONS = "cross-processing-variations"
    DONE = "done"
    ERROR = "error"


@_enum.verify(_enum.UNIQUE)
class Location(str, _enum.Enum):
    BERLIN = "Berlin"
    BRUSSELS = "Brussels"
    COPENHAGEN = "Copenhagen"
    MADRID = "Madrid"
    ZURICH = "Zurich"


class UpdateSimulation(_pyd.BaseModel):
    state: SimulationState


class SimulationBase(_pyd.BaseModel):
    name: _pcom.MaxLenStr
    location: Location
    type: Type


class WithParameters(_pyd.BaseModel):
    parameters: _params.Parameters


class CreateSimulation(SimulationBase, WithParameters):
    @_pyd.model_validator(mode="after")
    def _ensure_types_agree(self) -> _tp.Self:
        return _ensure_types_agree(self)


class GetSimulation(SimulationBase, UpdateSimulation):
    id: _pcom.MaxLenStr

    state: SimulationState = SimulationState.WAITING_FOR_VARIATIONS_CREATION
    state_changed_on: _pcom.AwarePastDatetime
    progress: _pyd.NonNegativeInt = 0

    created_on: _pcom.AwarePastDatetime

    user_id: _pcom.MaxLenStr


class WithVariations(_pyd.BaseModel):
    variations: list[_pvar.Variation]


class Simulation(GetSimulation, WithVariations):
    pass


class SimulationWithParams(Simulation, WithParameters):
    @_pyd.model_validator(mode="after")
    def _ensure_types_agree(self) -> _tp.Self:
        return _ensure_types_agree(self)


class _HasTwoTypes(_tp.Protocol):
    type: Type
    parameters: _params.Parameters


def _ensure_types_agree[S: _HasTwoTypes](simulation: S) -> S:
    simulation_type = simulation.type.value
    parameters_type = simulation.parameters.values.type

    if simulation_type != parameters_type:
        raise ValueError(
            f"The system type given on the simulation ({simulation_type}) and in the parameters ({parameters_type}) must agree."
        )

    return simulation
