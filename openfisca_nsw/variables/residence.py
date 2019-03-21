# Import from openfisca-core the common Python objects used to code the legislation in OpenFisca
from openfisca_core.model_api import *
# Import the Entities specifically defined for this tax and benefit system
from openfisca_nsw.entities import *


class is_nsw_resident(Variable):
    value_type = bool
    entity = Person
    definition_period = MONTH
    label = "is a resident of New South Wales"

class is_act_resident(Variable):
    value_type = bool
    entity = Person
    definition_period = MONTH
    label = "is a resident of the Australian Capital Territory"
