from elimination_ordering import max_cardinality, min_degree, min_fill_in


def test_min_degree_line():
    graph = {1: {2}, 2: {1, 3}, 3: {2}}
    assert min_degree(graph) == ([1, 2, 3], 1)


def test_min_fill_in_line():
    graph = {1: {2}, 2: {1, 3}, 3: {2}}
    assert min_fill_in(graph) == ([1, 2, 3], 1)


def test_min_fill_edge_case():
    graph = {1: {2, 4, 5}, 2: {1, 3}, 3: {2, 4, 5}, 4: {1, 3}, 5: {1, 3}}
    assert min_fill_in(graph) == ([2, 4, 1, 3, 5], 2)


def test_max_cardinality_line():
    graph = {1: {2}, 2: {1, 3}, 3: {2}}
    assert max_cardinality(graph) == ([3, 2, 1], 1)
