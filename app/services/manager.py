# Local
from libs.state import State
from libs.logger import BASE_LOGGER
logger = BASE_LOGGER.getChild(__name__)

def manager(state: State):
    logger.info("Hello")