#!/bin/bash
# send a DELETE request to an URL
curl -X POST -d "email=test@gmail.com&subject=I will always be here for PLD" "$1"
