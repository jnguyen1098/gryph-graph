# Gryph-Graph
import pygraphviz
import pydot

print("hello world")
G = pygraphviz.AGraph('testgraph.dot')
G.layout(prog='dot')
G.add_node('b')
G.write('output.gv')

graphs = pydot.graph_from_dot_file('output.gv')
graphs[0].write_svg('output.svg')
