#!/bin/bash

command_used=$(ps -o args -p $1)

echo "command details = $command_used"
