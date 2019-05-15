# Import from openfisca-core the common Python objects used to code the legislation in OpenFisca
from openfisca_core.model_api import *
# Import the Entities specifically defined for this tax and benefit system
from openfisca_nsw.entities import *


class single_promotion(Variable):
    value_type = bool
    entity = Organisation
    definition_period = DAY
    label = "Will the organisation be running a single type of trade promotion/lottery?"


class online_application_lodgement(Variable):
    value_type = bool
    entity = Organisation
    definition_period = DAY
    label = "Will the lodgement of the permit application be made online?"


class permit_fee(Variable):
    value_type = int
    entity = Organisation
    definition_period = DAY
    label = "Calculate permit fee based on multiple or single promotions and value of total prizes"
