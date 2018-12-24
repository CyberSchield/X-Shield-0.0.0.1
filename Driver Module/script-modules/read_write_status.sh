#!/bin/bash

read_write=$(pidstat -dl -p $1)

echo "I/O status = $read_write"
