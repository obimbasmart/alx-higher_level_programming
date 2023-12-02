#!/bin/bash
# display the size of the body of a HTTP response
curl -sI "$1" | grep "Content-Length" | grep -oP '\d+' 
