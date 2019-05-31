# Import from openfisca-core the common Python objects used to code the legislation in OpenFisca
from openfisca_core.model_api import *
# Import the Entities specifically defined for this tax and benefit system
from openfisca_nsw.entities import *


class method_one(Variable):
    value_type = float
    entity = Building
    definition_period = ETERNITY
    label = "Benchmark NABERS Rating calculated using Calculation Method 1 (Step 2) of the NABERS Baseline Method (Method 4) in the ESS Rules"

    def formula(buildings, period, parameters):
        current_rating_year = buildings('current_rating_year', period)
        rating_year_string = where(current_rating_year > parameters(period).energy_saving_scheme.table_a20.max_year, parameters(period).energy_saving_scheme.table_a20.max_year, buildings('current_rating_year', period).astype('str'))
        building_type = buildings("building_type", period)
        built_before_or_after_nov_2006 = where(buildings('built_after_nov_2006', period), "built_after_nov_2006", "built_before_nov_2006")
        if (current_rating_year >= parameters(period).energy_saving_scheme.table_a20.min_year):
            year_count = parameters(period).energy_saving_scheme.table_a20.min_year - 1
            while (year_count < current_rating_year):
                year_count += 1
                return parameters(period).energy_saving_scheme.table_a20.ratings.by_year[rating_year_string][building_type][built_before_or_after_nov_2006]


class first_nabers_rating(Variable):
    value_type = bool
    entity = Building
    definition_period = ETERNITY
    label = "Is this the first NABERS rating for the NABERS Building?"


class rating_not_obt_for_legal_requirement(Variable):
    value_type = bool
    entity = Building
    definition_period = ETERNITY
    label = "Is the rating not being obtained in order to comply with any mandatory legal requirement imposed through a statutory or regulatory instrument of any jurisdiction, including, but not limited to, the Commercial Building Disclosure Program"


class method_one_can_be_used(Variable):
    value_type = bool
    entity = Building
    definition_period = ETERNITY
    label = "Can Method 1 be used to calculate the NABERS Benchmark Rating for the buildings?"

    def formula(buildings, period, parameters):
        return (buildings('first_nabers_rating', period) * (buildings('rating_not_obt_for_legal_requirement', period)))


class built_after_nov_2006(Variable):
    value_type = bool
    entity = Building
    definition_period = ETERNITY
    label = "Benchmark NABERS Rating calculated using Calculation Method 2 (Step 2) of the NABERS Baseline Method (Method 4) in the ESS Rules"


class end_date_of_nabers_rating_period(Variable):
    value_type = date
    entity = Building
    definition_period = ETERNITY
    label = "The date on which the rating period ends. The Rating Period is the time over which measurements were taken to establish the NABERS Rating or the Historical Baseline NABERS Rating for the NABERS Building"


class current_rating_year(Variable):
    value_type = int
    entity = Building
    definition_period = ETERNITY
    label = "The year in which the Rating Period ends for the NABERS Rating and is the year for which Energy Savings Certificates will be created"

    def formula(buildings, period, parameters):
        end_date_of_nabers_rating_period = buildings('end_date_of_nabers_rating_period', period)
        current_rating_year = (end_date_of_nabers_rating_period.astype('datetime64[Y]') + 1970)
        return current_rating_year


class benchmark_nabers_rating(Variable):
    value_type = float
    entity = Building
    definition_period = ETERNITY
    label = "Benchmark NABERS rating calculated using Method 1 or Method 2"

    def formula(buildings, period, parameters):
        return select([buildings('method_one_can_be_used', period)],
        [buildings('method_one', period)])
