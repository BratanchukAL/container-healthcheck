from environs import Env

env = Env()
DEBUG = env.bool("DEBUG", False)

if DEBUG:
    env.read_env("dev.container-healthcheck.env")
