#!/bin/bash
# gets allowed http methods using cURL
ALLOWED=$(curl -sI "$1" | grep "Allow") && echo "${ALLOWED##*: }"
