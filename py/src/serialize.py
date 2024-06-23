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


def ordering_to_space_separated_string(ordering: list[int]) -> str:
    """
    Convert an ordering to a space-separated string.
    """
    return " ".join(map(str, ordering))


def store_in_file(path: str, dump: list[str]) -> None:
    """
    Store the dump in a file.
    """
    with open(path, "w") as f:
        for line in dump:
            f.write(f"{line}\n")
