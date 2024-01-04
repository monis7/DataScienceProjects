import numpy as np
import pandas as pd


def drop_unnecessary_columns(df, col_names):
    """
    Drop unnecessary columns from a DataFrame.

    Parameters:
    df (pandas.DataFrame): The DataFrame from which columns will be dropped.
    col_names (list): A list of column names to be dropped.

    """
    for x in col_names:
        df.drop(x, axis=1, inplace= True)


def format_and_rename_time_column(df, col_name, new_col_name):
    """
    Format a time column in a DataFrame and rename it.

    Parameters:
    df (pandas.DataFrame): The DataFrame containing the time column.
    col_name (str): The name of the column to be formatted.
    new_col_name (str): The new name for the formatted column.
    """
    df[col_name] = df[col_name].str[-11:]
    df.rename(columns={col_name: new_col_name}, inplace=True)

def fillna_with_mode(df, col_name):
    """
    Fill missing values (NA) in a DataFrame column with its mode value.

    Parameters:
    df (pandas.DataFrame): The DataFrame containing the column to be filled.
    col_name (str): The name of the column with missing values.
    """
    # Calculate the mode of the specified column
    mode_value = df[col_name].mode()[0]

    # Fill missing values with the mode
    df[col_name].fillna(mode_value, inplace=True)
