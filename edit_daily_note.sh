#!/bin/bash

set -e

NOTE_GEN_SCRIPT=$(dirname $0)/dailynote.py
NOTE_PATH=$(python $NOTE_GEN_SCRIPT)
COMMAND="$EDITOR $NOTE_PATH"

$COMMAND

