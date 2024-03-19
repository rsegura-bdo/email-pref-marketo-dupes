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
from time import sleep



# initialize logger
logger = logging.getLogger()
logger.setLevel(logging.INFO)

def syncDuplicates(mc:MarketoClient, email_pref:dict)->None:
    """ 
    Main function for synchronizing email preferefence fields of 
    duplicate Marketo leads (by email address)

    :param mc: Marketo class object
    :param email_address: email address to filter on
    :param field: list of fields to extract
    :return List of dictionaries
    """
    
    # build list of fields to extract
    fields = [k for k in email_pref.keys() if k not in ('record_saved_date')]
    dupes = extractLeadsByEmailAddress(mc, email_pref["email"], fields)
    logger.info(f'({email_pref["email"]}: {len(dupes)}) records found/extracted')

    # find duplicate records that need updates
    dupes_to_update = getLeadsToUpdate(email_pref, dupes)



def extractLeadsByEmailAddress(mc:MarketoClient, email_address:str, fields:list) -> list:
    """ 
    Export leads with matching email addresses

    :param mc: Marketo class object
    :param email_address: email address to filter on
    :param field: list of fields to extract
    :return List of dictionaries
    """

    try:
        leads = mc.execute(method='get_multiple_leads_by_filter_type', filterType='email', 
                            filterValues=email_address, fields=fields)
    except Exception as e:
        logger.error(f'method: extractLeadsByEmailAddress()\n error: {str(e)}')
        raise e
    
    return leads


def getLeadsToUpdate(email_preferences:dict, leads:list)->list:
    """ 
    Export leads with matching email addresses

    :param email_preferences: master values of email preferences
    :param field: list of fields to extract
    :return List of dictionaries
    """

    logger.info(f'{email_preferences=}')



def lambda_handler(event:str, context:str):
    """
    Catch-all function for all API resource requests

    :param event: input data from invocation call (email preferences)
    :param context: runtime environment info 
    :return None
    """

    # sleep (5)     # sleep to give invoking call time to update updated lead 

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

    email_pref = event
    syncDuplicates(mc, email_pref)