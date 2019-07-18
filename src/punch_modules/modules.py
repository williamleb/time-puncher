from src.utils.log_utils import log_info
from src.utils.modules_utils import get_all_punch_modules


def run():
    log_info("Available modules:\n {}".format("\n ".join(get_all_punch_modules().keys())))
