# Import from openfisca-core the common Python objects used to code the legislation in OpenFisca
from openfisca_core.model_api import *
# Import the Entities specifically defined for this tax and benefit system
from openfisca_nsw.entities import *


class has_concession_card(Variable):
    value_type = bool
    entity = Person
    definition_period = MONTH
    label = "Has one of the Department of Human Services concession or Healthcare cards - https://www.humanservices.gov.au/individuals/subjects/concession-and-health-care-cards"
