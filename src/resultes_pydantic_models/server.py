import collections.abc as _cabc

import pydantic as _pyd
import resultes_pydantic_models.simulations.simulation as _psim
import resultes_pydantic_models.simulations.variation as _pvar


class WaitingVariations(_pyd.BaseModel):
    waiting_variations: _cabc.Sequence[_pvar.Variation]
    associated_simulations: _cabc.Sequence[_psim.Simulation]
    other_variations: _cabc.Sequence[_pvar.Variation]
