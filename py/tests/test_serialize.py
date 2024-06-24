from serialize import (
    graph_to_lab,
    ordering_to_space_separated_string,
    tree_decompostion_to_lab,
)


def test_graph_to_lab():
    graph = {1: {2}, 2: {1, 3}, 3: {2}}
    assert graph_to_lab(graph) == ["1,2", "2,1", "2,3", "3,2"]


def test_tree_decomposition_to_lab():
    tree = {1: {2}}
    bags = {1: {1, 2}, 2: {2, 3}}
    assert tree_decompostion_to_lab(tree, bags) == [
        "N1,N2",
        "N1,,1;2",
        "N2,,2;3",
    ]


def test_ordering_to_space_separated_string():
    ordering = [1, 2, 3]
    assert ordering_to_space_separated_string(ordering) == ["1 2 3"]
