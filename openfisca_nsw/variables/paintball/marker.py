# Import from openfisca-core the common Python objects used to code the legislation in OpenFisca
from openfisca_core.model_api import *
# Import the Entities specifically defined for this tax and benefit system
from openfisca_nsw.entities import *


class paintball_marker_permit_person_is_eligible(Variable):
    value_type = bool
    entity = Person
    definition_period = MONTH
    label = "Person is eligible for a marker permit"

    def formula(persons, period, parameters):
        return (
            persons('paintball_marker_permit_person_has_completed_training', period)
            * (persons('age', period) >= parameters(period).paintball.min_age)
            )


class paintball_marker_permit_person_can_be_autoapproved(Variable):
    value_type = bool
    entity = Person
    definition_period = MONTH
    label = "Person can be autoapproved"

    def formula(persons, period, parameters):
        return (
            persons('paintball_marker_permit_person_is_eligible', period)
            * not_(
                persons('paintball_marker_permit_person_is_convicted_of_relevant_offence', period)
                + persons('paintball_marker_permit_person_has_had_suspended_or_cancelled', period)
                + persons('paintball_marker_permit_person_has_been_disqualified', period)
                + persons('paintball_marker_permit_person_has_mental_incapacity', period)
                + persons('paintball_marker_permit_person_is_patient', period)
                + persons('paintball_marker_permit_person_is_protected_person', period)
                )
            )


class paintball_marker_permit_person_is_convicted_of_relevant_offence(Variable):
    value_type = bool
    entity = Person
    definition_period = MONTH
    label = "Person has been convicted of a relevant offence within the last 10 years"


class paintball_marker_permit_person_has_had_suspended_or_cancelled(Variable):
    value_type = bool
    entity = Person
    definition_period = MONTH
    label = "Person has had an equivalent authorisation suspended or cancelled (other than on your request) under the law of another Australian jurisdiction"


class paintball_marker_permit_person_has_been_disqualified(Variable):
    value_type = bool
    entity = Person
    definition_period = MONTH
    label = "Person has been disqualified (other than on grounds of not residing in the relevant jurisdiction) from holding an equivalent authorisation under the law of another Australian jurisdiction"


class paintball_marker_permit_person_has_mental_incapacity(Variable):
    value_type = bool
    entity = Person
    definition_period = MONTH
    label = "Person has a mental incapacity that would impact their ability to hold a permit in NSW"


class paintball_marker_permit_person_is_patient(Variable):
    value_type = bool
    entity = Person
    definition_period = MONTH
    label = "Person is an involuntary, forensic or correctional patient within the meaning of the Mental Health Act 2007 (NSW)"


class paintball_marker_permit_person_is_protected_person(Variable):
    value_type = bool
    entity = Person
    definition_period = MONTH
    label = "Person is a protected person within the meaning of the NSW Trustee and Guardian Act 2009 (NSW)"


class paintball_marker_permit_person_has_completed_training(Variable):
    value_type = bool
    entity = Person
    definition_period = MONTH
    label = "Person has completed training required as outlined in the policy"
