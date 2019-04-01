# -*- coding: utf-8 -*-

# This file defines variables for the modelled legislation.
# A variable is a property of an Entity such as a Person, a Household…
# See https://openfisca.org/doc/key-concepts/variables.html

# Import from openfisca-core the common Python objects used to code the legislation in OpenFisca
from openfisca_core.model_api import *
# Import the Entities specifically defined for this tax and benefit system
from openfisca_nsw.entities import *


# This is used to calculate whether the youth is eligible for Teenage Education Payment
class teenage_education_payments__youth_meets_payment_criteria(Variable):
    value_type = bool
    entity = Person
    definition_period = MONTH
    label = "Youth meets criteria for Teenage Education Payment"
    reference = 'https://www.facs.nsw.gov.au/__data/assets/pdf_file/0004/319954/teenage_education_payment_guidelines.pdf'

    def formula(persons, period, parameters):
        min_age_in_months = 12 * parameters(period).teenage_education_payment.min_age
        upper_age_in_months = 12 * parameters(period).teenage_education_payment.upper_age
        age_in_months = persons('age_in_months', period)

        return (
            (persons('is_enrolled_in_school', period) + persons('is_nsw_resident', period))
            * (persons(age_in_months >= min_age_in_months) * (age_in_months < upper_age_in_months))
            + (persons('teenage_education_payments__youth_18_meets_payment_criteria', period))
            )


# This is used to calculate whether persons over 17 are still eligible for Teenage Education Payment
class teenage_education_payments__youth_18_meets_payment_criteria(Variable):
    value_type = bool
    entity = Person
    definition_period = MONTH
    label = "Youth is 18 but still meets criteria for Teenage Education Payment"

    def formula(persons, period, parameters):
        upper_age_in_months = 12 * parameters(period).teenage_education_payment.upper_age
        max_age_in_months = 12 * parameters(period).teenage_education_payment.max_age
        age_in_months = persons('age_in_months', period)
        # Youth age is over 17 but less than 19
        return (
            (age_in_months >= upper_age_in_months)
            * (age_in_months < max_age_in_months)
            )


class teenage_education_payments__adult_meets_payment_criteria (Variable):
    value_type = bool
    entity = Person
    definition_period = MONTH
    label = "person is a carer / short-term carer / guardian who is entitled to the Teenage Education Payment"

    def formula(persons, period, parameters):
        return (
            (persons('is_carer', period) + persons('is_guardian', period) + persons('is_carer_providing_short_term_placement', period))
            * not_(persons('is_respite_carer', period))
            * persons('teenage_education_payments__youth_meets_payment_criteria', period)
            * persons('teenage_education_payments__is_family_tax_benefit_recipient_partA_youth15', period)
            )


class teenage_education_payments__is_family_tax_benefit_recipient_partA_youth15 (Variable):
    value_type = bool
    entity = Person
    definition_period = MONTH
    label = "carer or guardian received Family Tax Benefit part A when young person was 15 years old"


class teenage_education_payments__amount (Variable):
    value_type = int
    entity = Person
    definition_period = MONTH
    label = "Teenage Education Paymnent amount"

    def formula(persons, period, parameters):
        return persons('teenage_education_payments__adult_meets_payment_criteria', period) \
            * parameters(period).teenage_education_payment.payment
