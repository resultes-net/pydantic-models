import enum as _enum

import pydantic as _pyd
import resultes_pydantic_models.simulations.parameters.ttes as _pttes

import resultes_server.database_utils.helpers as _dbh


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


class Simulation(_pyd.BaseModel):
    parameters: _pttes.TtesParameters = _pyd.Field(discriminator="type")

    id: str | None
    created_on: _dbh.AwarePastDatetime

    user_id: str

    object_storage_url: _pyd.HttpUrl | None = _dbh.HTTP_URL_FIELD

    state: SimulationState = SimulationState.WAITING_FOR_VARIATIONS_CREATION
    state_changed_on: _dbh.AwarePastDatetime = _dbh.UTC_NOW_FIELD
