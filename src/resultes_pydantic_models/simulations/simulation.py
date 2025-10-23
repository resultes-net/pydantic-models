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
class SimulationState(_enum.Enum):
    WAITING_FOR_VARIATIONS_CREATION = "waiting-for-variations-creation"
    CREATING_VARIATIONS = "creating-variations"
    WAITING_FOR_VARIATION_RUNS = "waiting-for-variation-runs"
    RUNNING_VARIATIONS = "running-variations"
    WAITING_FOR_CROSS_VARIATION_PROCESSING = "waiting-for-cross-variation-processing"
    CROSS_PROCESSING_VARIATIONS = "cross-processing-variations"
    DONE = "done"


class UpdateSimulation(_pyd.BaseModel):
    state: SimulationState


class SimulationBase(UpdateSimulation):
    id: str

    state: SimulationState = SimulationState.WAITING_FOR_VARIATIONS_CREATION
    state_changed_on: _pcom.AwarePastDatetime

    parameters: _params.Parameters

    created_on: _pcom.AwarePastDatetime

    user_id: str

    object_storage_url: _pyd.HttpUrl | None


class Simulation(SimulationBase):
    variations: _cabc.Sequence[_pvar.Variation]
