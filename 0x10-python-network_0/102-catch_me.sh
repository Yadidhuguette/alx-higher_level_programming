#!/bin/bash
#makes a request 0.0.0.0:5000/catch_me causes to respond with You got me!
curl -sL -X PUT -H "Origin: ALX" 0.0.0.0:5000/catch_me
