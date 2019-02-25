# -*- coding: utf-8 -*-

# This file defines variables for the modelled legislation.
# A variable is a property of an Entity such as a Person, a Household…
# See https://openfisca.org/doc/key-concepts/variables.html

# Import from openfisca-core the common Python objects used to code the legislation in OpenFisca
from openfisca_core.model_api import *
# Import the Entities specifically defined for this tax and benefit system
from openfisca_nsw.entities import *


# This variable is a pure input: it doesn't have a formula
# class active_kids__is_parent(Variable):
#     value_type = bool
#     entity = Person
#     definition_period = MONTH
#     label = "Applicant is a parent"


# class active_kids__is_guardian(Variable):
#     value_type = bool
#     entity = Person
#     definition_period = MONTH
#     label = "Applicant is a guardian"


# class active_kids__is_carer(Variable):
#     value_type = bool
#     entity = Person
#     definition_period = MONTH
#     label = "Applicant is a carer"


class active_kids__is_nsw_resident(Variable):
    value_type = bool
    entity = Person
    definition_period = MONTH
    label = "Child is a NSW Resident"


class active_kids__is_enrolled_full_time(Variable):
    value_type = bool
    entity = Person
    definition_period = MONTH
    label = "Child is enrolled in full time education, including home schooling, and TAFE"


class active_kids__age_in_months(Variable):
    value_type = float
    entity = Person
    definition_period = MONTH
    label = "Childs age in months"


class active_kids__is_entitled(Variable):
    value_type = bool
    entity = Person
    definition_period = MONTH
    label = "Calculates entitlement to active kids"

    def formula(person, period, parameters):
        return (
            (
                person('active_kids__is_parent', period)
                | person('active_kids__is_guardian', period)
                | person('active_kids__is_carer', period)
                )
            and person('active_kids__is_nsw_resident', period)
            and (54 <= person('active_kids__age_in_months', period) <= 216)
            and person('active_kids__is_enrolled_full_time', period)
            )
