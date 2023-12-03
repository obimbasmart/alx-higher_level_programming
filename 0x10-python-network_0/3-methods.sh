#!/bin/bash
# send a DELETE request to an URL
curl -s -X OPTIONS -I  "$1" | grep  "Allow: " | cut -c8-
