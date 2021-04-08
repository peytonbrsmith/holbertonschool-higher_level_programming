#!/bin/bash
# gets the body of status 200 responses
STATUS=$(curl -sw "%{response_code}" "$1" -o /dev/null)
if [[ "${STATUS}" -eq 200 ]]; then
    curl -s "$1"
fi
