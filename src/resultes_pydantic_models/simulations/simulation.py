import collections.abc as _cabc
import enum as _enum

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
    pass


class GetSimulation(SimulationBase, UpdateSimulation):
    id: _pcom.MaxLenStr

    state: SimulationState = SimulationState.WAITING_FOR_VARIATIONS_CREATION
    state_changed_on: _pcom.AwarePastDatetime
    progress: _pyd.NonNegativeInt = 0

    created_on: _pcom.AwarePastDatetime

    user_id: _pcom.MaxLenStr

    variations: _cabc.Sequence[_pvar.Variation] = []


class Simulation(GetSimulation, WithParameters):
    pass
