# Import from openfisca-core the common Python objects used to code the legislation in OpenFisca
from openfisca_core.model_api import *
# Import the Entities specifically defined for this tax and benefit system
from openfisca_nsw.entities import *


class has_concession_card(Variable):
    value_type = bool
    entity = Person
    definition_period = MONTH
    label = "Has any one of the Department of Human Services concession or Healthcare cards - https://www.humanservices.gov.au/individuals/subjects/concession-and-health-care-cards"


class has_health_care_card(Variable):
    value_type = bool
    entity = Person
    definition_period = MONTH
    label = "Has any one of the Department of Human Services health care cards - https://www.humanservices.gov.au/individuals/subjects/concession-and-health-care-cards"


class has_department_human_services_pensioner_concession_card(Variable):
    value_type = bool
    entity = Person
    definition_period = MONTH
    label = "Has a Department of Human Services pensioner concession card"


class has_department_veteran_affairs_pensioner_concession_card(Variable):
    value_type = bool
    entity = Person
    definition_period = MONTH
    label = "Has a Department of Vterans Affairs concession card"


class has_department_veteran_affairs_gold_card_war_widow(Variable):
    value_type = bool
    entity = Person
    definition_period = MONTH
    label = "DVA Gold Card marked with either War Widow or War Widower Pension."


class has_department_veteran_affairs_gold_card_TPI_EDA(Variable):
    value_type = bool
    entity = Person
    definition_period = MONTH
    label = "DVA Gold Card marked with Totally and Permanently Incapacitated (TPI) or Disability Pension (EDA)."


class has_department_veteran_affairs_gold_card_not_TPI_EDA(Variable):
    value_type = bool
    entity = Person
    definition_period = MONTH
    label = "DVA Gold Card without Totally and Permanently Incapacitated (TPI) or Disability Pension (EDA) embossment."


class has_student_concession_card(Variable):
    value_type = bool
    entity = Person
    definition_period = MONTH
    label = "Holds a student concession card"


class has_transport_concession_entitlement_card(Variable):
    value_type = bool
    entity = Person
    definition_period = MONTH
    label = "Holds a transport entitlement concession card"


class has_international_pensioners_card(Variable):
    value_type = bool
    entity = Person
    definition_period = MONTH
    label = "Holds an international pensioners card"
