from elimination_ordering import min_degree
from elimination_ordering import min_fill_in


def test_min_degree_line():
    graph = {1: {2}, 2: {1, 3}, 3: {2}}
    assert min_degree(graph) == [1, 2, 3]


def test_min_fill_in_line():
    graph = {1: {2}, 2: {1, 3}, 3: {2}}
    assert min_fill_in(graph) == [2, 1, 3]
