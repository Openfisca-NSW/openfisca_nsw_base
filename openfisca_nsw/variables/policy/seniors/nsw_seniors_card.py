# -*- coding: utf-8 -*-

# This file defines variables for the modelled legislation.
# A variable is a property of an Entity such as a Person, a Household…
# See https://openfisca.org/doc/key-concepts/variables.html

# Import from openfisca-core the common Python objects used to code the legislation in OpenFisca
from openfisca_core.model_api import *
# Import the Entities specifically defined for this tax and benefit system
from openfisca_nsw.entities import *


class nsw_seniors_card_works_under_20hrs(Variable):
    value_type = bool
    entity = Person
    definition_period = MONTH
    label = "Whether the person works under 20 hours a week over a 12 month period"


class nsw_seniors_card_person_is_eligible(Variable):
    value_type = bool
    entity = Person
    definition_period = MONTH
    label = "Whether the person is eligible for a NSW seniors card"

    def formula(persons, period, parameters):
        return (
            (persons('age', period) >= parameters(period).nsw_seniors_card.min_age)
            * persons('is_permanent_nsw_resident', period)
            * persons('nsw_seniors_card_works_under_20hrs', period)
            )
