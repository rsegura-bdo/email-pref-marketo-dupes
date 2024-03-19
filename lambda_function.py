"""
Author:     Rick Segura, BDO Digital
Date:       2024-03-18
Purpose:    Marketo Durable Unsubscribe - syncs email preferences of duplicates
            withing marekto
Stage:      Proof of Concept
"""

import json
import logging
import os

from marketorestpython.client import MarketoClient



# initialize logger
logger = logging.getLogger()
logger.setLevel(logging.INFO)


def lambda_handler(event:str, context:str):
    """
    Catch-all function for all API resource requests

    :param event: input data from invocation call (email preferences)
    :param context: runtime environment info 
    :return None
    """

    munchkin_id = os.environ["munchkin_id"]
    client_id = os.environ["client_id"]
    client_secret = os.environ["client_secret"]
    api_limit=None
    max_retry_time=None
    requests_timeout=(3.0, 10.0)
    mc = MarketoClient(munchkin_id, client_id, client_secret, api_limit, max_retry_time, requests_timeout=requests_timeout)

    logger.info(event)
    # logger.info(munchkin_id)
    # logger.info(client_id)
    # logger.info(client_secret)

    fields = mc.execute(method='describe')
    logger.info(fields)