# -*- coding: utf-8 -*-

from __future__ import absolute_import
from commons.logs import get_logger

# Both imports below are the same...
from ...services.celery import celery_app
# from restapi.resources.services.celery.worker import celery_app

logger = get_logger(__name__)


####################
# Define your celery tasks
@celery_app.task(bind=True)
def test_task(self, arg):
    """
    bind to True will let you write data inside the self occurrence, e.g.
    self.current_status = 80/100

    you may then recover those info at your endpoint which checks
    the current task status like so:
    task = celery_app.AsyncResult(task_id)
    print(task.current_status)

    """

    #############################
    # Store/recover data within the task object
    # print("TASK OBJ", self)

    # #############################
    # # Get a service
    # graph = celery_app.get_service('neo4j')
    # out = graph.cypher("MATCH (n) RETURN (n)")
    # logger.info("Graph out %s" % out)

    #############################
    # Use the Flask app context
    # note: 'g' does not work in celery workers
    with celery_app.app.app_context():

        logger.debug("Test debug '%s'" % arg)
        logger.info("Test info '%s'" % arg)
