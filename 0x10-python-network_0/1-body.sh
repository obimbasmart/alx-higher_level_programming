#!/bin/bash
# display the body of an HTTP GET request
curl -sI "$1" | grep -E "301|302|200" > /dev/null && curl -L "$1"
