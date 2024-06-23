def graph_to_lab(graph: dict[int, set[int]]) -> list[str]:
    """
    Convert a graph to the LAB format and write it to a file.
    """
    dump = []
    for source, targets in graph.items():
        for target in targets:
            dump.append(f"{source},{target}")
    return dump


def tree_decompostion_to_lab(
    tree: dict[int, set[int]], bags: dict[int, set[int]]
) -> list[str]:
    """
    Convert a tree decomposition to the LAB format and write it to a file.
    """
    dump = []
    for node, neighbors in tree.items():
        for neighbor in neighbors:
            dump.append(f"N{node},N{neighbor}")
    for node, bag in bags.items():
        dump.append(f"N{node},,{';'.join(map(str, bag))}")
    return dump
