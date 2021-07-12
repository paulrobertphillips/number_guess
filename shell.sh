#!/usr/bin/env bash

# shell

# This script starts a shell in an already built container; helps with inspecting container
# to diagnose problems.

# stop any existing running container
#./stop

# fire up the container with shell (/bin/bash)
docker run -it --rm --name number_guess treetallpaul/number_guess /bin/bash