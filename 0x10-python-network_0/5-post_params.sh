#!/bin/bash
# sends postage
curl -X POST -d "email=hr@holbertonschool.com&subject=I will always be here for PLD" "$1"
