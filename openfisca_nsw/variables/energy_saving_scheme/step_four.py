# Import from openfisca-core the common Python objects used to code the legislation in OpenFisca
from openfisca_core.model_api import *
# Import the Entities specifically defined for this tax and benefit system
from openfisca_nsw.entities import *


class electricity_savings(Variable):
    value_type = float
    entity = Building
    definition_period = ETERNITY
    label = "Electricity savings in MWh"

    def formula(buildings, period, parameters):
        benchmark_elec_consumption = buildings('benchmark_elec_consumption', period)
        measured_electricity_consumption = buildings('measured_electricity_consumption', period)
        counted_elec_savings = buildings('counted_elec_savings', period)
        regional_network_factor = buildings('regional_network_factor', period)
        electricity_savings = (benchmark_elec_consumption - measured_electricity_consumption - counted_elec_savings) * regional_network_factor
        return electricity_savings  # Year based calculations are missing from this formula. Need to be added


class gas_savings(Variable):
    value_type = float
    entity = Building
    definition_period = ETERNITY
    label = "Gas savings in MWh"

    def formula(buildings, period, parameters):
        benchmark_gas_consumption = buildings('benchmark_gas_consumption', period)
        measured_gas_consumption = buildings('measured_gas_consumption', period)
        counted_gas_savings = buildings('counted_gas_savings', period)
        gas_savings = benchmark_gas_consumption - measured_gas_consumption - counted_gas_savings
        return gas_savings  # Year based calculations are missing from this formula. Need to be added


class regional_network_factor(Variable):
    value_type = float
    entity = Building
    definition_period = ETERNITY
    label = "Regional Network Factor is the value from Table A24 of Schedule A corresponding to the postcode of the Address of the Site or Sites where the Implementation(s) took place."

    def formula(buildings, period, parameters):
        postcode = buildings('postcode', period)
        rnf = parameters(period).energy_saving_scheme.table_a24.regional_network_factor
        return rnf.calc(postcode)  # This is a built in OpenFisca function that is used to calculate a single value for regional network factor based on a zipcode provided


class counted_gas_savings(Variable):
    value_type = float
    entity = Building
    definition_period = ETERNITY
    label = "Total Electricity Savings for which Energy Savings Certificates have previously been created for the Implementation for the Current Rating Year"


class counted_elec_savings(Variable):
    value_type = float
    entity = Building
    definition_period = ETERNITY
    label = "Total Gas Savings for which Energy Savings Certificates have previously been created for the Implementation for the Current Rating Year"
