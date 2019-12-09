# Import from openfisca-core the common Python objects used to code the legislation in OpenFisca
from openfisca_core.model_api import *
# Import the Entities specifically defined for this tax and benefit system
from openfisca_nsw.entities import *


class is_charity(Variable):
    value_type = bool
    entity = Organisation
    definition_period = MONTH
    label = "Orgnaisation is a charity"


class is_not_for_profit(Variable):
    value_type = bool
    entity = Organisation
    definition_period = MONTH
    label = "Organisation is a not-for-profit"


class is_art_union(Variable):
    value_type = bool
    entity = Organisation
    definition_period = MONTH
    label = "Organisation is an art union"


class is_registered_club(Variable):
    value_type = bool
    entity = Organisation
    definition_period = MONTH
    label = "Organisation is a registered club"


class is_for_profit_business(Variable):
    value_type = bool
    entity = Organisation
    definition_period = MONTH
    label = "Organisation is a for-profit business"
