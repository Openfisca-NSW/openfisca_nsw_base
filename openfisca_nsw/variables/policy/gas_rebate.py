# -*- coding: utf-8 -*-

# This file defines variables for the modelled legislation.
# A variable is a property of an Entity such as a Person, a Household…
# See https://openfisca.org/doc/key-concepts/variables.html

# Import from openfisca-core the common Python objects used to code the legislation in OpenFisca
from openfisca_core.model_api import *
# Import the Entities specifically defined for this tax and benefit system
from openfisca_nsw.entities import *


# This is used to calculate whether persons are eligible for family energy rebate - Retail category
class gas_rebate__person_holds_valid_concession_card(Variable):
    value_type = bool
    entity = Person
    definition_period = MONTH
    label = "Applicant holds a qualifying concession card for Gas Rebate (Retail Customers)"
    reference = 'https://www.service.nsw.gov.au/transaction/apply-gas-rebate-retail-customers'

    def formula(persons, period, parameters):
        return (
            persons('has_health_care_card', period) *
            persons('has_department_human_services_pensioner_concession_card', period) *
            persons('has_department_veteran_affairs_pensioner_concession_card', period) *
            persons('has_department_veteran_affairs_gold_card', period))


class gas_rebate__person_meets_retail_criteria(Variable):
    value_type = bool
    entity = Person
    definition_period = MONTH
    label = "Applicant meets criteria for Gas (Retail Customers)"
    reference = 'https://www.service.nsw.gov.au/transaction/apply-gas-rebate-retail-customers'

    def formula(persons, period, parameters):
        return (
            persons('is_nsw_resident', period) *
            persons('is_energy_account_holder', period) *
            not_(persons('energy_provider_supply_customer', period)) *
            persons('retail_gas_rebate__person_holds_valid_concession_card', period))


class gas_rebate__person_meets_supply_criteria(Variable):
    value_type = bool
    entity = Person
    definition_period = MONTH
    label = "Applicant meets criteria for Gas (Retail Customers)"
    reference = 'https://www.service.nsw.gov.au/transaction/apply-gas-rebate-retail-customers'

    def formula(persons, period, parameters):
        return (
            persons('is_nsw_resident', period) *
            persons('is_energy_account_holder', period) *
            not_(persons('energy_provider_supply_customer', period)) *
            persons('retail_gas_rebate__person_holds_valid_concession_card', period))
