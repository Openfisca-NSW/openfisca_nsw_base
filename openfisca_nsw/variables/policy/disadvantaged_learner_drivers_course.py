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
    definition_period = MONTH
    label = "Whether the learner has completed 50 hours of on-road driving, which excludes any 3-for-1 bonus driving hours"


# class creative_kids__voucher_amount(Variable):
#     value_type = int
#     entity = Person
#     definition_period = MONTH
#     label = "Calculates voucher amount for Creative Kids"

#     def formula(persons, period, parameters):
#         return (persons('creative_kids__child_meets_criteria', period)
#                 * parameters(period).creative_kids.voucher)


class disadvantaged_learner_drivers_course__learner_meets_criteria(Variable):
    value_type = bool
    entity = Person
    definition_period = MONTH
    label = "Whether the learner meets the criteria for a free drivers course"

    def formula(persons, period, parameters):
        max_age = parameters(period).disadvantaged_learner_drivers_course.max_age
        min_age = parameters(period).disadvantaged_learner_drivers_course.min_age
        age = persons('age', period)
        return (persons('has_valid_learner_licence', period)
                * persons('disadvantaged_learner_drivers_course__completed_driving_hours', period)
                * (persons('has_health_care_card', period)
                + persons('has_department_human_services_pensioner_concession_card', period))
                * (persons('has_stayed_in_Out_Of_Care_Home', period)
                + persons('currently_staying_in_Out_Of_Care_Home', period))
                * ((age >= min_age)
                * (age < max_age)))
