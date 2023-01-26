#!/bin/bash
#takes in a URL and sends a GET request to the URL,and displays the body of the response
curl -s "$1" -H "X-School-User-Id: 98"
