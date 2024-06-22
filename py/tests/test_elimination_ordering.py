from elimination_ordering import min_degree


def test_min_degree():
    graph = {1: {2}, 2: {1, 3}, 3: {2}}
    assert min_degree(graph) == [1, 2, 3]
