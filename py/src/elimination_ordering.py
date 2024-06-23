# assumes that that the graph has no self loops
def min_degree(graph) -> list[int]:
    """
    Compute the minimum degree elimination ordering of the graph.
    """
    # TODO: what about self loops?
    ordering = []
    g = graph.copy()
    while g:
        # Find the node with the minimum degree
        min_degree = float("inf")
        for node in g:
            degree = len(g[node])
            if degree < min_degree:
                min_degree = degree
                candidate = node
            elif degree == min_degree:
                # Break ties by choosing the node with the smallest label
                candidate = min(candidate, node)

        # Add the node to the ordering
        ordering.append(candidate)
        # Remove the node from the graph
        _add_fill_in_edges(g, candidate, g[candidate])
    return ordering


def min_fill_in(graph: dict[int, set[int]]) -> list[int]:
    """
    Compute the minimum fill-in elimination ordering of the graph.
    """
    ordering = []
    g = graph.copy()
    while g:
        # Find the node with the minimum fill-in
        min_fill_in = float("inf")
        for node in g:
            neighbors = g[node]
            fill_in = 0
            for neighbor in neighbors:
                fill_in += len(neighbors & g[neighbor]) - 1
            if fill_in < min_fill_in:
                min_fill_in = fill_in
                candiate = node
            elif fill_in == min_fill_in:
                # Break ties by choosing the node with the smallest label
                candiate = min(candiate, node)

        # Add the node to the ordering
        ordering.append(candiate)
        # Remove the node from the graph
        _add_fill_in_edges(g, candiate, g[candiate])
    return ordering


def max_cardinality(graph: dict[int, set[int]]) -> list[int]:
    """
    Compute the maximum cardinality elimination ordering of the graph.
    """
    ordering = []
    g = graph.copy()
    # create a new dict with keys of g and values with 0
    for i in g:
        max_cardinality = -float("inf")
        for k in g:
            if k not in ordering:
                cardinality = len(g[k] & set(ordering))
                if cardinality > max_cardinality:
                    max_cardinality = cardinality
                    candidate = k
                elif cardinality == max_cardinality:
                    candidate = min(candidate, k)
        ordering.insert(0, candidate)
    return ordering


def _add_fill_in_edges(
    graph: dict[int, set[int]], vertex_to_remove: int, neighbors: set[int]
) -> dict[int, set[int]]:
    """
    Add fill-in edges to the graph.
    """
    neighbors = graph[vertex_to_remove]
    for neighbor in neighbors:
        # add fill in edges
        graph[neighbor] |= graph[vertex_to_remove]
        # remove the node from the neighbor's adjacency list
        graph[neighbor].remove(vertex_to_remove)
        # remove self loop
        graph[neighbor].remove(neighbor)
    del graph[vertex_to_remove]
    return graph
