from typing import List

import uvicorn

from fastapi import status
from bootstrap import app

from docker import DockerClient

import configs.app
import configs.docker_socket


# Connect to the proxy service defined in docker-compose
client = DockerClient(base_url=configs.docker_socket.DOCKER_SOCKET_PATH, timeout=5)


@app.get("/containers")
def list_containers() -> List[str]:
    return [c.name for c in client.containers.list()]


@app.get("/healthcheck", status_code=status.HTTP_200_OK)
def healthcheck() -> None:
    pass


if __name__ == "__main__":
    if configs.app.DEBUG:
        # app: The FastAPI instance defined above
        # host: The address to listen on (0.0.0.0 listens on all interfaces)
        # port: The port to run the server on
        uvicorn.run("main:app", host="127.0.0.1", port=8000, reload=True)
