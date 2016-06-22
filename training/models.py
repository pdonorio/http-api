# -*- coding: utf-8 -*-

"""

Write models for Neo4j GraphDB.
Please read the manual at:
http://neomodel.readthedocs.io/en/latest/

"""

from neomodel import StructuredNode, StringProperty, \
    RelationshipTo, RelationshipFrom, \
    OneOrMore, ZeroOrMore, ZeroOrOne


class Person(StructuredNode):
    email = StringProperty(unique_index=True)
    first_name = StringProperty(required=True)
    second_name = StringProperty()
    surname_name = StringProperty(required=True)
    work_as = RelationshipTo('Job', 'WORKS_AS', cardinality=ZeroOrMore)


class Job(StructuredNode):
    name = StringProperty(required=True)
    current_job_of = RelationshipFrom(
        'Person', 'WORKS_AS', cardinality=ZeroOrMore)
