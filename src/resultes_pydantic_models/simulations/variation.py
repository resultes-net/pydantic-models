import enum as _enum

import pydantic as _pyd
import resultes_pydantic_models.common as _pcom


@_enum.verify(_enum.UNIQUE)
class VariationState(_enum.Enum):
    WAITING = "waiting"
    RUNNING = "running"
    DONE = "done"


class CreateVariation(_pyd.BaseModel):
    relative_deck_file_containing_dir_path: _pcom.PureWindowsPath


class Variation(CreateVariation):
    id: str
    created_on: _pcom.AwarePastDatetime
    state: VariationState = VariationState.WAITING
    state_changed_on: _pcom.AwarePastDatetime
    progress: _pyd.NonNegativeInt = 0
    simulation_id: str

    @_pyd.field_validator("progress", mode="after")
    @classmethod
    def _validate_progress(cls, value: int) -> int:
        if not 0 <= value <= 100:
            raise ValueError("Progress must be between 0 and 100, inclusive.")

        return value
