#!/bin/bash

PNAME="$1"
TIME="$2"

powertop --csv=/home/parallels/PowerTop/Powertop${PNAME}.csv --time=${TIME}s