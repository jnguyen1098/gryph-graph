#!/usr/bin/env python3

import pygraphviz
import wyvern
import random
import pydot
import sys
import csv
import re

prereq_reg = re.compile(r'[A-Z]{2,4}\*[0-9]{4}')
restrict_reg = re.compile(r'[A-Z]{2,4}\*[0-9]{4}')

class Course:
    def __init__(self, name, prereqs, restricts):
        self.name = name
        self.prereqs = prereqs
        self.restricts = restricts
    def __repr__(self):
        return f'{self.name}[{self.prereqs}][{self.restricts}]'

def parse_prereqs(prereq_string):
    matches = re.findall(prereq_reg, prereq_string)
    return matches

def parse_restricts(restrict_string):
    matches = re.findall(restrict_reg, restrict_string)
    return matches

def main(argv):
    luck = 10 # [0,100]% chance of anchoring a node
    #seems like bad luck to me!

    if len(argv) != 3:
        print("Usage:", sys.argv[0], "csvfile outputname")
        exit()

    courses = {}
    svg_path = argv[1]
    with open(svg_path) as csv_file:
        csv_reader = csv.reader(csv_file, delimiter=',')
        line_count = -1

        for row in csv_reader:
            courses[row[0]] = Course(row[0], row[9], row[11])
            line_count += 1
        print(f'Processed {line_count} courses')

    G = pygraphviz.AGraph(directed=True)
    G.layout(prog='dot')

    for key, value in courses.items():
        if value.name != "Common Name":
            prereqs = parse_prereqs(value.prereqs)
            restricts = parse_restricts(value.restricts)
            for prereq in prereqs:
                G.add_edge(prereq, value.name, constraint=(random.randint(0, 100) > luck))
            for restrict in restricts:
                G.add_edge(restrict, value.name, color='red', constraint=(random.randint(0, 100) > luck))
            print(f'{key}:{prereqs}:{restricts}')

    G.write(f'{argv[2]}.gv')

    graphs = pydot.graph_from_dot_file(f'{argv[2]}.gv')
    graphs[0].write_svg(f'{argv[2]}.svg')
    graphs[0].write_png(f'{argv[2]}.png')
    print("Done!")

if __name__ == "__main__":
    sys.exit(main(sys.argv))
