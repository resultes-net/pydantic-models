import enum as _enum

import pydantic as _pyd
import resultes_pydantic_models.common as _pcom
import resultes_pydantic_models.simulations.parameters.ptes as _pptes
import resultes_pydantic_models.simulations.parameters.ttes as _pttes


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
    state: SimulationState = SimulationState.WAITING_FOR_VARIATIONS_CREATION

    parameters: _pttes.TtesParameters | _pptes.PtesParameters = _pyd.Field(
        discriminator="type"
    )

    created_on: _pcom.AwarePastDatetime

    user_id: str

    object_storage_url: _pyd.HttpUrl | None

    state_changed_on: _pcom.AwarePastDatetime


class Simulation(SimulationBase):
    id: str
