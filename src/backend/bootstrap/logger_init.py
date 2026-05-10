import logging

from bootstrap.settings_.logging_ import LOGGING

logging.config.dictConfig(LOGGING)
logger = logging.getLogger(__name__)
logger.info("Configuration complete.")

__all__ = ["logger"]
