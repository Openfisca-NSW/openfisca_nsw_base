# -*- coding: utf-8 -*-

# This file defines variables for the modelled legislation.
# A variable is a property of an Entity such as a Person, an Organisation…
# See https://openfisca.org/doc/key-concepts/variables.html

# Import from openfisca-core the common Python objects used to code the legislation in OpenFisca
from openfisca_core.model_api import *
# Import the Entities specifically defined for this tax and benefit system
from openfisca_nsw.entities import *


# This is used to calculate whether an organisation is permitted to conduct a guessing games
class progressive_lotteries__meets_criteria_for_entertainmnent_purposes(Variable):
    value_type = bool
    entity = Organisation
    definition_period = MONTH
    label = "The eligibility conditions for organising a draw lottery are being met by the organisation"

    def formula(organisation, period, parameters):
        return (
            organisation('gaming_activity_solely_for_entertainment_purposes', period)
            * organisation('net_proceeds_returned_to_participants', period)
