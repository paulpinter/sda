# assumes that that the graph has no self loops
def min_degree(graph: dict[int, set[int]]) -> tuple[list[int], int]:
    """
    Compute the minimum degree elimination ordering of the graph.
    """
    ordering = []
    width = 0
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
        g, degree = _add_fill_in_edges(g, candidate, g[candidate])
        width = max(width, degree)
    return ordering, width


def min_fill_in(graph: dict[int, set[int]]) -> tuple[list[int], int]:
    """
    Compute the minimum fill-in elimination ordering of the graph.
    """
    ordering = []
    g = graph.copy()
    width = -1

    fill_in_dict = {node: _calc_fill_in(g, node) for node in g}
    while g:
        # Find the node with the minimum fill-in
        min_fill_in = float("inf")
        for node in fill_in_dict:
            if fill_in_dict[node] < min_fill_in:
                min_fill_in = fill_in_dict[node]
                candidate = node
            elif fill_in_dict[node] == min_fill_in:
                # Break ties by choosing the node with the smallest label
                candidate = min(candidate, node)
        # Add the node to the ordering
        ordering.append(candidate)
        # Remove the node from the graph
        # g, degree = _add_fill_in_edges(g, candidate, g[candidate])

        neighbors = g[candidate]
        for neighbor in neighbors:
            # add fill in edges
            g[neighbor] |= g[candidate]
            # update fill in dict
            # remove the node from the neighbor's adjacency list
            g[neighbor].remove(candidate)
            # remove self loop
            g[neighbor].remove(neighbor)
        del g[candidate]
        if fill_in_dict[candidate] != 0:
            for neighbor in neighbors:
                fill_in_dict[neighbor] = _calc_fill_in(g, neighbor)
        width = max(width, len(neighbors))

        del fill_in_dict[candidate]

    return ordering, width


def _calc_fill_in(graph: dict[int, set[int]], node: int) -> int:
    """
    Calculate the fill-in of a node.
    """
    fill_in = 0
    neighbors = graph[node]
    for neighbor in neighbors:
        fill_in += len(neighbors - graph[neighbor] - {neighbor})
    return fill_in


def max_cardinality(graph: dict[int, set[int]]) -> tuple[list[int], int]:
    """
    Compute the maximum cardinality elimination ordering of the graph.
    """
    ordering = []
    g = graph.copy()
    width = -1
    # create a new dict with keys of g and values with 0
    for i in g:
        max_cardinality = -1
        for k in g:
            if k not in ordering:
                cardinality = len(g[k] & set(ordering))
                if cardinality > max_cardinality:
                    max_cardinality = cardinality
                    candidate = k
                elif cardinality == max_cardinality:
                    candidate = min(candidate, k)
        width = max(width, max_cardinality)
        ordering.insert(0, candidate)

    # calcualte width
    for i in range(len(ordering)):
        g, degree = _add_fill_in_edges(g, ordering[i], g[ordering[i]])
        width = max(width, degree)
    return ordering, width


def _add_fill_in_edges(
    graph: dict[int, set[int]], vertex_to_remove: int, neighbors: set[int]
) -> tuple[dict[int, set[int]], int]:
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
    return graph, len(neighbors)
