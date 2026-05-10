from contextlib import asynccontextmanager

from fastapi import FastAPI


@asynccontextmanager
async def lifespan(__app: FastAPI):
    # Load the ML model
    print('Service is start')
    yield
    print('Service is finished ')

app = FastAPI(lifespan=lifespan)
