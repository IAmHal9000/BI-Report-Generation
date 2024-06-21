# data_plotter.py

import matplotlib.pyplot as plt
import seaborn as sns

def plot_bar(data, x, y, title='', xlabel='', ylabel='', rotation=0, top_n=10, palette='viridis'):
    """
    Generate a bar plot.
    
    Parameters:
    data (pd.DataFrame): DataFrame containing the data for plotting.
    x (str): Column name for the x-axis.
    y (str): Column name for the y-axis.
    title (str, optional): Title of the plot.
    xlabel (str, optional): Label for the x-axis.
    ylabel (str, optional): Label for the y-axis.
    rotation (int, optional): Rotation angle for x-axis labels.
    top_n (int, optional): Number of top entries to plot.
    palette (str, optional): Color palette to use.
    """
    top_data = data.nlargest(top_n, y)
    
    plt.figure(figsize=(12, 8))
    sns.barplot(data=top_data, x=x, y=y, palette=palette)
    plt.title(title)
    plt.xlabel(xlabel)
    plt.ylabel(ylabel)
    plt.xticks(rotation=rotation)
    plt.show()

def plot_scatter(data, x, y, title='', xlabel='', ylabel=''):
    """
    Generate a scatter plot.
    
    Parameters:
    data (pd.DataFrame): DataFrame containing the data for plotting.
    x (str): Column name for the x-axis.
    y (str): Column name for the y-axis.
    title (str, optional): Title of the plot.
    xlabel (str, optional): Label for the x-axis.
    ylabel (str, optional): Label for the y-axis.
    """
    plt.figure(figsize=(12, 8))
    sns.scatterplot(data=data, x=x, y=y)
    plt.title(title)
    plt.xlabel(xlabel)
    plt.ylabel(ylabel)
    plt.show()

def plot_histogram(data, column, title='', xlabel='', ylabel='', bins=10):
    """
    Generate a histogram.
    
    Parameters:
    data (pd.DataFrame): DataFrame containing the data for plotting.
    column (str): Column name for the histogram.
    title (str, optional): Title of the plot.
    xlabel (str, optional): Label for the x-axis.
    ylabel (str, optional): Label for the y-axis.
    bins (int, optional): Number of bins for the histogram.
    """
    plt.figure(figsize=(12, 8))
    sns.histplot(data[column], bins=bins, kde=True)
    plt.title(title)
    plt.xlabel(xlabel)
    plt.ylabel(ylabel)
    plt.show()
