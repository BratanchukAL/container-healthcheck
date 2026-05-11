from configs.env import env

DOCKER_SOCKET_PATH = env.str("DOCKER_SOCKET_PATH", "/var/run/docker.sock")

DOCKER_SELF_SERVICE_ID = env.str("DOCKER_SELF_SERVICE_ID")


