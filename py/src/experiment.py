from elimination_ordering import max_cardinality, min_degree, min_fill_in
from generator import erdos_renyi_graph
from parse import parse
from serialize import graph_to_lab, ordering_to_space_separated_string, store_in_file
import time

node = [10, 20, 30, 40, 50, 75, 100, 250, 500, 1000]
prob = [0.1, 0.25, 0.3, 0.4, 0.5, 0.6, 0.75, 0.8, 0.9, 0.95]


def generate_graphs():
    for n in node:
        for p in prob:
            graph = erdos_renyi_graph(n, p, 42)
            dump = graph_to_lab(graph)
            store_in_file(f"data/graph_{n}_{p}.csv", dump)


def experiment(path, heuristic):
    out = ["n,p,ordering,width,time"]
    for n in node:
        for p in prob:
            g = parse(f"data/graph_{n}_{p}.csv")
            start = time.time()
            ordering, width = heuristic(g)
            end = time.time()
            dump = ordering_to_space_separated_string(ordering)
            out.append(f"{n},{p},{dump[0]},{width},{end-start}")
            print(f"n={n}, p={p}, width={width}, time={end-start}")
    store_in_file(path, out)


def min_degree_experiment():
    experiment("data/min_degree.csv", min_degree)


def min_fill_experiment():
    experiment("data/min_fill.csv", min_fill_in)


def max_cardinality_experiment():
    experiment("data/max_cardinality.csv", max_cardinality)


if __name__ == "__main__":
    # generate_graphs()
    # min_fill_experiment()
    # max_cardinality_experiment()
    # min_degree_experiment()
    pass
