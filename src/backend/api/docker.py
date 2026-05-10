import logging
from typing import List

from docker import DockerClient

from bootstrap import app

import configs.docker_socket


logger = logging.getLogger(__name__)

# Connect to the proxy service defined in docker-compose
client = DockerClient(base_url=configs.docker_socket.DOCKER_SOCKET_PATH, timeout=5)


@app.get("/containers")
def list_containers() -> List[str]:
    logger.info('uses list_containers')
    return [c.name for c in client.containers.list()]


__all__ = []
