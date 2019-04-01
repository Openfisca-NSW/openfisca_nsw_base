# -*- coding: utf-8 -*-

# This file defines variables for the modelled legislation.
# A variable is a property of an Entity such as a Person, a Household…
# See https://openfisca.org/doc/key-concepts/variables.html

# Import from openfisca-core the common Python objects used to code the legislation in OpenFisca
from openfisca_core.model_api import *
# Import the Entities specifically defined for this tax and benefit system
from openfisca_nsw.entities import *


class national_parks_seniors_person_is_eligible(Variable):
    value_type = bool
    entity = Person
    definition_period = MONTH
    label = "Whether the person is eligible for seniors' discount annual park passes at approx 20% discount. https://www.nationalparks.nsw.gov.au/passes-and-fees/discount-and-concession-passes#seniors-discount-annual-park-passes"

    def formula(persons, period, parameters):
        return (
            persons('has_any_seniors_card', period)
            )
