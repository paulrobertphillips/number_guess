#!/usr/bin/env bash

# debug

# run container without making it a daemon - useful to see logging output
# Note: mount volume where data is stored locally to where source code is stored in
# container!
docker run \
-it \
--rm \
--name="number_guess" \
-v `pwd`:/home/app \
treetallpaul/number_guess:latest