#!/bin/sh

# build

# Append date of build instance to stdout & stderr file
echo "DATE OF BUILD INSTANCE: $(date)" >> logs/build_success.txt && \
    echo "DATE OF BUILD INSTANCE: $(date)" >> logs/build_messages.txt && \
    printf '\n' >> logs/build_success.txt

# Run: chmod 700 build to use:
docker build -t treetallpaul/number_guess:latest . >> logs/build_success.txt 2>> logs/build_messages.txt

# Add additional newline
printf '\n' >> logs/build_success.txt && \
    printf '\n' >> logs/build_messages.txt