#!/bin/bash
# passing json
curl -sH "Content-Type: application/json" -d "@$2" "$1"
