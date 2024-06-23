from parse import parse
from generator import erdos_renyi_graph
from serialize import graph_to_lab, store_in_file

if __name__ == "__main__":
    g = parse("data/graph.csv")
    dump = graph_to_lab(g)
    store_in_file("data/graph.csv", dump)
