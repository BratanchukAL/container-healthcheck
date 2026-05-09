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