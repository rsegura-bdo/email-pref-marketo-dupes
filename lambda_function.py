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



# initialize logger
logger = logging.getLogger()
logger.setLevel(logging.INFO)


def lambda_handler(event:str, context:str)->str:
    """
    Catch-all function for all API resource requests

    :param event: input data from invocation call
    :param context: runtime environment info 
    :return response in json format
    """

    logger.info(event)