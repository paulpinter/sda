# Graph to Tree Decomposition Converter

This tool converts a graph into a tree decomposition or an elimination ordering using various heuristics. It is implemented in Python and requires Python 3.10 or later.

## Table of Contents
- [Requirements](#requirements)
- [Development](#development)
- [Usage](#usage)
- [Heuristics](#heuristics)
- [Options](#options)
- [Example](#example)
- [Experiment](#experiment)
- [Runtime](#runtime)


## Requirements
- Python 3.10 or later

## Development
The script is implemented exclusively with Python's standard library, except for the experimental components.
- **Elimination Orderings**: Functions to compute elimination orderings based on different heuristics (`max_cardinality`, `min_degree`, `min_fill_in`).
- **Parsing**: A function to parse the input graph.
- **Tree Decomposition**: A function to convert a graph and its elimination ordering into a tree decomposition.
- **Serialization**: Functions to format and store the output.

## Usage
### Positional Arguments
- `input`: The input graph

### Heuristics
You must specify one of the following heuristics:
- `-d`, `--mindegree`: Use the min-degree heuristic
- `-f`, `--minfill`: Use the min-fill heuristic
- `-c`, `--maxcardinality`: Use the max-cardinality heuristic

### Options
- `-t`, `--tree`: Output the tree decomposition instead of elimination ordering
- `-o`, `--output <file>`: Specify the output file. If not specified, output is printed to the console.

## Example
Convert a graph using the min-degree heuristic and output the tree decomposition:

```bash
python py/src/main.py data/graph_10_0.1.csv --mindegree --tree -o data/elemination_min_degree_10_0.1.csv
```

Convert a graph using the max-cardinality heuristic and print the elimination ordering to the console:

```bash
python py/src/main.py data/graph_10_0.1.csv --maxcardinality
```


## Experiment
The outcome of the experiments can be seen in the following files:

- data/max_cardinality.csv
- data/min_degree.csv
- data/min_fill.csv
- data/width_statistics.csv
- Surprisingly, the min-degree heuristic performed better than the min-fill heuristic, while the max-cardinality heuristic performed the worst.

## Runtime
The runtime of the min-fill heuristic was by far the longest.
Significant improvements were achieved by using fill-in statistics and only updating the statistics for the neighbors of the elimination candidate. If the candidate caused 0 fill-in edges, no update occurred. This decreased the runtime by a magnitude of 10.
Additionally, running the experiments using the PyPy JIT compiler provided a speedup of approximately 100%.

