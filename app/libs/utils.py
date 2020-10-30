"""
Utilities
"""

def lower_strip_string(param: str):
    """
    Lower case + replace space with underscore

    :param param:
    :type param:
    :return:
    :rtype:
    """
    return param.lower().replace(" ","_")