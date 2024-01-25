#!/bin/bash
# if the status is 200 print the body if not do nothing and follow the link
curl -fsL "$1"
