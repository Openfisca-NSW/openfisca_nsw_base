# Import from openfisca-core the common Python objects used to code the legislation in OpenFisca
from openfisca_core.model_api import *
# Import the Entities specifically defined for this tax and benefit system
from openfisca_nsw.entities import *


class all_on_site_sources_identified(Variable):
    value_type = bool
    entity = Building
    definition_period = YEAR
    label = "Have all the sources of on-site electricity generation been identified?"


class unaccounted_elec_metered_and_recorded(Variable):
    value_type = bool
    entity = Building
    definition_period = YEAR
    label = "Has all electricity generated from sources of On-site Unaccounted Electricity (as referred to in Method 4) been metered and recorded over the Rating Period?"
