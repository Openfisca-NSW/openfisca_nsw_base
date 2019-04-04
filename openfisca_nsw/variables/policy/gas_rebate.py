# -*- coding: utf-8 -*-

# This file defines variables for the modelled legislation.
# A variable is a property of an Entity such as a Person, a Household…
# See https://openfisca.org/doc/key-concepts/variables.html

# Import from openfisca-core the common Python objects used to code the legislation in OpenFisca
from openfisca_core.model_api import *
# Import the Entities specifically defined for this tax and benefit system
from openfisca_nsw.entities import *


class gas_rebate__already_issued_in_financial_year(Variable):
    value_type = bool
    entity = Person
    definition_period = MONTH
    set_input = set_input_dispatch_by_period
    label = "Whether the user has already had a gas rebate this financial year"


class gas_rebate__person_holds_valid_concession_card(Variable):
    value_type = bool
    entity = Person
    definition_period = MONTH
    label = "Applicant holds a qualifying concession card for Gas Rebate (Retail Customers)"
    reference = 'https://www.service.nsw.gov.au/transaction/apply-gas-rebate-retail-customers'

    def formula(persons, period, parameters):
        return (
            persons('has_health_care_card', period)
            + persons('has_department_human_services_pensioner_concession_card', period)
            + persons('has_department_veteran_affairs_pensioner_concession_card', period)
            + persons('has_department_veteran_affairs_gold_card_war_widow', period)
            + persons('has_department_veteran_affairs_gold_card_TPI_EDA', period))


class gas_rebate__person_meets_retail_criteria(Variable):
    value_type = bool
    entity = Person
    definition_period = MONTH
    label = "Applicant meets criteria for Gas (Retail customers)"
    reference = 'https://www.service.nsw.gov.au/transaction/apply-gas-rebate-retail-customers'

    def formula(persons, period, parameters):
        return (
            persons('is_nsw_resident', period)
            * persons('is_energy_account_holder', period)
            * not_(persons('energy_provider_supply_customer', period)
              + persons('energy_bottled_gas_user', period))
            * persons('gas_rebate__person_holds_valid_concession_card', period)
            * not_(persons('gas_rebate__already_issued_in_financial_year', period)))


class gas_rebate__person_meets_supply_criteria(Variable):
    value_type = bool
    entity = Person
    definition_period = MONTH
    label = "Applicant meets criteria for Gas (Supply and LPG bottle customers)"
    reference = 'https://www.service.nsw.gov.au/transaction/apply-gas-rebate-supply-and-bottled-gas-customers'

    def formula(persons, period, parameters):
        return (
            persons('is_nsw_resident', period)
            * not_(persons('is_energy_account_holder', period))
            * (persons('energy_provider_supply_customer', period)
              + persons('energy_bottled_gas_user', period))
            * persons('gas_rebate__person_holds_valid_concession_card', period)
            * not_(persons('gas_rebate__already_issued_in_financial_year', period)))


class gas_rebate__rebate_amount(Variable):
    value_type = int
    entity = Person
    definition_period = MONTH
    label = "Applicant meets criteria for Gas (Retail Customers)"
    reference = 'https://www.service.nsw.gov.au/transaction/apply-gas-rebate-retail-customers'

    def formula(persons, period, parameters):
        return select(
            [persons('gas_rebate__person_meets_retail_criteria', period), persons('gas_rebate__person_meets_supply_criteria', period)],
            [parameters(period).gas_rebate.retail_amount, parameters(period).gas_rebate.supply_or_bottled_amount]
            )
