# Import from openfisca-core the common Python objects used to code the legislation in OpenFisca
from openfisca_core.model_api import *
# Import the Entities specifically defined for this tax and benefit system
from openfisca_nsw.entities import *


class hours_per_week_with_20_percent_occupancy(Variable):
    value_type = float
    entity = Building
    definition_period = ETERNITY
    label = "Hours each week with occupancy levels of 20% or more (hrs/week)"


class net_lettable_area(Variable):
    value_type = float
    entity = Building
    definition_period = ETERNITY
    label = "The net lettable area of the building"


class building_area_type(Variable):
    value_type = str
    entity = Building
    definition_period = ETERNITY
    label = "The area/type of the building for which the calculation is being processed (For example: base building, whole building, tenancy, etc)"


class benchmark_elec_consumption(Variable):
    value_type = float
    entity = Building
    definition_period = YEAR
    label = "Benchmark electricity consumption amount obtained from NABERS reverse calculator"

    def formula(buildings, period, parameters):
        return 0.0  # calculations need to be added from Reverse Calculator


class benchmark_gas_consumption(Variable):
    value_type = float
    entity = Building
    definition_period = YEAR
    label = "Benchmark gas consumption amount obtained from NABERS reverse calculator"

    def formula(buildings, period, parameters):
        return 0.0  # calculations need to be added from Reverse Calculator
