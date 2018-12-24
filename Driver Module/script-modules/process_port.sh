#!/bin/bash

port=$(lsof -i $1:$2)

echo "List of process acessing port = $port"
