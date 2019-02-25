# -*- coding: utf-8 -*-

# This file defines variables for the modelled legislation.
# A variable is a property of an Entity such as a Person, a Household…
# See https://openfisca.org/doc/key-concepts/variables.html

# Import from openfisca-core the common Python objects used to code the legislation in OpenFisca
from openfisca_core.model_api import *
# Import the Entities specifically defined for this tax and benefit system
from openfisca_nsw.entities import *


class active_kids__voucher_amount(Variable):
    value_type = int
    entity = Person
    definition_period = MONTH
    label = "Calculates voucher amount for Active Kids"

    def formula(persons, period, parameters):
        return persons('active_kids__is_entitled', period) \
            * parameters(period).active_kids.voucher


class active_kids__is_entitled(Variable):
    value_type = bool
    entity = Person
    definition_period = MONTH
    label = "Calculates entitlement to Active Kids"

    def formula(persons, period, parameters):
        return (
            persons.has_role(Family.PARENT)
            * persons('is_nsw_resident', period)
            * (54 <= persons('age_in_months', period) <= 216)
            * persons('is_enrolled_full_time', period)
            )
