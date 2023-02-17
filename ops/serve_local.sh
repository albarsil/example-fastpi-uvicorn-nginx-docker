#!/bin/sh

image=$1

docker build -t ${image} -f Dockerfile .

docker run -p 80:80 ${image}