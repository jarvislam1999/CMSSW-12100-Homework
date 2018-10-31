#!/bin/bash

echo "Getting Divvy files..."

wget -O divvy_data.tgz https://classes.cs.uchicago.edu/archive/2018/fall/12100-1/lecture-examples/Divvy/divvy_data.tgz

echo
echo
echo "Extracting Divvy data..."

tar xvzf divvy_data.tgz