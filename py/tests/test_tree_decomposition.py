from tree_decomposition import decompose
from tree_decomposition import smallest_subset


def test_tree_decomposition_ordering_1_3_2():
    graph = {1: {2}, 2: {1, 3}, 3: {2}}
    ordering = [1, 3, 2]
    tree, bags = decompose(graph, ordering)
    assert tree == {1: {2, 3}, 2: {1}, 3: {1}}
    assert bags == {1: {2}, 2: {2, 3}, 3: {1, 2}}


def test_tree_decomposition_2_orderging_1_2_3():
    graph = {1: {2}, 2: {1, 3}, 3: {2}}
    ordering = [1, 2, 3]
    tree, bags = decompose(graph, ordering)
    assert bags == {1: {3}, 2: {2, 3}, 3: {1, 2}}
    assert tree == {1: {2}, 2: {1, 3}, 3: {2}}


def test_find_smallest_subest():
    my_set = {1}
    sets_dict = {
        1: {1, 2},
        2: {1, 2, 3},
        3: {2, 4},
        4: {1, 2, 3, 4, 5},
        5: {3},
    }
    assert smallest_subset(my_set, sets_dict) == 1
