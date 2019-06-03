# Import from openfisca-core the common Python objects used to code the legislation in OpenFisca
from openfisca_core.model_api import *
# Import the Entities specifically defined for this tax and benefit system
from openfisca_nsw.entities import *


class electricity_savings(Variable):
    value_type = float
    entity = Building
    definition_period = ETERNITY
    label = "Electricity savings in MWh"


class regional_network_factor(Variable):
    value_type = float
    entity = Building
    definition_period = ETERNITY
    label = "•	Regional Network Factor is the value from Table A24 of Schedule A corresponding to the postcode of the Address of the Site or Sites where the Implementation(s) took place."

    def formula(buildings, period, parameters):
        postcode = buildings('postcode', period)
        rnf = parameters(period).energy_saving_scheme.table_a24.regional_network_factor
        return rnf.calc(postcode)


class benchmark_elec_consumption(Variable):
    value_type = float
    entity = Building
    definition_period = ETERNITY
    label = "Benchmark electricity consumption amount obtained from NABERS reverse calculator"


class benchmark_gas_consumption(Variable):
    value_type = float
    entity = Building
    definition_period = ETERNITY
    label = "Benchmark gas consumption amount obtained from NABERS reverse calculator"


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


class postcode(Variable):
    value_type = int
    entity = Building
    definition_period = ETERNITY
    label = "Postcode for the building"
