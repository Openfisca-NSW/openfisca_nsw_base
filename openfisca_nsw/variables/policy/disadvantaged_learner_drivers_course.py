# -*- coding: utf-8 -*-

# This file defines variables for the modelled legislation.
# A variable is a property of an Entity such as a Person, a Household…
# See https://openfisca.org/doc/key-concepts/variables.html

# Import from openfisca-core the common Python objects used to code the legislation in OpenFisca
from openfisca_core.model_api import *
# Import the Entities specifically defined for this tax and benefit system
from openfisca_nsw.entities import *


class disadvantaged_learner_drivers_course__completed_driving_hours(Variable):
    value_type = bool
    entity = Person
    definition_period = YEAR
    set_input = set_input_dispatch_by_period
    label = "Whether the learner has completed 50 hours of on-road driving, which excludes any 3-for-1 bonus driving hours"


# class creative_kids__voucher_amount(Variable):
#     value_type = int
#     entity = Person
#     definition_period = MONTH
#     label = "Calculates voucher amount for Creative Kids"

#     def formula(persons, period, parameters):
#         return (persons('creative_kids__child_meets_criteria', period)
#                 * parameters(period).creative_kids.voucher)