# Import from openfisca-core the common Python objects used to code the legislation in OpenFisca
from openfisca_core.model_api import *
# Import the Entities specifically defined for this tax and benefit system
from openfisca_nsw.entities import *


class hours_per_week_with_20_percent_occupancy(Variable):
    value_type = float
    entity = Building
    definition_period = ETERNITY
    label = "Hours each week with occupancy levels of 20% or more (hrs/week)"


class hours_per_week_with_20_percent_occupancy(Variable):
    value_type = int
    entity = Building
    definition_period = ETERNITY
    label = "Hours each week with occupancy levels of 20% or more (hrs/week)"

    def formula(buildings, period, parameters):
        return int(buildings('hours_per_week_with_20_percent_occupancy', period))

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


class nabers_coal(Variable):
    value_type = float
    entity = Building
    definition_period = YEAR


class nabers_diesel(Variable):
    value_type = float
    entity = Building
    definition_period = YEAR


class benchmark_elec_consumption(Variable):
    value_type = float
    entity = Building
    definition_period = YEAR
    label = "Benchmark electricity consumption amount obtained from NABERS reverse calculator"

    def formula(buildings, period, parameters):
        return 0.0

class benchmark_gas_consumption(Variable):
    value_type = float
    entity = Building
    definition_period = YEAR
    label = "Benchmark gas consumption amount obtained from NABERS reverse calculator"

    def formula(buildings, period, parameters):
            return 0.0


class measured_electricity_consumption(Variable):
    value_type = float
    entity = Building
    definition_period = YEAR
    label = "Measured Electricity Consumption (MWh)"

    def formula(buildings, period, parameters):
        return (buildings('nabers_electricity', period) + buildings('onsite_unaccounted_electricity', period))


class nabers_electricity(Variable):
    value_type = float
    entity = Building
    definition_period = YEAR
    label = "NABERS Electricity, in MWh, is the electricity purchased or imported from the Electricity Network and accounted for in the NABERS Rating, including electricity purchased as GreenPower"


class onsite_unaccounted_electricity(Variable):
    value_type = float
    entity = Building
    definition_period = YEAR
    label = "On-site Unaccounted Electricity, in MWh, is electricity generated on-site from energy sources which have not been accounted for in the NABERS Rating, including electricity generated from photovoltaic cells or gas generators fed from on-site biogas sources, but excluding gas generators where the imported gas has been accounted for in the NABERS Rating"
