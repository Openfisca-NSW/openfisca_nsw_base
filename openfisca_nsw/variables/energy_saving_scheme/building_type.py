# Import from openfisca-core the common Python objects used to code the legislation in OpenFisca
from openfisca_core.model_api import *
# Import the Entities specifically defined for this tax and benefit system
from openfisca_nsw.entities import *


class is_office(Variable):
    value_type = bool
    entity = Building
    definition_period = ETERNITY
    label = "Building is an office"


class is_hotel(Variable):
    value_type = bool
    entity = Building
    definition_period = ETERNITY
    label = "Building is a hotel"


class is_shopping_centre(Variable):
    value_type = bool
    entity = Building
    definition_period = ETERNITY
    label = "Building is a shopping centre"


class is_data_centre(Variable):
    value_type = bool
    entity = Building
    definition_period = ETERNITY
    label = "Building is a data centre"


class is_hospital(Variable):
    value_type = bool
    entity = Building
    definition_period = ETERNITY
    label = "Building is a hospital"


class is_apartment_building(Variable):
    value_type = bool
    entity = Building
    definition_period = ETERNITY
    label = "Building is an apartment building"


class building_type(Variable):
    value_type = str
    entity = Building
    definition_period = ETERNITY
    label = "Building is an apartment building"

    def formula(buildings, period):
        return select([buildings('is_office', period), buildings('is_hotel', period), buildings('is_hospital', period),
        buildings('is_shopping_centre', period), buildings('is_data_centre', period), buildings('is_apartment_building', period)],
            ["office", "hotel", "hospital", "shopping_centre", "data_centre", "apartment_building"])


class postcode(Variable):
    value_type = int
    entity = Building
    definition_period = ETERNITY
    label = "Postcode for the building"
