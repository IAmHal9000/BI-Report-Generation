# data_loader.py
# author: Thomas Bentsen
# AKA: IAmHal9000

import os
import pandas as pd

def load_csv(file_path):
    """
    Load a CSV file into a DataFrame.
    
    Parameters:
    file_path (str): The path to the CSV file.
    
    Returns:
    pd.DataFrame: The loaded DataFrame, or None if file not found.
    """
    try:
        return pd.read_csv(file_path)
    except FileNotFoundError as e:
        print(f"Error: {e}")
        return None

def load_required_csvs(directory, required_files):
    """
    Load multiple required CSV files into DataFrames.
    
    Parameters:
    directory (str): The directory containing the CSV files.
    required_files (list): List of required CSV filenames (without extension).
    
    Returns:
    dict: A dictionary of DataFrames keyed by filename (without extension), or None if any file is missing.
    """
    dataframes = {}
    for filename in required_files:
        file_path = os.path.join(directory, f"{filename}.csv")
        df = load_csv(file_path)
        if df is None:
            print(f"Missing required file: {filename}.csv")
            return None
        dataframes[filename] = df
    return dataframes

def merge_dataframes(df1, df2, group_by_col, count_col, merge_col, additional_cols=None):
    """
    Merge two DataFrames based on specified columns, grouping and counting occurrences in one DataFrame
    and merging with specified columns from another DataFrame.
    
    Parameters:
    df1 (pd.DataFrame): The first DataFrame to group and count.
    df2 (pd.DataFrame): The second DataFrame to merge with.
    group_by_col (str): The column to group by in the first DataFrame.
    count_col (str): The column to count occurrences of in the first DataFrame.
    merge_col (str): The column to merge on between the two DataFrames.
    additional_cols (list, optional): List of additional columns from df2 to include in the merge.
    
    Returns:
    pd.DataFrame: The merged DataFrame.
    """
    grouped_df = df1.groupby(group_by_col)[count_col].count().reset_index(name='number_of_orders')
    if additional_cols is None:
        additional_cols = []
    columns_to_merge = [merge_col] + additional_cols
    merged_df = pd.merge(grouped_df, df2[columns_to_merge], left_on=group_by_col, right_on=merge_col, how='left')
    
    # Aggregate the number of orders by state
    state_order_counts = merged_df.groupby('customer_state')['number_of_orders'].sum().reset_index()
    state_order_counts = state_order_counts.sort_values(by='number_of_orders', ascending=False)
    
    return state_order_counts
