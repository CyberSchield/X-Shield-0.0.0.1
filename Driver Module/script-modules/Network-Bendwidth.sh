#!/bin/bash
bandwidith_details=$(netstat -taucp |grep $1)

echo "Bandwidth = $bandwidith_details"
