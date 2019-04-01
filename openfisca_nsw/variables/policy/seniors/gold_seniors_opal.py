# -*- coding: utf-8 -*-

# This file defines variables for the modelled legislation.
# A variable is a property of an Entity such as a Person, a Household…
# See https://openfisca.org/doc/key-concepts/variables.html

# Import from openfisca-core the common Python objects used to code the legislation in OpenFisca
from openfisca_core.model_api import *
# Import the Entities specifically defined for this tax and benefit system
from openfisca_nsw.entities import *


class gold_seniors_opal_person_is_eligible(Variable):
    value_type = bool
    entity = Person
    definition_period = ETERNITY
    label = "Person is eligible for Gold Pensioners' Opal Card"

    def formula(persons, period, parameters):
        return (
            (persons('nsw_seniors_card_person_is_eligible', period) * persons('has_nsw_seniors_card', period))
            + persons('has_nsw_seniors_card', period)
            + persons('has_act_seniors_card', period)
            )
