# -*- coding: utf-8 -*-

# This file defines variables for the modelled legislation.
# A variable is a property of an Entity such as a Person, a Household…
# See https://openfisca.org/doc/key-concepts/variables.html

# Import from openfisca-core the common Python objects used to code the legislation in OpenFisca
from openfisca_core.model_api import *
# Import the Entities specifically defined for this tax and benefit system
from openfisca_nsw.entities import *


class will_preparation_eligible_for_free_will_preparation(Variable):
    value_type = bool
    entity = Person
    definition_period = ETERNITY
    label = "Whether the child is due to join school next year"


    def formula(persons, period, parameters):
        return (
            persons('is_full_age_pension_recipient', period) +
            persons('is_veterans_pension_recipient', period)
            )
