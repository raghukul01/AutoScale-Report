#!/bin/bash

n=$1
m=$2
./gen $n $m
python3 set.py
