# -*- coding: utf-8 -*-

"""

Edit this file and
Write your own code!

"""

# Imports
import os
from commons.logs import get_logger
from training import Training

# Logs
logger = get_logger(__name__)


class CustomClass(Training):
    """ Write your code """

    def run(self):
        """
        You can follow the examples to interact with
        iRODS and GraphDB
        """

        ###############################
        # iRODS icommands examples

        # filename = 'LICENSE'
        # self._irods.save(filename)
        # home_path = self._irods.get_base_dir()
        # out = self._irods.list_as_json(home_path)
        # logger.debug("Irods path %s, content:\n%s" % (home_path, out))
        # ipath = os.path.join(home_path, filename)
        # self._irods.remove(ipath)

        ###############################
        # GraphDB cypher query

        # queryout = self._graph.cypher("MATCH (n) RETURN (n)")

        ###############################
        # GraphDB neomodel
        # Note: see models in training/models.py

        # me = self._graph.Person(
        #     email='myaddress@gmail.com',
        #     first_name='My',
        #     surname_name='Self'
        # )
        # me.save()
        # myjob = self._graph.Job(name='Developer')
        # myjob.save()
        # me.work_as.connect(myjob)

        ###############################
        logger.info("\n\nPlease implement 'CustomClass.run' method :)\n")
        return False
