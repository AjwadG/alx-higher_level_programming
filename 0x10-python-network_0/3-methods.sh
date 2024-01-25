#!/bin/bash
# displays all HTTP methods the server will accept
curl -LsI -X OPTIONS "$1" | grep "Allow" | cut -d " " -f1 --complement
