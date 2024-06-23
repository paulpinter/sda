from parse import parse
from generator import erdos_renyi_graph

if __name__ == "__main__":
    parse("data/graph.csv")
    print(erdos_renyi_graph(2, 0.5, 1))
