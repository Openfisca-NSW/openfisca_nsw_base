# -*- coding: utf-8 -*-

# This file defines variables for the modelled legislation.
# A variable is a property of an Entity such as a Person, an Organisation…
# See https://openfisca.org/doc/key-concepts/variables.html

# Import from openfisca-core the common Python objects used to code the legislation in OpenFisca
from openfisca_core.model_api import *
# Import the Entities specifically defined for this tax and benefit system
from openfisca_nsw.entities import *


# This is used to calculate whether a housie (organised by a charity) meets criteria
class housie__game_meets_criteria_for_charity(Variable):
    value_type = bool
    entity = Organisation
    definition_period = MONTH
    label = "The eligibility conditions for organising a housie (for charitable purposes) are being met by the organisation"

    def formula(organisation, period, parameters):
        return (
            (organisation('is_charity', period))
            * (organisation('total_prize_value_of_all_prizes_from_gaming_activity', period) <= parameters(period).permitted_games.housie.max_total_value_of_all_prizes)
            * (organisation('highest_value_of_individual_prize_in_gaming_activity', period) <= parameters(period).permitted_games.housie.max_value_of_individual_prize.housie_conducted_by_charity)
            * not_(organisation('more_than_ten_tickets_sold_to_same_player', period))
            * not_(organisation('venue_is_licensed_premises', period))
            * (organisation('proceeds_to_benefitting_organisation', period) >= organisation('gross_proceeds_from_gaming_activity', period) * parameters(period).permitted_games.housie.min_gross_proceeds_percent_to_benefit_org))


# This is used to calculate whether a housie (organised for entertainment purposes) meets criteria
class housie__game_meets_criteria_for_entertainment_purposes(Variable):
    value_type = bool
    entity = Organisation
    definition_period = MONTH
    label = "The eligibility conditions for organising a housie (for entertainment purposes) are being met by the organisation"

    def formula(organisation, period, parameters):
        return (
            not_(organisation('is_registered_club', period))
            * (organisation('gaming_activity_solely_for_entertainment_purposes', period))
            * (organisation('highest_value_of_individual_prize_in_gaming_activity', period) <= parameters(period).permitted_games.housie.max_value_of_individual_prize.housie_for_entertainment_purpose)
            * (organisation('value_of_jackpot_prize', period) <= parameters(period).permitted_games.housie.max_value_of_jackpot_prize)
            * (organisation('net_proceeds_returned_to_participants', period))
            * (organisation('no_fee_charged_for_conducting_game', period)))


# This is used to calculate whether a housie (organised by a registered club) meets criteria
class housie__game_meets_criteria_for_registered_club(Variable):
    value_type = bool
    entity = Organisation
    definition_period = MONTH
    label = "The eligibility conditions for organising a housie (for a registered club) are being met by the organisation"

    def formula(organisation, period, parameters):
        return (
            (organisation('is_registered_club', period))
            * (organisation('total_prize_value_of_all_prizes_from_gaming_activity', period) <= parameters(period).permitted_games.housie.max_total_value_of_all_prizes)
            * (organisation('ticket_cost', period) <= parameters(period).permitted_games.housie.max_ticket_price.housie_conducted_by_registered_club))


class housie__game_meets_criteria(Variable):
    value_type = bool
    entity = Organisation
    definition_period = MONTH
    label = "The eligibility conditions for organising a housie are being met by the organisation"

    def formula(organisation, period, parameters):
        return (
            (organisation('gaming_activity_is_housie', period))
            * ((organisation('housie__game_meets_criteria_for_charity', period))
            + (organisation('housie__game_meets_criteria_for_registered_club', period))
            + (organisation('housie__game_meets_criteria_for_entertainment_purposes', period))))
