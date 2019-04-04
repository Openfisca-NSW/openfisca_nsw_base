# Import from openfisca-core the common Python objects used to code the legislation in OpenFisca
from openfisca_core.model_api import *
# Import the Entities specifically defined for this tax and benefit system
from openfisca_nsw.entities import *


class is_australian_citizen(Variable):
    value_type = bool
    entity = Person
    definition_period = MONTH
    label = "Holds Australian Citizenship"


class is_permanent_resident(Variable):
    value_type = bool
    entity = Person
    definition_period = MONTH
    label = "Holds Australian Permanent Residency"
