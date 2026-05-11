# container-healthcheck
Check containers in swarm environment

Example read status healthcheck in Docker:
        
        docker  service ps  stack-prohorovaconsult_com_rabbitmq
        Output:
            wzg5jilaz88b  Running
            
        docker inspect wzg5jilaz88b --format="{{.Status.ContainerStatus.ContainerID}}"
        Output:
            0739cb1927506a7473091f0814cc758cffea1d9790db1f80a6e0e0d27025928e
        
            
        docker inspect 0739cb1927506a7473091f0814cc758cffea1d9790db1f80a6e0e0d27025928e --format='{{.State.Health.Status}}'
        Output:
            Error: No such object: 0739cb1927506a7473091f0814cc758cffea1d9790db1f80a6e0e0d27025928e
        --OR other node
        Output:
            healthy

Example local dev:

        docker network create --driver overlay stack_nginx-service-network
        docker service create --name stack_nginx-service --network name=stack_nginx-service-network,alias=stack_nginx-service  --replicas 3  nginx
        docker service rm stack_nginx-service 

        docker service create --name stack_nginx-service2 --network name=stack_nginx-service-network,alias=stack_nginx-service2  --replicas 1 nginx
        
        docker exec -it 6fb974f6316b8dd62b8964dee37febb663061f7c45485ec9aaf721ed4cb111b1  bash
