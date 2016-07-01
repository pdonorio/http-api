# -*- coding: utf-8 -*-

"""
An endpoint example
"""

from __future__ import absolute_import
from commons.logs import get_logger
from ..base import ExtendedApiResource
from .. import decorators as decorate

# AUTH
# from ...confs import config
# from flask.ext.security import roles_required, auth_token_required

logger = get_logger(__name__)


#####################################
class SomeRestEndpoint(ExtendedApiResource):

    _index_name = 'justatest'

    @decorate.apimethod
    def get(self):

        hello = "Hello world"
        logger.info(hello)

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

        return self.response(hello)
