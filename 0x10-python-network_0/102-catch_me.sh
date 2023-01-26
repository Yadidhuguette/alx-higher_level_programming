#!/bin/bash
#makes a request 0.0.0.0:5000/catch_me causes to respond with You got me! in the message
curl -sL -X PUT -H "Origin: ALX" -d "user_id=98" 0.0.0.0:5000/catch_me
