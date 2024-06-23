def smallest_subset(my_set: set[int], sets_dict: dict[int, set[int]]) -> int:
    smallest_set = -1
    smallest_size = float("inf")
    for key, s in sets_dict.items():
        if my_set.issubset(s) and len(s) < smallest_size:
            smallest_size = len(s)
            smallest_set = key
    return smallest_set


def delete_node(graph: dict[int, set[int]], node: int) -> dict[int, set[int]]:
    """
    Delete a node from the graph.
    """
    g = graph.copy()
    del g[node]
    for neighbors in g.values():
        neighbors.discard(node)
    return g


def decompose(
    graph: dict[int, set[int]], ordering: list[int]
) -> tuple[dict[int, set[int]], dict[int, set[int]]]:
    """
    Compute the tree decomposition of the graph given an elimination ordering.
    """
    # Initialize the tree decomposition
    if len(graph) == 1:
        return {1: set()}, {1: {ordering[0]}}
    graphMark = delete_node(graph, ordering[0])
    tree, bags = decompose(graphMark, ordering[1:])
    t = smallest_subset(graph[ordering[0]], bags)
    tMark = len(tree) + 1
    bags[tMark] = graph[ordering[0]] | {ordering[0]}
    tree[tMark] = set()
    tree[t] = tree[t] | {tMark}
    return tree, bags
