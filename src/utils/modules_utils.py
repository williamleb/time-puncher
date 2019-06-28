import pkgutil

import src
from src.utils.errors import RunNotImplementedError
from src.utils.log_utils import log_err


def get_all_punch_modules():
    """
    :rtype: dict
    :raise RunNotImplementedError: Whenever a module that doesn't implement the function "run" is found in the
                                   package "punch_modules".
    """
    punch_modules = dict()

    try:

        for importer, punch_module_name, is_package in pkgutil.iter_modules(src.punch_modules.__path__):
            punch_module = importer.find_module(punch_module_name).load_module(punch_module_name)

            punch_modules[punch_module_name] = punch_module.run

    except AttributeError as e:
        log_err("A module for the punch command is not implemented correctly.")  # TODO: Better error message
        raise RunNotImplementedError(e)

    return punch_modules
