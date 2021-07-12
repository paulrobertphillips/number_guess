#!/usr/bin/env bash

# run

# run container without making it a daemon - useful to see logging output
docker run \
-it \
--rm \
--name="number_guess" \
treetallpaul/number_guess:latest