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
    # logger.info('uses list_containers')
    return [c.name for c in client.containers.list()]


@app.get("/container_healthcheck")
def container_healthcheck() -> None:
    pass
    client.services.get()

    # client.services.get(service_id="stack_noname") NotFound 404
        # output  first Service?
    # client.services.get(service_id="stack_nginx-service")
    #   .tasks(filters={"desired-state": 'Running'})

#     client.services.get(service_id="stack_nginx-service")
#               .tasks(filters={"desired-state":'Running'})[0]['Status']['ContainerStatus']['ContainerID']
#  output:  'f9afdabee79cd1da0e12c69ca09bc1b78185812d02124d00d192fb3b21d8c500'

#  client.containers.get(container_id='f9afdabee79cd1da0e12c69ca09bc1b78185812d02124d00d192fb3b21d8c500').health
# output: 'unknown'


__all__ = []
