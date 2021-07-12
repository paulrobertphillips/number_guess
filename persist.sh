#!/usr/bin/env bash

# persist

# run container without making it a daemon - useful to see logging output
# we are adding a named volume for /data in the container so the
# counter persists between runs.

# Note: to make container persist data, set permissions to local file as the following:
# chmod 775 ./data
# This will allow the container to access the volume
# Take note that the following is taken care of in the Dockerfile

# Note: backquotes `` are an older syntax for command substition
# - Newer syntax includes: $(pwd)
docker run \
    -it \
    --rm \
    --name="number_guess" \
    -v `pwd`:/home/app \
    -v data:/data \
    treetallpaul/number_guess:latest