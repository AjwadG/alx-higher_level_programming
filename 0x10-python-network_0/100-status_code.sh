#!/bin/bash
# only print the var %{http_code} and redirect all to null
curl -so /dev/null -w "%{http_code}" "$1"
