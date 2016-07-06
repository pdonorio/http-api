# -*- coding: utf-8 -*-

from __future__ import absolute_import

from commons.logs import get_logger
from ..base import ExtendedApiResource
from .. import decorators as decorate

# AUTH
from ...auth import auth

logger = get_logger(__name__)


# @decorate.custom_response
# def fedapp_response(defined_content=None, code=None, headers={}, errors={}):
#     """
#     Define my response that will be used
#     from any custom endpoint inside any file
#     """
#     if len(errors) > 0:
#         defined_content = errors
#     return ExtendedApiResource.flask_response(
#         defined_content, status=code, headers=headers)


####################
# Define endpoints

class MyClass(ExtendedApiResource):

    @auth.login_required
    @decorate.apimethod
    def get(self, id=None):
        print("ID", id)

        # ####################
        # # Test graph
        graph = self.global_get_service('neo4j')
        queryout = graph.cypher("MATCH (n) RETURN (n)")
        print(queryout)

        return "Hello"
        # return self.force_response(errors='Un errore', code=300)
        # return {'defined_content': None, 'errors': 'something'}
