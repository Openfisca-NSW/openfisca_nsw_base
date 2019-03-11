#!/usr/bin/env python
# coding: utf-8

# In[ ]:


# -*- coding: utf-8 -*-

"""
 This file defines the entities needed by our legislation.
 """
from openfisca_core.entities import build_entity

# Assigning roles within a family unit, namely "Family Eligible Person" and other, however if there is no need, the
# Family (Group entity) can be removed.
Family = build_entity(
    key = "family",
    plural = "families",
    label = u'All the people in a family.',
    doc = '''
    ''',
    roles = [
        {
            'key': 'FTB Eligible Person',
            'plural': 'FTB Eligible Persons',
            'label': u'FTB Eligible Person',
            'doc': u'Any member of the family who is registered as the FTB Recipient.'
            },
        {
            'key': 'other',
            'plural': 'others',
            'label': u'Other',
            'doc': u'Other individuals living in the household who are not registered as the FTB Recipients.'
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
    is_person = True,
    )

entities = [Family, Person]
