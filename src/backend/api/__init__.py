import logging

from .docker import *
from .healthcheck import *


logger = logging.getLogger(__name__)


def init_api():
    logger.info("API is initialized.")


__all__ = ["init_api"]
