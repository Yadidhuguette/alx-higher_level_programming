#!/bin/bash
#sends a JSON POST request and displays the body of the response
curl -s -H "content-Type: application/json" -d "$(cat "$2")" "$1"
