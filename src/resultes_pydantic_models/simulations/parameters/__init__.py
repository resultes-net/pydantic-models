import pydantic as _pyd

from . import ptes as _ptes
from . import ttes as _ttes


class Parameters(_pyd.BaseModel):
    values: _ttes.TtesParameters | _ptes.PtesParameters = _pyd.Field(
        discriminator="type"
    )
