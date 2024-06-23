import random


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
