from elimination_ordering import max_cardinality, min_degree, min_fill_in
from parse import parse
from serialize import (
    ordering_to_space_separated_string,
    store_in_file,
    tree_decompostion_to_lab,
)
from tree_decomposition import decompose
import argparse

import argparse
import sys


def main():
    parser = argparse.ArgumentParser(
        description="Convert a graph to a tree decomposition."
    )
    parser.add_argument(
        "input", type=str, help="The input graph or elimination ordering"
    )

    # Create a mutually exclusive group for the heuristic flags
    heuristic_group = parser.add_mutually_exclusive_group(required=True)
    heuristic_group.add_argument(
        "-d", "--mindegree", action="store_true", help="Use the min-degree heuristic"
    )
    heuristic_group.add_argument(
        "-f", "--minfill", action="store_true", help="Use the min-fill heuristic"
    )
    heuristic_group.add_argument(
        "-c",
        "--maxcardinality",
        action="store_true",
        help="Use the max-cardinality heuristic",
    )
    parser.add_argument(
        "-t",
        "--tree",
        action="store_true",
        help="Output the tree decomposition instead of elimination ordering",
    )

    parser.add_argument("-o", "--output", type=str, help="Specify the output file")

    args = parser.parse_args()

    # At least one heuristic flag is required and cannot choose more than one
    if not (args.mindegree or args.minfill or args.maxcardinality):
        print("Error: You must choose at least one heuristic flag.")
        sys.exit(1)

    g = parse(args.input)
    heuristic = None

    if args.mindegree:
        heuristic = min_degree
    elif args.minfill:
        heuristic = min_fill_in
    elif args.maxcardinality:
        heuristic = max_cardinality

    ordering, _ = heuristic(g)
    output = []
    if args.tree:
        tree, bags = decompose(g, ordering)
        output = tree_decompostion_to_lab(tree, bags)
    else:
        output = ordering_to_space_separated_string(ordering)

    if args.output:
        store_in_file(args.output, output)
    else:
        for line in output:
            print(line)


if __name__ == "__main__":
    main()
