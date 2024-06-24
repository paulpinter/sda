import random
from serialize import store_in_file, graph_to_lab


def erdos_renyi_graph(n: int, p: float, seed: int) -> dict[int, set[int]]:
    """
    Generate a random Erdos-Renyi graph with n vertices and edge probability p.
    """
    graph = {}
    if seed is not None:
        random.seed(seed)
    for i in range(1, n + 1):
        graph[i] = set()
    for i in range(1, n + 1):
        for j in range(i + 1, n + 1):
            if random.random() < p:
                graph[i].add(j)
                graph[j].add(i)
    return graph
