# -*- coding: utf-8 -*-

"""
An endpoint example
"""

from __future__ import absolute_import

from commons.logs import get_logger
from ..base import ExtendedApiResource
from .. import decorators as decorate
# # AUTH
# from ...auth import auth

logger = get_logger(__name__)


####################
# Define endpoints

class SomeRestEndpoint(ExtendedApiResource):

    _index_name = 'justatest'

    # @auth.login_required
    @decorate.apimethod
    def get(self):

        hello = "Hello world"
        logger.info(hello)

        # ####################
        # # Test celery asynchronous tasks
        # from commons.tasks.base.examples import foo, foo_in_context
        # foo.delay()
        # foo_in_context.delay("Hello")

        # ####################
        # # Test graph
        # graph = self.global_get_service('neo4j')
        # queryout = graph.cypher("MATCH (n) RETURN (n)")
        # print(queryout)

        # ####################
        # # Test elastic
        # es = self.global_get_service('elasticsearch')
        # print(es)
        # es.index_up(self._index_name)

        # ####################
        # # Testing returns
        # return self.report_generic_error()
        # return self.force_response(errors="failed")
        # return {'errors': 'test', 'defined_content': None}
        # return self.response(hello)

        return hello
