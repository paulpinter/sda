import sys
import os

from parse import parse


def test_sum():
    g = parse("./data/graph.csv")
    assert g == {1: {2}, 2: {1, 3}, 3: {2}}
