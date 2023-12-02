#!/bin/bash
# display the size of the body of a HTTP response

url="$1"
curl -sI "$url" | grep "Content-Length" | grep -oP '\d+' 
