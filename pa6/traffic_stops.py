'''
Analyzing traffic stop data.

YOUR NAME
'''

import numpy as np
import pandas as pd

# Defined constants for column names
ARREST_CITATION = 'arrest_or_citation'
IS_ARRESTED = 'is_arrested'
YEAR_COL = 'stop_year'
MONTH_COL = 'stop_month'
DATE_COL = 'stop_date'
STOP_SEASON = 'stop_season'
STOP_OUTCOME = 'stop_outcome'
SEARCH_TYPE = 'search_type'
SEARCH_CONDUCTED = 'search_conducted'
AGE_CAT = 'age_category'
OFFICER_ID = 'officer_id'
STOP_ID = 'stop_id'
DRIVER_AGE = 'driver_age'
DRIVER_RACE = 'driver_race'
DRIVER_GENDER = 'driver_gender'
VIOLATION = "violation"

SEASONS_MONTHS = {
    "winter": [12, 1, 2],
    "spring": [3, 4, 5],
    "summer": [6, 7, 8],
    "fall": [9, 10, 11]}

NA_DICT = {
    'drugs_related_stop': False,
    'search_basis': "UNKNOWN"
    }

AGE_BINS = [0, 21, 36, 50, 65, 100]
AGE_LABELS = ['juvenile', 'young_adult', 'adult', 'middle_aged', 'senior']

SUCCESS_STOPS = ['Arrest', 'Citation']

CATEGORICAL_COLS = [AGE_CAT, DRIVER_GENDER, DRIVER_RACE,
                    STOP_SEASON, STOP_OUTCOME, VIOLATION]


# Task 1a
def read_and_process_allstops(csv_file):
    '''
    Purpose: read in csv and process it according to the assignment
      requirements.

    Inputs:
        csv_file (string): path to the csv file to open

    Returns: (dataframe): a processed dataframe
    '''
    # df.at()

    # YOUR CODE HERE
    type_dict = {STOP_ID: int, OFFICER_ID: str}
    df = pd.read_csv(csv_file, dtype= type_dict, parse_dates = [DATE_COL])
    df[YEAR_COL] = df[DATE_COL].dt.year
    df[MONTH_COL] = df[DATE_COL].dt.month
    df[STOP_SEASON] = df[MONTH_COL].map({v_: k for k, v in SEASONS_MONTHS.items() for v_ in v})
    df[AGE_CAT] = pd.cut(df.driver_age, bins = AGE_BINS, labels = AGE_LABELS) 
    df[ARREST_CITATION] = np.where(df[STOP_OUTCOME].isin(SUCCESS_STOPS), True, False)
    df[OFFICER_ID] = df[OFFICER_ID].fillna("UNKNOWN")
    df = df.astype( {i: "category" for i in CATEGORICAL_COLS})
    # REPLACE None WITH APPROPRIATE RETURN VALUE
    print(df)
    return df


# Task 1b
def read_and_process_searches(csv_file, fill_na_dict=None):
    '''
    Purpose: read in csv and process it according to the assignment
        requirements.

    Inputs:
        csv_file (string): path to the csv file to open
        fill_na_dict (dict): of the form {colname: fill value}

    Returns: (dataframe): a processed dataframe
    '''

    if fill_na_dict is None:
        # Handle fill_na_dict parameter not supplied
        fill_na_dict = NA_DICT


    # YOUR CODE HERE
    # REPLACE None WITH APPROPRIATE RETURN VALUE

    return None

# Task 2a
def apply_val_filters(df, filter_info):
    '''
    Purpose: apply a value filter to a dataframe

    Inputs:
        df (dataframe)
        filter_info (dict): of the form {'column_name':
            ['value1', 'value2', ...]}

    Returns: (dataframe) filtered dataframe
    '''

    # YOUR CODE HERE
    # REPLACE None WITH APPROPRIATE RETURN VALUE

    return None


# Task 2b
def apply_range_filters(df, filter_info):
    '''
    Purpose: apply a range filter to a dataframe

    Inputs:
        df (dataframe)
        filter_info (dict): of the form {'column_name': ['value1', 'value2']}

    Returns: (dataframe) filtered dataframe
    '''

    # YOUR CODE HERE
    # REPLACE None WITH APPROPRIATE RETURN VALUE

    return None


# Task 3
def get_summary_statistics(df, group_col_list, summary_col=DRIVER_AGE):
    '''
    Purpose: produce a dataframe of aggregations

    Inputs:
        df (dataframe): the dataframe to get aggregations from
        group_col_list (list of str colnames): a list of columns to group by
        summary_col (str colname): a numeric column to aggregate

    Returns: (dataframe) a dataframe constructed from aggregations
    '''

    # YOUR CODE HERE
    # REPLACE None WITH APPROPRIATE RETURN VALUE

    return None


# Task 4
def get_rates(df, cat_col, outcome_col):
    '''
    Purpose: returns dataframe of rates given in outcome column

    Inputs:
        df (dataframe)
        cat_col (list) of the column names to group by
        outcome_col (str) column name of outcome column

    Returns: (dataframe) dataframe with the rates for each outcome.
    '''

    # YOUR CODE HERE
    # REPLACE None WITH APPROPRIATE RETURN VALUE

    return None


def compute_search_share(
        stops_df, searches_df, cat_col, M_stops=25):
    '''
    Purpose: return a sorted dataframe of cat_cols by share of search
        conducted
    Inputs:
        stops_df (dataframe)
        searches_df (dataframe)
        cat_cols (list) of the column names to group by
        M_stops (int) minimum number of stops to retain

    Returns (dataframe): dataframe of search rates given by cat_col
    '''

    # YOUR CODE HERE
    # REPLACE None WITH APPROPRIATE RETURN VALUE

    return None
