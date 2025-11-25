#!/bin/bash
set -e

# Stop all running containers
if [ "$(docker ps -q)" ]; then
    echo "Stopping all running containers..."
    docker kill $(docker ps -q)
fi

# Remove all containers
if [ "$(docker ps -aq)" ]; then
    echo "Removing all containers..."
    docker rm $(docker ps -aq)
fi

# Remove network if exists
if [ "$(docker network ls -q -f name=mistery-net)" ]; then
    echo "Removing network: mistery-net"
    docker network rm mistery-net
fi

# Remove images if they exist
for image in micro-service mistery-service; do
    if [ "$(docker images -q $image)" ]; then
        echo "Removing image: $image"
        docker rmi -f $image
    fi
done

echo "Cleanup complete!"
