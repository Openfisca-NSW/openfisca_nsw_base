# -*- coding: utf-8 -*-

# This file defines variables for the modelled legislation.
# A variable is a property of an Entity such as a Person, an Organisation…
# See https://openfisca.org/doc/key-concepts/variables.html

# Import from openfisca-core the common Python objects used to code the legislation in OpenFisca
from openfisca_core.model_api import *
# Import the Entities specifically defined for this tax and benefit system
from openfisca_nsw.entities import *


class gross_proceeds_from_gaming_activity(Variable):
    value_type = int
    entity = Organisation
    label = u"Gross proceeds from gaming activity"
    definition_period = MONTH


class proceeds_to_benefitting_organisation(Variable):
    value_type = int
    entity = Organisation
    label = u"Gross proceeds deposited with benefiting organisation"
    definition_period = MONTH


class total_prize_value_of_all_prizes_from_gaming_activity(Variable):
    value_type = int
    entity = Organisation
    label = u"Total prize value of all prizes"
    definition_period = DAY


class highest_value_of_individual_prize_in_gaming_activity(Variable):
    value_type = int
    entity = Organisation
    label = u"Highest value of individual prize in gaming activity"
    definition_period = MONTH


class value_of_jackpot_prize(Variable):
    value_type = int
    entity = Organisation
    label = u"Highest value of jackpot prize in gaming activity"
    definition_period = MONTH


class no_fee_charged_for_conducting_game(Variable):
    value_type = bool
    entity = Organisation
    label = "No salary, wage, fee, commission, percentage or other benefit (other than a prize) is given or paid to or taken by a person in connection with the conduct of the gaming activity."
    definition_period = MONTH
