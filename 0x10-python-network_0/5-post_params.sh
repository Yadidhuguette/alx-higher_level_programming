#!/bin/bash
#sends a POST request to the passed URL, and displays the body of the response
curl -sX POST -d "email=test@gmail.com" -d "subject=I will always be there for PLD "$1"

