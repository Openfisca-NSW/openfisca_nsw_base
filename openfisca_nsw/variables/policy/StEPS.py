# -*- coding: utf-8 -*-

# This file defines variables for the modelled legislation.
# A variable is a property of an Entity such as a Person, a Household…
# See https://openfisca.org/doc/key-concepts/variables.html

# Import from openfisca-core the common Python objects used to code the legislation in OpenFisca
from openfisca_core.model_api import *
# Import the Entities specifically defined for this tax and benefit system
from openfisca_nsw.entities import *


class StEPS__already_screened(Variable):
    value_type = bool
    entity = Person
    definition_period = MONTH
    label = "Whether the child has already had a StEPS screening"


class StEPS__child_is_joining_school(Variable):
    value_type = bool
    entity = Person
    definition_period = MONTH
    label = "Whether the child is due to join school next year"


class StEPS__child_meets_criteria(Variable):
    value_type = bool
    entity = Person
    definition_period = MONTH
    label = "child meets criteria for StEPS screening"
    reference = 'https://sport.nsw.gov.au/sectordevelopment/activekids'

    def formula(persons, period, parameters):
        return (
            not_(persons('StEPS__already_screened', period))
            * ((persons('age', period) >= parameters(period).StEPS.min_age)
              * (persons('age', period) <= parameters(period).StEPS.max_age))
            + ((persons('age', period) >= parameters(period).StEPS.age_if_joining_school)
              * persons('StEPS__child_is_joining_school', period)))
