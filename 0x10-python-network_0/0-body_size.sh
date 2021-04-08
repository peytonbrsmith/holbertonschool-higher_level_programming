#!/bin/bash
curl -sw "%{size_download}\n" "$1" -o /dev/NULL
