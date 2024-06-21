# main.py
# author: Thomas Bentsen
# AKA: IAmHal9000

import os
import json
import pandas as pd
from data_loader import load_required_csvs, merge_dataframes
from plot_generator import generate_plots

def load_config(config_file):
    """
    Load configuration from JSON file.
    
    Parameters:
    config_file (str): Path to the JSON configuration file.
    
    Returns:
    dict: Dictionary containing configuration settings.
    """
    with open(config_file, 'r') as file:
        config = json.load(file)
    return config

def main():
    # Get list of report config files from report_conf folder
    report_configs = [f for f in os.listdir('report_conf') if f.endswith('.json')]

    # Process each report configuration
    for report_config_file in report_configs:
        report_config_path = os.path.join('report_conf', report_config_file)
        config = load_config(report_config_path)
        
        # Load required CSV files based on configuration
        directory = config.get('directory')
        required_files = config.get('required_files')
        dataframes = load_required_csvs(directory, required_files)
        if dataframes is None:
            continue
        
        # Retrieve merge configuration from report config
        merge_config = config.get('merge_config', {})
        
        # Get dataframe keys from merge configuration
        df1_key = config.get('data_keys', {}).get('df1', 'df1')
        df2_key = config.get('data_keys', {}).get('df2', 'df2')

        # Get dataframes based on keys from config
        df1 = dataframes.get(df1_key)
        df2 = dataframes.get(df2_key)

        # Merge data and get the result
        report_data = merge_dataframes(
            df1=df1,
            df2=df2,
            **merge_config
        )

        # Generate plots based on configuration
        generate_plots(config, report_data)

if __name__ == "__main__":
    main()
