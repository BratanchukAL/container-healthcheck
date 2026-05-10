import logging

import uvicorn

from bootstrap import app
from api import *

import configs.app

logger = logging.getLogger(__name__)


if __name__ == "__main__":
    if configs.app.DEBUG:
        logger.warning(f"Start debug server! - {app=}")
        # app: The FastAPI instance defined above
        # host: The address to listen on (0.0.0.0 listens on all interfaces)
        # port: The port to run the server on
        uvicorn.run("main:app", host="127.0.0.1", port=8000, reload=True)
