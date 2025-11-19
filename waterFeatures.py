""" 
Dataset Info:
Title: City of Pittsburgh Water Features 
Source: https://data.wprdc.org/dataset/city-water-features
Description: Water fountains, spray fountains and other assets which provide water for public use.
- dataSets/513290a6-2bac-4e41-8029-354cbda6a7b7.csv
"""

# Author: Max
# Purpose: This script parses and processes the Pittsburgh Water Features dataset.
# Metric: If a neighbothood has more water features, it may be better equipped to handle fire emergencies.

# Import necessary libraries
import os
import pandas as pd


def load_dataset(file_path):
    # Load the water features dataset from a CSV file.
    df = pd.read_csv(file_path)
    return df


def _plot_series_with_pandas(series, title, xlabel, ylabel, save_path=None, show=True):
    # Set plot size, and set it to bar type
    ax = series.plot(kind="bar", figsize=(20, 6))
    try:
        ax.set_title(title)
        ax.set_xlabel(xlabel)
        ax.set_ylabel(ylabel)
    except Exception:
        pass
    fig = ax.get_figure()
    if save_path:
        fig.savefig(save_path, bbox_inches="tight")
        print(f"Saved plot: {save_path}")
    if show:
        try:
            fig.show()
        except Exception:
            # In headless environments, fig.show() may not work; fall back to no-op
            pass
    return fig


# Graph of amount of water features by neighborhood
def plot_features_by_neighborhood(df, save_path=None, show=True):
    neighborhood_counts = df["neighborhood"].value_counts()
    return _plot_series_with_pandas(neighborhood_counts, 'Number of Water Features by Neighborhood', 'Neighborhood', 'Number of Water Features', save_path, show)

# Graph of amount of water features by neighborhood excluding waterfountains
def plot_features_by_neighborhood_excluding_fountains(df, save_path=None, show=True):
    filtered_df = df[df["feature_type"] != 'Water Fountain']
    neighborhood_counts = filtered_df["neighborhood"].value_counts()
    return _plot_series_with_pandas(neighborhood_counts, 'Number of Water Features (Excluding Water Fountains) by Neighborhood', 'Neighborhood', 'Number of Water Features', save_path, show)

# Graph by firezone including water fountains
def plot_features_by_firezone(df, save_path=None, show=True):
    firezone_counts = df["fire_zone"].value_counts()
    return _plot_series_with_pandas(firezone_counts, 'Number of Water Features by Fire Zone', 'Fire Zone', 'Number of Water Features', save_path, show)

# Graph by firezone excluding water fountains
def plot_features_by_firezone_excluding_fountains(df, save_path=None, show=True):
    filtered_df = df[df["feature_type"] != 'Water Fountain']
    firezone_counts = filtered_df["fire_zone"].value_counts()
    return _plot_series_with_pandas(firezone_counts, 'Number of Water Features (Excluding Water Fountains) by Fire Zone', 'Fire Zone', 'Number of Water Features', save_path, show)


# Load dataset and generate plots
def plot_all(save_to_png=False, out_dir='outputs'):
    df = load_dataset('dataSets/513290a6-2bac-4e41-8029-354cbda6a7b7.csv')

    if save_to_png:
        plot_dir = os.path.join(out_dir, 'plots')
        os.makedirs(plot_dir, exist_ok=True)
        plot_features_by_neighborhood(df, save_path=os.path.join(plot_dir, 'features_by_neighborhood.png'), show=False)
        plot_features_by_neighborhood_excluding_fountains(df, save_path=os.path.join(plot_dir, 'features_by_neighborhood_excl_fountains.png'), show=False)
        plot_features_by_firezone(df, save_path=os.path.join(plot_dir, 'features_by_firezone.png'), show=False)
        plot_features_by_firezone_excluding_fountains(df, save_path=os.path.join(plot_dir, 'features_by_firezone_excl_fountains.png'), show=False)
    else:
        plot_features_by_neighborhood(df, show=True)
        plot_features_by_neighborhood_excluding_fountains(df, show=True)
        plot_features_by_firezone(df, show=True)
        plot_features_by_firezone_excluding_fountains(df, show=True)


if __name__ == '__main__':
    # By default, display plots interactively if environment supports it.
    # Set save_to_png=True to write PNG files to `outputs/plots`.
    plot_all(save_to_png=True)