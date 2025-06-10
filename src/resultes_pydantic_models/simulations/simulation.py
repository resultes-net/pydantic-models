import enum as _enum

import pydantic as _pyd
import resultes_pydantic_models.common as _pcom
import resultes_pydantic_models.simulations.parameters.ttes as _pttes


@_enum.verify(_enum.UNIQUE)
class Type(_enum.Enum):
    TTES = "ttes"
    PTES = "ptes"
    BTES = "btes"


@_enum.verify(_enum.UNIQUE)
class SimulationState(_enum.Enum):
    WAITING_FOR_VARIATIONS_CREATION = "waiting-for-variations-creation"
    WAITING_FOR_VARIATION_RUNS = "waiting-for-variation-runs"
    WAITING_FOR_CROSS_VARIATION_PROCESSING = "waiting-for-cross-variation-processing"
    DONE = "done"


class UpdateSimulation(_pyd.BaseModel):
    state: SimulationState = SimulationState.WAITING_FOR_VARIATIONS_CREATION


class Simulation(UpdateSimulation):
    parameters: _pttes.TtesParameters = _pyd.Field(discriminator="type")

    id: str | None
    created_on: _pcom.AwarePastDatetime

    user_id: str

    object_storage_url: _pyd.HttpUrl | None

    state_changed_on: _pcom.AwarePastDatetime
