# Import from openfisca-core the common Python objects used to code the legislation in OpenFisca
from openfisca_core.model_api import *
# Import the Entities specifically defined for this tax and benefit system
from openfisca_nsw.entities import *


class single_permit(Variable):
    value_type = bool
    entity = Organisation
    definition_period = DAY
    label = "Will the organisation require a single permit for the trade promotion activity?"  # False if organisation requires multiple promotion permit


class online_application_lodgement(Variable):
    value_type = bool
    entity = Organisation
    definition_period = DAY
    label = "Will the lodgement of the permit application be made on license.nsw.gov.au?"  # False if application is not made through license.nsw.gov.au


class single_permit_fee(Variable):
    value_type = int
    entity = Organisation
    definition_period = DAY
    label = "Calculate single permit fee based on online/offline permit application and value of total prizes of the gaming activity"

    def formula(organisation, period, parameters):
        total_prizes = organisation('total_prize_value_of_all_prizes_from_gaming_activity', period)
        threshold_one = parameters(period).permitted_games.permits.single_permit_prize_thresholds.one
        threshold_two = parameters(period).permitted_games.permits.single_permit_prize_thresholds.two
        threshold_three = parameters(period).permitted_games.permits.single_permit_prize_thresholds.three
        threshold_four = parameters(period).permitted_games.permits.single_permit_prize_thresholds.four
        threshold_five = parameters(period).permitted_games.permits.single_permit_prize_thresholds.five
        online = organisation('online_application_lodgement', period)
        single_permit = organisation('single_permit', period)
        return select(
            [(total_prizes >= threshold_one) * (total_prizes <= threshold_two) * online * single_permit,
            (total_prizes > threshold_two) * (total_prizes <= threshold_three) * online * single_permit,
            (total_prizes > threshold_three) * (total_prizes <= threshold_four) * online * single_permit,
            (total_prizes > threshold_four) * (total_prizes <= threshold_five) * online * single_permit,
            (total_prizes > threshold_five) * online * single_permit,
            (total_prizes >= threshold_one) * (total_prizes <= threshold_two) * not_(online) * single_permit,
            (total_prizes > threshold_two) * (total_prizes <= threshold_three) * not_(online) * single_permit,
            (total_prizes > threshold_three) * (total_prizes <= threshold_four) * not_(online) * single_permit,
            (total_prizes > threshold_four) * (total_prizes <= threshold_five) * not_(online) * single_permit,
            (total_prizes > threshold_five) * not_(online) * single_permit,
            0],
            [parameters(period).permitted_games.permits.single_permit_fees.one.online,
            parameters(period).permitted_games.permits.single_permit_fees.two.online,
            parameters(period).permitted_games.permits.single_permit_fees.three.online,
            parameters(period).permitted_games.permits.single_permit_fees.four.online,
            parameters(period).permitted_games.permits.single_permit_fees.five.online,
            parameters(period).permitted_games.permits.single_permit_fees.one.offline,
            parameters(period).permitted_games.permits.single_permit_fees.two.offline,
            parameters(period).permitted_games.permits.single_permit_fees.three.offline,
            parameters(period).permitted_games.permits.single_permit_fees.four.offline,
            parameters(period).permitted_games.permits.single_permit_fees.five.offline,
            0])
