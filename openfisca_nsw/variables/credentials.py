# Import from openfisca-core the common Python objects used to code the legislation in OpenFisca
from openfisca_core.model_api import *
# Import the Entities specifically defined for this tax and benefit system
from openfisca_nsw.entities import *


class has_valid_learner_licence(Variable):
    value_type = bool
    entity = Person
    definition_period = MONTH
    label = "has a valid learners licence"
