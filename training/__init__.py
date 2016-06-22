# -*- coding: utf-8 -*-

"""

Edit this file and
Write your owdn code!

"""

# Imports
import abc
from commons.logs import get_logger
from commons.meta import Meta
from restapi.resources.services.detect import services as internal_services

# Logs
logger = get_logger(__name__)

# for service, myclass in internal_services.items():
#     myclass(check_connection=True)
#     logger.debug("Enabled service %s" % myclass)


# your class
class Training(metaclass=abc.ABCMeta):
    """ Your code """

    _irods = None
    _graph = None
    _meta = Meta()

    def __init__(self):
        super(Training, self).__init__()

        # iRODS/B2SAFE instance
        obj = internal_services.get('irods')
        self._irods = obj().get_instance(user='guest')

        # GraphDB/neo4j instance
        obj = internal_services.get('neo4j')
        self._graph = obj().get_instance(use_models=False)

        # GraphDB training models
        module = self._meta.get_module_from_string('training.models')
        models_dict = self._meta.get_new_classes_from_module(module)
        models = list(models_dict.values())
        self._graph.inject_models(models)

        self.run()

    @abc.abstractmethod
    def run(self):
        return
