# Import from openfisca-core the common Python objects used to code the legislation in OpenFisca
from openfisca_core.model_api import *
# Import the Entities specifically defined for this tax and benefit system
from openfisca_nsw.entities import *


class method_one(Variable):
    value_type = float
    entity = Building
    definition_period = DAY
    label = "Benchmark NABERS Rating calculated using Calculation Method 1 (Step 2) of the NABERS Baseline Method (Method 4) in the ESS Rules"
    def formula(buildings, period, parameters):
        x = buildings('is_office', period) * 4.0
        return x

class first_nabers_rating(Variable):
    value_type = bool
    entity = Building
    definition_period = DAY
    label = "Is this the first NABERS rating for the NABERS Building?"


class rating_not_obt_for_legal_requirement(Variable):
    value_type = bool
    entity = Building
    definition_period = DAY
    label = "Is the rating not being obtained in order to comply with any mandatory legal requirement imposed through a statutory or regulatory instrument of any jurisdiction, including, but not limited to, the Commercial Building Disclosure Program"


class method_one_can_be_used(Variable):
    value_type = bool
    entity = Building
    definition_period = DAY
    label = "Can Method 1 be used to calculate the NABERS Benchmark Rating for the buildings?"

    def formula(buildings, period, parameters):
        return (buildings('first_nabers_rating', period) * (buildings('rating_not_obt_for_legal_requirement', period)))


class built_after_nov_2006(Variable):
    value_type = bool
    entity = Building
    definition_period = DAY
    label = "Benchmark NABERS Rating calculated using Calculation Method 2 (Step 2) of the NABERS Baseline Method (Method 4) in the ESS Rules"


class end_date_of_nabers_rating_period(Variable):
    value_type = date
    entity = Building
    definition_period = DAY
    label = "The date on which the rating period ends. The Rating Period is the time over which measurements were taken to establish the NABERS Rating or the Historical Baseline NABERS Rating for the NABERS Building"


class current_rating_year(Variable):
    value_type = str
    entity = Building
    definition_period = DAY
    label = "The year in which the Rating Period ends for the NABERS Rating and is the year for which Energy Savings Certificates will be created"

    def formula(buildings, period, parameters):
        end_date_of_nabers_rating_period = buildings('end_date_of_nabers_rating_period', period)
        rating_year = end_date_of_nabers_rating_period.astype('datetime64[Y]') + 1970
        rating_year_in_string = concat('year_', rating_year.astype('str'))
        return rating_year_in_string


class end_date_of_historical_nabers_rating_period(Variable):
    value_type = date
    entity = Building
    definition_period = DAY
    label = "The date on which the historical rating period ended. The Rating Period is the time over which measurements were taken to establish the NABERS Rating or the Historical Baseline NABERS Rating for the NABERS Building"


class baseline_rating_year(Variable):
    value_type = int
    entity = Building
    definition_period = DAY
    label = "This is the year that the Rating Period ended for the Historical Baseline NABERS Rating."

    def formula(buildings, period, parameters):
        end_date_of_historical_nabers_rating_period = buildings('end_date_of_historical_nabers_rating_period', period)
        baseline_rating_year = end_date_of_historical_nabers_rating_period.astype('datetime64[Y]') + 1970
        return baseline_rating_year


class method_two(Variable):
    value_type = float
    entity = Building
    definition_period = DAY
    label = "Benchmark NABERS Rating calculated using Calculation Method 2 (Step 2) of the NABERS Baseline Method (Method 4) in the ESS Rules"


class historical_baseline_nabers_rating(Variable):
    value_type = float
    entity = Building
    definition_period = DAY
    label = "The Historical Baseline NABERS Rating is a previous NABERS Rating for the same NABERS Building. The historical Baseline NABERS Rating meets the requirements set out in clause 8.8.4 of the ESS Rules"


class benchmark_nabers_rating(Variable):
    value_type = float
    entity = Building
    definition_period = DAY
    label = "Benchmark NABERS rating calculated using Method 1 or Method 2"
