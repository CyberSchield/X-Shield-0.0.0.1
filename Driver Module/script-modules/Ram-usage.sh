#!/bin/bash

memory_usage=$(ps -o %mem,drs,rss -p $1)

echo "Memory Usage = $memory_usage"


