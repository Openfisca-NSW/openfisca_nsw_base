# Import from openfisca-core the common Python objects used to code the legislation in OpenFisca
from openfisca_core.model_api import *
# Import the Entities specifically defined for this tax and benefit system
from openfisca_nsw.entities import *


class is_energy_account_holder(Variable):
    value_type = bool
    entity = Person
    definition_period = MONTH
    label = "registered an energy account in their own name"


class energy_provider_supply_customer(Variable):
    value_type = bool
    entity = Person
    definition_period = MONTH
    label = "Does the applicant receive their energy bill from a strata manager/community village operator?"
