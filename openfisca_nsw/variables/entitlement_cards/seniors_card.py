# Import from openfisca-core the common Python objects used to code the legislation in OpenFisca
from openfisca_core.model_api import *
# Import the Entities specifically defined for this tax and benefit system
from openfisca_nsw.entities import *


class has_any_seniors_card(Variable):
    value_type = bool
    entity = Person
    definition_period = MONTH
    label = "Holds a pensioner concession card from any Australian state or territory."

    def formula(persons, period, parameters):
        return (
            persons('has_nsw_seniors_card', period) +
            persons('has_act_seniors_card', period) +
            persons('has_nt_seniors_card', period) +
            persons('has_qld_seniors_card', period) +
            persons('has_sa_seniors_card', period) +
            persons('has_tas_seniors_card', period) +
            persons('has_vic_seniors_card', period) +
            persons('has_wa_seniors_card', period) +
            )


class has_nsw_seniors_card(Variable):
    value_type = bool
    entity = Person
    definition_period = MONTH
    label = "Holds a pensioner concession card from New South Wales."


class has_act_seniors_card(Variable):
    value_type = bool
    entity = Person
    definition_period = MONTH
    label = "Holds a pensioner concession card from the Australian Capital Territory."


class has_nt_seniors_card(Variable):
    value_type = bool
    entity = Person
    definition_period = MONTH
    label = "Holds a pensioner concession card from the Northern Territory."


class has_qld_seniors_card(Variable):
    value_type = bool
    entity = Person
    definition_period = MONTH
    label = "Holds a pensioner concession card from Queensland."


class has_sa_seniors_card(Variable):
    value_type = bool
    entity = Person
    definition_period = MONTH
    label = "Holds a pensioner concession card from South Australia."


class has_tas_seniors_card(Variable):
    value_type = bool
    entity = Person
    definition_period = MONTH
    label = "Holds a pensioner concession card from Tasmania."


class has_vic_seniors_card(Variable):
    value_type = bool
    entity = Person
    definition_period = MONTH
    label = "Holds a pensioner concession card from Victoria."


class has_wa_seniors_card(Variable):
    value_type = bool
    entity = Person
    definition_period = MONTH
    label = "Holds a pensioner concession card from Western Australia."
