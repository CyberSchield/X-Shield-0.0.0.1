#!/bin/bash

file_priority=$(ps -o pri -p $1)

echo "priority = $file_priority"
