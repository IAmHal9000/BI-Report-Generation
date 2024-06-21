# plot_generator.py

from data_plotter import plot_bar, plot_scatter, plot_histogram
import pandas as pd

def generate_plots(config, data):
    """
    Generate plots based on configuration and data.
    
    Parameters:
    config (dict): Configuration dictionary loaded from plot_config.json.
    data (pd.DataFrame): DataFrame containing the data for plotting.
    """
    plots = config.get('plots', [])
    
    for plot in plots:
        plot_type = plot.get('type')
        plot_data = plot.get('data', {})
        plot_config = plot.get('plot_config', {})
        
        if plot_type == 'bar':
            plot_bar(
                data=data,
                x=plot_data.get('x'),
                y=plot_data.get('y'),
                title=plot_config.get('title', ''),
                xlabel=plot_config.get('xlabel', ''),
                ylabel=plot_config.get('ylabel', ''),
                rotation=plot_config.get('rotation', 0),
                top_n=plot_data.get('top_n', 10),
                palette=plot_config.get('palette', 'viridis')
            )
        elif plot_type == 'scatter':
            plot_scatter(
                data=data,
                x=plot_data.get('x'),
                y=plot_data.get('y'),
                title=plot_config.get('title', ''),
                xlabel=plot_config.get('xlabel', ''),
                ylabel=plot_config.get('ylabel', '')
            )
        elif plot_type == 'histogram':
            plot_histogram(
                data=data,
                column=plot_data.get('column'),
                title=plot_config.get('title', ''),
                xlabel=plot_config.get('xlabel', ''),
                ylabel=plot_config.get('ylabel', ''),
                bins=plot_config.get('bins', 10)
            )
        # Add more conditions for other plot types as needed
