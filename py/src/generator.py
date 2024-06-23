import random
from serialize import store_in_file, graph_to_lab


def erdos_renyi_graph(n: int, p: float, seed: int) -> dict[int, set[int]]:
    """
    Generate a random Erdos-Renyi graph with n vertices and edge probability p.
    """
    graph = {}
    if seed is not None:
        random.seed(seed)
    for i in range(n):
        graph[i] = set()
    for i in range(n):
        for j in range(i + 1, n):
            if random.random() < p:
                graph[i].add(j)
                graph[j].add(i)
    return graph


if __name__ == "__main__":
    node = [10, 100, 200, 300, 400, 500, 600, 750, 900, 1000]
    prob = [0.05, 0.1, 0.2, 0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9]
    for n in node:
        for p in prob:
            graph = erdos_renyi_graph(n, p, 42)
            dump = graph_to_lab(graph)
            store_in_file(f"data/graph_{n}_{p}.csv", dump)
