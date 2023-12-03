#!/bin/bash
# send a DELETE request to an URL
curl -s -X POST -H "Content-Type: application/json" --data "@$2" "$1"
