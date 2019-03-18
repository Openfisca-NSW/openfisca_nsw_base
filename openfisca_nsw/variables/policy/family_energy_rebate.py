# -*- coding: utf-8 -*-

# This file defines variables for the modelled legislation.
# A variable is a property of an Entity such as a Person, a Household…
# See https://openfisca.org/doc/key-concepts/variables.html

# Import from openfisca-core the common Python objects used to code the legislation in OpenFisca
from openfisca_core.model_api import *
# Import the Entities specifically defined for this tax and benefit system
from openfisca_nsw.entities import *


# This is used to calculate whether persons are eligible for family energy rebate - Retail category
class family_energy_rebate__person_meets_retail_criteria(Variable):
    value_type = bool
    entity = Person
    definition_period = MONTH
    label = "Applicant meets criteria for Family Energy Rebate (Retail Customers)"
    reference = 'http://www.resourcesandenergy.nsw.gov.au/energy-consumers/financial-assistance?a=436725'

    def formula(persons, period, parameters):

        return (
            persons('is_nsw_resident', period) *
            persons('has_energy_account', period) *
            not_(persons('energy_provider_category', period)) *
            persons('is_ftb_recipient', period))

    
# This is used to calculate whether persons are eligible for family energy rebate - On Supply category
class family_energy_rebate__person_meets_supply_criteria(Variable):
    value_type = bool
    entity = Person
    definition_period = MONTH
    label = "Applicant meets criteria for Family Energy Rebate (On Supply Customers)"
    reference = 'http://www.resourcesandenergy.nsw.gov.au/energy-consumers/financial-assistance?a=436725'

    def formula(persons, period, parameters):

        return (
            persons('is_nsw_resident', period) *
            persons('has_energy_account', period) *
            persons('energy_provider_category', period) *
            persons('is_ftb_recipient', period))

    
# This is used to calculate the rebate amount for family energy rebate - for retail customers
class family_energy_rebate__retail_rebate_amount(Variable):
    value_type = int
    entity = Person
    definition_period = MONTH
    label = "Calculate family energy rebate (retail) amount"

    def formula(persons, period, parameters):
        condition_healthcare = persons('has_healthcare_card', period)
        condition_concession = persons('has_concession_card', period)
        condition_health_or_concession = condition_healthcare + condition_concession
        return select(
            [condition_health_or_concession, not_(condition_health_or_concession)]
            [persons('family_energy_rebate__person_meets_retail_criteria', period) * parameters(period).retail_min_rebate_amount, persons('family_energy_rebate__person_meets_retail_criteria', period) * parameters(period).retail_max_rebate_amount])

