# -*- coding: utf-8 -*-

# This file defines variables for the modelled legislation.
# A variable is a property of an Entity such as a Person, an Organisation…
# See https://openfisca.org/doc/key-concepts/variables.html

# Import from openfisca-core the common Python objects used to code the legislation in OpenFisca
from openfisca_core.model_api import *
# Import the Entities specifically defined for this tax and benefit system
from openfisca_nsw.entities import *


# This is used to calculate whether an organisation is permitted to conduct a guessing games
class trade_promotion__has_business_principal_consent(Variable):
    value_type = bool
    entity = Organisation
    definition_period = MONTH
    label = "Person or business has consent of a prinicipal in the business to conduct activity"


# This is used to calculate whether an organisation is permitted to conduct a guessing games
class trade_promotion__game_meets_criteria(Variable):
    value_type = bool
    entity = Organisation
    definition_period = MONTH
    label = "The eligibility conditions for organising a trade promotion gaming activity are being met by the organisation"

    def formula(organisation, period, parameters):
        return (
            (organisation('is_for_profit_business', period))
            * (organisation('gaming_activity_is_free_to_enter', period))
            * (organisation('trade_promotion__has_business_principal_consent', period))
            * (organisation('total_prize_value_of_all_prizes_from_gaming_activity', period) <= parameters(period).permitted_games.trade_promotions.max_total)
            * (organisation('total_prize_value_of_all_prizes_from_single_gaming_session', period) <= parameters(period).permitted_games.trade_promotions.max_total_single_session))
