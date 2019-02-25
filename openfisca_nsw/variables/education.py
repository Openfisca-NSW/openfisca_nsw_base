# Import from openfisca-core the common Python objects used to code the legislation in OpenFisca
from openfisca_core.model_api import *
# Import the Entities specifically defined for this tax and benefit system
from openfisca_nsw.entities import *


class is_enrolled_full_time(Variable):
    value_type = bool
    entity = Person
    definition_period = MONTH
    label = "Child is enrolled in full time education, including home schooling, and TAFE"
