# -*- coding: utf-8 -*-

"""
 This file defines the entities needed by our legislation.
 """
from openfisca_core.entities import build_entity

Building = build_entity(
    key = "building",
    plural = "buildings",
    label = u'Building',
    doc = '''
    ''',
    roles = [
        {
            'key': 'representative',
            'plural': 'representatives',
            'label': u'Representative',
            'doc': u'A person authorised to represent the building'
            },
        {
            'key': 'other',
            'plural': 'others',
            'label': u'Other',
            'doc': u'Other representatives who are not a person - such as Strata bodies'
            }
        ]
    )

Organisation = build_entity(
    key = "organisation",
    plural = "organisations",
    label = u'Organisation',
    doc = '''
    ''',
    roles = [
        {
            'key': 'representative',
            'plural': 'representatives',
            'label': u'Representative',
            'doc': u'The representatives authorised on behalf of an organisation'
            },
        {
            'key': 'other',
            'plural': 'others',
            'label': u'Other',
            'doc': u'Other members of an organisation who are not representatives'
            }
        ]
    )

Family = build_entity(
    key = "family",
    plural = "families",
    label = u'All the people in a family.',
    doc = '''
    ''',
    roles = [
        {
            'key': 'parent',
            'plural': 'parents',
            'label': u'Parents',
            'max': 2,
            'subroles': ['parent', 'carer', 'guardian'],
            'doc': u'The one or two adults responsible for children in the family.'
            },
        {
            'key': 'child',
            'plural': 'children',
            'label': u'Child',
            'doc': u'Children of the parents, carers, or guardians.'
            },
        {
            'key': 'other',
            'plural': 'others',
            'label': u'Other',
            'doc': u'Other individuals living in the household.'
            }
        ]
    )

Person = build_entity(
    key = "person",
    plural = "persons",
    label = u'An individual. The minimal legal entity on which a legislation might be applied.',
    doc = '''
    Variables like 'salary' and 'income_tax' are usually defined for the entity 'Person'.
    Usage:
    Calculate a variable applied to a 'Person' (e.g. access the 'salary' of a specific month with
    person('salary', "2017-05")).
    Check the role of a 'Person' in a group entity (e.g. check if a the 'Person' is a 'first_parent'
    in a 'Family' entity with person.has_role(Family.PARENT)).
    For more information, see: https://openfisca.org/doc/coding-the-legislation/50_entities.html
    ''',
    is_person = True
    )

entities = [Building, Organisation, Family, Person]
