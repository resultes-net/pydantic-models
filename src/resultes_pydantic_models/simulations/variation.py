import enum as _enum

import pydantic as _pyd
import resultes_pydantic_models.common as _pcom


@_enum.verify(_enum.UNIQUE)
class VariationState(_enum.Enum):
    WAITING = "waiting"
    RUNNING = "running"
    DONE = "done"


class UpdateVariation(_pyd.BaseModel):
    state: VariationState


class CreateVariation(_pyd.BaseModel):
    relative_deck_file_containing_dir_path: _pcom.PureWindowsPath


class VariationBase(CreateVariation, UpdateVariation):
    created_on: _pcom.AwarePastDatetime
    state: VariationState = VariationState.WAITING
    state_changed_on: _pcom.AwarePastDatetime
    simulation_id: str


class Variation(VariationBase):
    id: str
