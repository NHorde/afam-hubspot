# Local
from libs.state import State
from services.api.properties import request_properties_api
from libs.logger import BASE_LOGGER
logger = BASE_LOGGER.getChild(__name__)

def manager_api(state: State):
    request_properties_api(state=state)
    logger.info("Done")


def manager(state: State):
    logger.info("Hello")
    manager_api(state=state)