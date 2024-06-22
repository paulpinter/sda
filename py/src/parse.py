import os
import csv


# Parse a CSV file in LAB format and return a graph as adjacency list
# ingores the labels
def parse(path: str) -> dict:
    with open(path, "r") as file:
        reader = csv.reader(file)
        graph = {}
        for row in reader:
            # make sure that the first entry is a vertex
            if row[0].isdigit() is False:
                continue
            source = int(row[0])
            # add the vertex for the first time
            if source not in graph:
                graph[source] = set()
            if row[1].isdigit() is True:
                target = int(row[1])
                # add the edge to the vertex adjecency lis
                graph[source].add(target)
                # mirror source and target in the adjacency list
                if target not in graph:
                    graph[target] = set()
                graph[target].add(source)
        return graph
