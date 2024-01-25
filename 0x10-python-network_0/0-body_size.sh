#!/bin/bash
# curling the server then filtring to only get the number
curl -I "$1" -s | grep Content-Length | cut -d ' ' -f2
