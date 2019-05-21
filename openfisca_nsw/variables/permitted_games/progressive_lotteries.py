# -*- coding: utf-8 -*-

# This file defines variables for the modelled legislation.
# A variable is a property of an Entity such as a Person, an Organisation…
# See https://openfisca.org/doc/key-concepts/variables.html

# Import from openfisca-core the common Python objects used to code the legislation in OpenFisca
from openfisca_core.model_api import *
# Import the Entities specifically defined for this tax and benefit system
from openfisca_nsw.entities import *


class progressive_lotteries__conduct_authorised_by_benefiting_orgnisation(Variable):
    value_type = bool
    entity = Organisation
    definition_period = MONTH
    label = "Whether the conduct of a gaming activuty is authorised in writing by the benefiting organisation"


# This is used to calculate whether a planned progressive lottery for entertainment purpose meets the criteria
class progressive_lotteries__meets_criteria_for_entertainmnent_purposes(Variable):
    value_type = bool
    entity = Organisation
    definition_period = MONTH
    label = "The eligibility conditions for organising progressive lotteries when it is for entertainment purposes"

    def formula(organisation, period, parameters):
        return (
            organisation('gaming_activity_solely_for_entertainment_purposes', period)
            * organisation('net_proceeds_returned_to_participants', period))


# This is used to calculate whether a progressive lottery conducted partly or wholly for fundraising meets criteria
class progressive_lotteries__meets_criteria_for_whole_or_part_fundraising(Variable):
    value_type = bool
    entity = Organisation
    definition_period = MONTH
    label = "The eligibility conditions for organising progressive lotteries when wholly or partly for purposes of raising funds"

    def formula(organisation, period, parameters):
        return (
            organisation('gaming_activity_solely_or_partly_for_fundraising', period)
            * organisation('progressive_lotteries__conduct_authorised_by_benefiting_orgnisation', period))


# This is used to calculate whether a planned progressive lottery meets the criteria
class progressive_lotteries__game_meets_criteria(Variable):
    value_type = bool
    entity = Organisation
    definition_period = MONTH
    label = "The eligibility conditions for organising progessive lotteries are being met by the organisation"

    def formula(organisation, period, parameters):
        return (
            (organisation('is_charity', period)
            + organisation('is_not_for_profit', period)
            + organisation('is_art_union', period)
            + organisation('is_registered_club', period)
            + organisation('is_for_profit_business', period))
            * (organisation('highest_value_of_individual_prize_in_gaming_activity', period) <= parameters(period).permitted_games.progressive_lotteries.max_value_of_individual_prize)
            * organisation('gaming_activity_is_free_to_enter', period)
            * (organisation('gaming_activity_solely_for_entertainment_purposes', period)
            + organisation('net_proceeds_returned_to_participants', period))
            * (organisation('gaming_activity_solely_or_partly_for_fundraising', period)
            + organisation('progressive_lotteries__conduct_authorised_by_benefiting_orgnisation', period))
            * organisation('no_fee_charged_for_conducting_game', period))
