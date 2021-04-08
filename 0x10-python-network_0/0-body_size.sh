#!/bin/bash
curl -sw "%{size_download}\n" "$1"
