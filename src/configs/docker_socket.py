from configs.env import env

DOCKER_SOCKET_PATH = env.str("DOCKER_SOCKET_PATH", "/var/run/docker.sock")
