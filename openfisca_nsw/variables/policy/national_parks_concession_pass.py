# Import from openfisca-core the common Python objects used to code the legislation in OpenFisca
from openfisca_core.model_api import *
# Import the Entities specifically defined for this tax and benefit system
from openfisca_nsw.entities import *


class national_parks_concession_pass__person_meets_criteria(Variable):
    value_type = bool
    entity = Person
    definition_period = MONTH
    label = "person meets criteria for National Parks Concession Pass"

    def formula(persons, period, parameters):
        return (persons('has_department_human_services_pensioner_concession_card', period)
                + persons('has_department_veteran_affairs_gold_card_TPI_EDA', period)
                + persons('has_department_veteran_affairs_gold_card_war_widow', period)
                + (persons('has_department_veteran_affairs_gold_card_not_TPI_EDA', period) * persons('national_parks_concession_pass__person_receives_disability_pension', period))
                + (persons('has_department_veteran_affairs_gold_card_not_TPI_EDA', period) * persons('national_parks_concession_pass__person_receives_intermediate_pension', period))
                )


class national_parks_concession_pass__person_receives_disability_pension(Variable):
    value_type = bool
    entity = Person
    definition_period = MONTH
    label = "person receives disability pension"


class national_parks_concession_pass__person_receives_intermediate_pension(Variable):
    value_type = bool
    entity = Person
    definition_period = MONTH
    label = "person receives intermediate pension"
