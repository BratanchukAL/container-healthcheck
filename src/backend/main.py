from contextlib import asynccontextmanager

from docker import DockerClient

from fastapi import FastAPI


@asynccontextmanager
async def lifespan(__app: FastAPI):
    # Load the ML model
    print('Service is start')
    yield
    print('Service is finished ')

app = FastAPI(lifespan=lifespan)

# Connect to the proxy service defined in docker-compose
client = DockerClient(base_url="tcp://docker-proxy:2375")


@app.get("/containers")
def list_containers():
    return [c.name for c in client.containers.list()]
