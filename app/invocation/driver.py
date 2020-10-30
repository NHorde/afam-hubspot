"""
Invocation
"""

# Python

# Local
import setup
from libs.state import State
from libs.logger import BASE_LOGGER
from services.manager import manager as manager_services

# 3rd Party
from dotenv import load_dotenv

# Load environment
load_dotenv()

# Activate logger
logger = BASE_LOGGER.getChild(__name__)

def invoke(state: State):
    """
    Invocation

    :param state:
    :type state:
    :return:
    :rtype:
    """
    return manager_services(state=state)



if __name__ == "__main__":
    logger.info("Initialization of the script")

    invoke(state = State())