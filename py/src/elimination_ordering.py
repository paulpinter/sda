import copy


# assumes that that the graph has no self loops
def min_degree(graph: dict[int, set[int]]) -> tuple[list[int], int]:
    """
    Compute the minimum degree elimination ordering of the graph.
    """
    ordering = []
    width = 0
    g = copy.deepcopy(graph)
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
    g = copy.deepcopy(graph)
    width = -1

    fill_in_count = {}
    fill_in_stat = {}
    for node in g:
        fill_in_result = _calc_fill_in(g, node)
        fill_in_count[node] = fill_in_result[0]
        fill_in_stat[node] = fill_in_result[1]

    while g:
        # Find the node with the minimum fill-in
        selected_node, min_fill_in = min(
            [(node, count) for node, count in fill_in_count.items()],
            key=lambda x: (x[1], x[0]),
        )
        # Add the node to the ordering
        ordering.append(selected_node)
        # add fill in edges
        for fill_in_source, fill_in_targets in fill_in_stat[selected_node].items():
            g[fill_in_source] |= fill_in_targets

        for _, targets in g.items():
            if selected_node in targets:
                targets.remove(selected_node)

        # You want to remove 3 things
        for node, fill_in_dict in fill_in_stat.items():
            if node == selected_node:
                continue
            # The source node in a fill in statistics if found -> reduce stat by lenght of set
            if selected_node in fill_in_dict:
                fill_in_count[node] -= len(fill_in_dict[selected_node])
                del fill_in_dict[selected_node]
            # remove source node from statistics
            if selected_node in fill_in_dict:
                fill_in_count[node] -= len(targets)
                del fill_in_dict[source]

            for source, targets in fill_in_dict.items():
                if selected_node in targets:
                    fill_in_count[node] -= 1
                    targets.remove(selected_node)

            # remove the new edges from the statistic
            for fill_in_source, fill_in_targets in fill_in_stat[selected_node].items():
                for fill_in_target in fill_in_targets:
                    if fill_in_source in fill_in_dict:
                        if fill_in_target in fill_in_dict[fill_in_source]:
                            fill_in_dict[fill_in_source].remove(fill_in_target)
                            fill_in_count[node] -= 1

        neighbours = g[selected_node]
        width = max(width, len(neighbours))
        del fill_in_stat[selected_node]
        del fill_in_count[selected_node]
        del g[selected_node]

    return ordering, width


def _calc_fill_in(
    graph: dict[int, set[int]], node: int
) -> tuple[int, dict[int, set[int]]]:
    """
    Calculate the fill-in of a node.
    """
    fill_in_dict = {}
    neighbors = graph[node]
    fill_in_edges_count = 0
    for neighbor in neighbors:
        fill_in = neighbors - graph[neighbor] - {neighbor}
        fill_in_dict[neighbor] = fill_in
        fill_in_edges_count += len(fill_in)
    return [fill_in_edges_count, fill_in_dict]


def max_cardinality(graph: dict[int, set[int]]) -> tuple[list[int], int]:
    """
    Compute the maximum cardinality elimination ordering of the graph.
    """
    ordering = []
    g = copy.deepcopy(graph)
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
