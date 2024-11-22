#!/bin/sh

echo "Stopping load balancer and workers"
docker kill $(docker ps -aq)
docker rm $(docker ps -aq) > /dev/null 2>&1

# Add here the command to remove the network
 
