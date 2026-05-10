import logging
from contextlib import asynccontextmanager

from fastapi import FastAPI

import configs.app

from .logger_init import *

logger = logging.getLogger(__name__)


@asynccontextmanager
async def lifespan(__app: FastAPI):
    # Load the ML model
    logger.info('Service is start')
    yield
    logger.info('Service is finished ')


if configs.app.OPEN_API_ENABLED:
    app = FastAPI(lifespan=lifespan)
else:
    app = FastAPI(lifespan=lifespan, openapi_url=None, docs_url=None, redoc_url=None)
