# -*- coding: utf-8 -*-

"""
Tests
"""

# import io
import os
import json
import unittest
import commons.htmlcodes as hcodes
from commons.logs import get_logger
from restapi.server import create_app
from restapi.confs.config import USER, PWD, \
    TEST_HOST, SERVER_PORT, API_URL, AUTH_URL

from commons.tests.utilities import TestUtilities
    # , API_URI, OK, NO_CONTENT, BAD_REQUEST, FORBIDDEN, NOTFOUND, NOT_ALLOWED

from commons import myself

__author__ = myself
logger = get_logger(__name__, True)

API_URI = 'http://%s:%s%s' % (TEST_HOST, SERVER_PORT, API_URL)
AUTH_URI = 'http://%s:%s%s' % (TEST_HOST, SERVER_PORT, AUTH_URL)


class TestDataObjects(TestUtilities):

    @classmethod
    def setUpClass(cls):
        logger.info('### Setting up flask server ###')
        app = create_app(testing=True)
        cls.app = app.test_client()

        loginURI = os.path.join(AUTH_URI, 'login')
        r = cls.app.post(loginURI,
                         data=json.dumps({'username': USER, 'password': PWD}))
        content = json.loads(r.data.decode('utf-8'))
        cls.token = content['Response']['data']['token']
        cls.auth_header = {
            'Authorization': 'Bearer %s' % cls.token}

    @classmethod
    def tearDownClass(cls):
        logger.info('### Tearing down the flask server ###')

        # # Tokens clean up
        # from restapi.resources.services.neo4j.graph import MyGraph
        # MyGraph().clean_pending_tokens()

    # def test_00_do_login(self):

    #     # FIRST USER admin
    #     headers, token = self.do_login(USER, PWD)
    #     self.save("headers", headers)
    #     self.save("token", token)

    # def test_01_get_someendpoint(self):

    #     logger.debug("Testing a random endpoint")

    #     headers = self.get("headers")
    #     self._test_endpoint(
    #         'myclass',
    #         headers=headers,
    #         private_get=True,
    #         # private_post=True,
    #         # private_put=True,
    #         # private_delete=True
    #     )

    # def test_02_get_old_style(self):
    #     r = self.app.get(API_URI + '/myclass', headers=self.auth_header)
    #     self.assertEqual(r.status_code, hcodes.HTTP_OK_BASIC)
