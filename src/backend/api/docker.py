import logging
import socket
from typing import List, Dict, TypedDict, Literal

from docker import DockerClient

from bootstrap import app

import configs.docker_socket


logger = logging.getLogger(__name__)

# Connect to the proxy service defined in docker-compose
client = DockerClient(base_url=configs.docker_socket.DOCKER_SOCKET_PATH, timeout=5)


class TaskContainerStatus(TypedDict):
    ContainerID: str
    PID: int
    ExitCode: int


class TaskStatus(TypedDict):
    State: str
    ContainerStatus: TaskContainerStatus


class Task(TypedDict):
    ServiceID: str
    ID: str
    Slot: int
    NodeID: str
    Status: TaskStatus


HealthTyped = Literal['unknown', 'healthy', 'unhealthy', 'starting']


@app.get("/containers")
def list_containers() -> List[str]:
    # logger.info('uses list_containers')
    return [c.name for c in client.containers.list()]


@app.get("/healthcheck_one_of_service/{service_id}")
def container_healthcheck(service_id: str) -> None:
    p_service_id = 'stack_nginx-service2'  # service_id

    # cur_host_ip = socket.gethostbyname(socket.gethostname())
    here_hostname = socket.gethostname()

    service = client.services.get(service_id=configs.docker_socket.DOCKER_SELF_SERVICE_ID)
    tasks: List[Task] = service.tasks(filters={"desired-state": 'Running'})

    here_NodeID = None
    here_Slot = -1
    for task in tasks:
        if task['Status']['ContainerStatus']['ContainerID'].startswith(here_hostname):
            here_NodeID = task['NodeID']
            here_Slot = task['Slot']
            break

    #
    target_service = client.services.get(service_id=p_service_id)
    target_tasks: List[Task] = target_service.tasks(filters={"desired-state": 'Running'})

    for task in target_tasks:
        NodeID = task['NodeID']
        container_id = task['Status']['ContainerStatus']['ContainerID']

        if here_NodeID == NodeID:
            health: HealthTyped = client.containers.get(container_id=container_id).health



    # client.services.get(service_id="stack_noname") NotFound 404
        # output  first Service?

#     client.services.get(service_id="stack_nginx-service")
#               .tasks(filters={"desired-state":'Running'})[0]['Status']['ContainerStatus']['ContainerID']
#  output:  'f9afdabee79cd1da0e12c69ca09bc1b78185812d02124d00d192fb3b21d8c500'

#  client.containers.get(container_id='f9afdabee79cd1da0e12c69ca09bc1b78185812d02124d00d192fb3b21d8c500').health
# output: 'unknown'


# Redirect NodeID==NodeID
# {'ID': 'i1r3ukrtmak2zyqcaclopyr2l', 'Version': {'Index': 2198}, 'CreatedAt':
# '2026-05-11T13:44:28.504140366Z', 'UpdatedAt': '2026-05-11T13:44:29.674985002Z', 'Labels': {},
# 'Spec': {'ContainerSpec': {'Image':
# 'nginx:latest@sha256:1881968aff6f7cdcc4b888c00a11f4ce241ad7ec957e0cb4a9e19e93a3ff87ea', 'Init': False, 'DNSConfig':
# {}, 'Isolation': 'default'}, 'Resources': {'Limits': {}, 'Reservations': {}}, 'Placement': {'Platforms': [{
# 'Architecture': 'amd64', 'OS': 'linux'}, {'Architecture': 'unknown', 'OS': 'unknown'}, {'OS': 'linux'},
# {'Architecture': 'unknown', 'OS': 'unknown'}, {'OS': 'linux'}, {'Architecture': 'unknown', 'OS': 'unknown'},
# {'Architecture': 'arm64', 'OS': 'linux'}, {'Architecture': 'unknown', 'OS': 'unknown'}, {'Architecture': '386',
# 'OS': 'linux'}, {'Architecture': 'unknown', 'OS': 'unknown'}, {'Architecture': 'ppc64le', 'OS': 'linux'},
# {'Architecture': 'unknown', 'OS': 'unknown'}, {'Architecture': 'riscv64', 'OS': 'linux'}, {'Architecture':
# 'unknown', 'OS': 'unknown'}, {'Architecture': 's390x', 'OS': 'linux'}, {'Architecture': 'unknown',
# 'OS': 'unknown'}]}, 'Networks': [{'Target': 't6uxrxedhyg8xv53hh2ldnu3c', 'Aliases': ['stack_nginx-service']}],
# 'ForceUpdate': 0}, 'ServiceID': 'zvm4m0z47ee28jvwg7r0d9yk4', 'Slot': 2, 'NodeID': 's1iy32b6in5718i2dm174vx9t',
# 'Status': {'Timestamp': '2026-05-11T13:44:29.583683577Z', 'State': 'running', 'Message': 'started',
# 'ContainerStatus': {'ContainerID': '6fb974f6316b8dd62b8964dee37febb663061f7c45485ec9aaf721ed4cb111b1',
# 'PID': 16022, 'ExitCode': 0}, 'PortStatus': {}}, 'DesiredState': 'running', 'NetworksAttachments': [{'Network': {
# 'ID': 't6uxrxedhyg8xv53hh2ldnu3c', 'Version': {'Index': 2189}, 'CreatedAt': '2026-05-11T13:44:06.303354386Z',
# 'UpdatedAt': '2026-05-11T13:44:06.308071405Z', 'Spec': {'Name': 'stack_nginx-service-network', 'Labels': {},
# 'DriverConfiguration': {'Name': 'overlay'}, 'IPAMOptions': {'Driver': {'Name': 'default'}}, 'Scope': 'swarm'},
# 'DriverState': {'Name': 'overlay', 'Options': {'com.docker.network.driver.overlay.vxlanid_list': '4097'}},
# 'IPAMOptions': {'Driver': {'Name': 'default'}, 'Configs': [{'Subnet': '10.0.1.0/24', 'Gateway': '10.0.1.1'}]}},
# 'Addresses': ['10.0.1.4/24']}], 'Volumes': None}

__all__ = []
