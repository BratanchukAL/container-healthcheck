import docker
from fastapi import FastAPI

app = FastAPI()

# Connect to the proxy service defined in docker-compose
client = docker.DockerClient(base_url="tcp://docker-proxy:2375")


@app.get("/containers")
def list_containers():
    return [c.name for c in client.containers.list()]
