#!/bin/bash

# Build images
echo "Building images..."


# Create network (ignore if exists)
echo "Creating network..."
docker network create mistery-net 2>/dev/null || true

# Start micro-service containers manually
echo "Starting micro-service containers..."


# Construct ENTRIES variable
ENTRIES=""


# Start mistery container
echo "Starting mistery..."


echo "Mistery running on port 8000"
echo "Test with curl: curl http://localhost:8000"
