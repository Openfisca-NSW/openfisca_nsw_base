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
