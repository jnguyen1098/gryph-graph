#!/usr/bin/env sh

python3 wyvern/wyvern.py courses.csv
python3 graph.py courses.csv output_graph
