#!/bin/bash
cpu_usage=$(ps -o %cpu,cputime -p $1)

echo "CPU USAGE = $cpu_usage"

