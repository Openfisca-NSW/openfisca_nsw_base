# -*- coding: utf-8 -*-

# This file defines variables for the modelled legislation.
# A variable is a property of an Entity such as a Person, a Household…
# See https://openfisca.org/doc/key-concepts/variables.html

# Import from openfisca-core the common Python objects used to code the legislation in OpenFisca
from openfisca_core.model_api import *
# Import the Entities specifically defined for this tax and benefit system
from openfisca_nsw.entities import *


class NRMA_free2go__is_eligible(Variable):
    value_type = bool
    entity = Person
    definition_period = MONTH
    label = "Person is eligible for NRMA free2go"

    def formula(persons, period, parameters):
        return (
            (persons('is_nsw_resident', period) + persons('is_act_resident', period))
            * persons('NRMA_free2go__is_NRMA_member', period)
            * (persons('is_australian_citizen', period) + persons('is_permanent_resident', period))
            * (persons('age', period) >= parameters(period).NRMA_free2go.min_age)
            * (persons('age', period) <= parameters(period).NRMA_free2go.max_age)
            )


class NRMA_free2go__is_NRMA_member(Variable):
    value_type = bool
    entity = Person
    definition_period = MONTH
    label = "Person is an active NRMA member"


class NRMA_free2go__age_when_joining(Variable):
    value_type = int
    entity = Person
    definition_period = MONTH
    label = "Age the person was when becoming a free2go member"


class NRMA_free2go__membership_term(Variable):
    value_type = str
    entity = Person
    definition_period = MONTH
    label = "Person is an active NRMA member"


class NRMA_free2go__free2go_discount(Variable):
    value_type = float
    entity = Person
    definition_period = MONTH
    label = "Discount applied to free2go based on age and membership term"

    def formula(persons, period, parameters):
        discount_amount = select(  # calculate the discount amount
            [(persons('NRMA_free2go__age_when_joining', period) == 16), (persons('NRMA_free2go__age_when_joining', period) >= 17)],
            [parameters(period).NRMA_free2go.discount.by_year[persons('NRMA_free2go__membership_term', period)].sixteen, parameters(period).NRMA_free2go.discount.by_year[persons('NRMA_free2go__membership_term', period)].over_sixteen]
            )
        return select(  # if they qualify, return it, otherwise don't
            [persons('NRMA_free2go__is_eligible', period), not_(persons('NRMA_free2go__is_eligible', period))],
            [discount_amount, 0]
            )
