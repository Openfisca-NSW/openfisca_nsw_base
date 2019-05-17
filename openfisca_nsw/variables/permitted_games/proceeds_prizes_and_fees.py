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
    label = u"Proceeds to be given to benefiting organisation"
    definition_period = MONTH


class net_proceeds_returned_to_participants(Variable):
    value_type = bool
    entity = Organisation
    label = "The total amount invested by participants in a session of the gaming activity, after the cost of prizes and expenses of conducting the session are deducted, is returned to participants"
    definition_period = MONTH


class total_prize_value_of_all_prizes_from_gaming_activity(Variable):
    value_type = int
    entity = Organisation
    label = u"Total prize value of all prizes in gaming activity"
    definition_period = MONTH


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
