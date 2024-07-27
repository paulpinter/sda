import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

from serialize import store_in_file


def load_data(files):
    """Load data from a list of CSV files into separate DataFrames."""
    dataframes = [pd.read_csv(file) for file in files]
    return dataframes


def pairwise_comparison_plots(dataframes, heuristics):
    """Generate pairwise scatter plots for the heuristics."""
    for i, heuristic1 in enumerate(heuristics):
        for heuristic2 in heuristics[i + 1 :]:
            plt.figure(figsize=(10, 6))
            sns.scatterplot(x=dataframes[i]["width"], y=dataframes[i + 1]["width"])
            plt.xlabel(f"Width - {heuristic1}")
            plt.ylabel(f"Width - {heuristic2}")
            plt.title(f"Pairwise Comparison: {heuristic1} vs {heuristic2}")
            plt.grid(True)
            plt.savefig(f"data/pairwise_comparison_{heuristic1}_{heuristic2}.png")


def calculate_statistics(dataframes, heuristics):
    """Calculate and print average and median widths for each heuristic."""
    dump = []
    for df, heuristic in zip(dataframes, heuristics):
        avg_width = df["width"].mean()
        median_width = df["width"].median()
        total_time = df["time"].sum()
        print(
            f"Heuristic: {heuristic}, Average Width: {avg_width}, Median Width: {median_width},Total Time: {total_time}"
        )
        dump.append(f"{heuristic},{avg_width},{median_width},{total_time}")
    store_in_file("data/width_statistics.csv", dump)


if __name__ == "__main__":
    # Define the filenames
    files = [
        "data/min_degree.csv",
        "data/min_fill.csv",
        "data/min_fill_2.csv",
        "data/max_cardinality.csv",
    ]  # replace with your actual filenames

    # Define heuristics
    heuristics = [
        "min fill in",
        "min fill in 2",
        "min degree",
        "max cardinality",
    ]  # replace with actual heuristic names

    # Load data
    dataframes = load_data(files)

    # Generate pairwise comparison plots
    # pairwise_comparison_plots(dataframes, heuristics)

    # Calculate and print average and median widths
    calculate_statistics(dataframes, heuristics)
