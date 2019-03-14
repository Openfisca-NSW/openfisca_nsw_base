# Import from openfisca-core the common Python objects used to code the legislation in OpenFisca
from openfisca_core.model_api import *
# Import the Entities specifically defined for this tax and benefit system
from openfisca_nsw.entities import *


class low_income_rebate_qualifier(Variable):
    value_type = bool
    entity = Person
    definition_period = MONTH
    label = "is a qualifier of the low income household rebate"
