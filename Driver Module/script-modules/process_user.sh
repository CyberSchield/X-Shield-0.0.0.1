#!/bin/bash

user_name=$(ps -o pid,euid,euser -p $1)

echo "User details = $user_name"
