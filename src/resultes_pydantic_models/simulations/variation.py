import enum as _enum
import pathlib as _pl

import pydantic as _pyd
import resultes_pydantic_models.common as _pcom


@_enum.verify(_enum.UNIQUE)
class VariationState(_enum.Enum):
    WAITING = "waiting"
    RUNNING = "running"
    DONE = "done"


class CreateVariation(_pyd.BaseModel):
    relative_deck_file_path: _pl.PureWindowsPath


class Variation(CreateVariation):
    id: str | None
    created_on: _pcom.AwarePastDatetime
    state: VariationState = VariationState.WAITING
    simulation_id: str
