# Import from openfisca-core the common Python objects used to code the legislation in OpenFisca
from openfisca_core.model_api import *
# Import the Entities specifically defined for this tax and benefit system
from openfisca_nsw.entities import *


class is_parent(Variable):
    value_type = bool
    entity = Person
    definition_period = MONTH
    label = "is parent of children in family"


class is_guardian(Variable):
    value_type = bool
    entity = Person
    definition_period = MONTH
    label = "is parent of children in family"


class is_carer(Variable):
    value_type = bool
    entity = Person
    definition_period = MONTH
    label = "is parent of children in family"


class is_respite_carer:
    value_type = bool
    entity = Person
    definition_period = MONTH
    label = "person is a respite carer"


class is_carer_providing_short_term_placement:
    value_type = bool
    entity = Person
    definition_period = MONTH
    label = "carer providing short term placement of more than 3 months"
