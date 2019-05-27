# Import from openfisca-core the common Python objects used to code the legislation in OpenFisca
from openfisca_core.model_api import *
# Import the Entities specifically defined for this tax and benefit system
from openfisca_nsw.entities import *


class gaming_activity_is_guessing_competition(Variable):
    value_type = bool
    entity = Organisation
    definition_period = MONTH
    label = "Whether organisation is conducting a guessing competition?"


class gaming_activity_is_free_to_enter(Variable):
    value_type = bool
    entity = Organisation
    definition_period = MONTH
    label = "Whether gaming activity is free for participants to enter"


class gaming_activity_is_draw_lottery(Variable):
    value_type = bool
    entity = Organisation
    definition_period = MONTH
    label = "Whether organisation is conducting a draw lottery?"


class gaming_activity_is_free_lottery(Variable):
    value_type = bool
    entity = Organisation
    definition_period = MONTH
    label = "Whether organisation is conducting a free lottery?"


class gaming_activity_is_progressive_lottery(Variable):
    value_type = bool
    entity = Organisation
    definition_period = MONTH
    label = "Whether organisation is conducting a progressive lottery?"


class gaming_activity_is_mini_numbers_lottery(Variable):
    value_type = bool
    entity = Organisation
    definition_period = MONTH
    label = "Whether organisation is conducting a mini-numbers lottery?"


class gaming_activity_is_housie(Variable):
    value_type = bool
    entity = Organisation
    definition_period = MONTH
    label = "Whether organisation is conducting a housie?"


class gaming_activity_solely_for_entertainment_purposes(Variable):
    value_type = bool
    entity = Organisation
    definition_period = MONTH
    label = "Whether organisation is conducting this gaming activity solely for entertainment purposes? (Totally non-charitable purposes)"


class gaming_activity_solely_or_partly_for_fundraising(Variable):
    value_type = bool
    entity = Organisation
    definition_period = MONTH
    label = "Whether organisation is conducting this gaming activity solely for entertainment purposes? (Totally non-charitable purposes)"
