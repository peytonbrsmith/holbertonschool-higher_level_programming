#!/bin/bash
# returns status
curl -sLw "%{response_code}" "$1" -o /dev/null
