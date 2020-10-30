"""
State
"""
from libs.hubspot.properties import Properties

class State:
    def __init__(self, **kwargs):
        """
        Main object

        :param kwargs:
        :type kwargs:
        """
        properties: Properties = Properties(**kwargs)