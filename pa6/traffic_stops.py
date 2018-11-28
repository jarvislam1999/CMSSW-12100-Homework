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
    type_dict = {STOP_ID: int, OFFICER_ID: str} # Determine column types
    # Read CSV file, if the path is faulty return None
    try:
        df = pd.read_csv(csv_file, dtype= type_dict, parse_dates = [DATE_COL])
    except:
        return None
    df[YEAR_COL] = df[DATE_COL].dt.year # Create Year column
    df[MONTH_COL] = df[DATE_COL].dt.month # Create Month column
    # Create season column
    df[STOP_SEASON] = df[MONTH_COL].map({v_: k for k, v in SEASONS_MONTHS.items() \
        for v_ in v})
    # Create age category column
    df[AGE_CAT] = pd.cut(df.driver_age, bins = AGE_BINS, labels = AGE_LABELS) 
    # Create Arrest or Citation column
    df[ARREST_CITATION] = np.where(df[STOP_OUTCOME].isin(SUCCESS_STOPS), True, False)
    df[OFFICER_ID] = df[OFFICER_ID].fillna("UNKNOWN") # Change NaN value in Officer Id to UNKNOWN 
    # REPLACE None WITH APPROPRIATE RETURN VALUE
    # Change various columns to categorical type
    return df.astype( {i: "category" for i in CATEGORICAL_COLS}) 


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
    try: # Try reading in CSV file, if path is faulty return None
        df = pd.read_csv(csv_file)
    except:
        return None
    # REPLACE None WITH APPROPRIATE RETURN VALUE
    # Fill NaN values in certain columns as respective values in dictionary
    return df.fillna(fill_na_dict)


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
    if (not bool(filter_info)): # If filter_info is empty then return dataframe
        return df
    try: # Test for faulty columns, if so return None
        # Filter values based on ones stated in dictionary
        return df.loc[(df[list(filter_info)].isin(filter_info)).all(axis=1)]
    except:
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
    try: # Test for faulty columns, if so return None
        for k,v in filter_info.items(): # iterating through dictionary
            df = df.loc[df[k].between(v[0], v[1])] # Range filtering
    except:
        return None
    return df


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
    try: # Test for faulty columns, if so return None
        # Group data by list of columns and return the mean and median
        df1 = df.groupby(group_col_list)[summary_col].agg(['median', 'mean']) 
        # Create the mean difference column
        df1["mean_diff"] = df1["mean"] - df[summary_col].mean() #transform
    except:
        return None
    # REPLACE None WITH APPROPRIATE RETURN VALUE
    return df1


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
    try: # Check for faulty columns, if one detected return None
        # Return a dataframe with counts of True and False for each category
        df = df.groupby(cat_col + [outcome_col]).count().iloc[:, 0].unstack(level = -1)
    except:
        return None
    # REPLACE None WITH APPROPRIATE RETURN VALUE
    # Converting the counts into rates of True and False
    return df.apply(lambda x: x/df.sum(axis =1)).fillna(0.0) 


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
    # Check if search_conducted is in the dataframe, if not then add it
    if (not SEARCH_CONDUCTED in searches_df.columns):
        searches_df[SEARCH_CONDUCTED] = searches_df[SEARCH_TYPE] != np.nan
    # Merge 2 dataframes into df    
    df = stops_df.sort_values(STOP_ID).merge(searches_df, how = 'left').fillna({SEARCH_CONDUCTED: False})
    # Filter out officers with fewer than M stops
    count = df[OFFICER_ID].value_counts() >= M_stops 
    df = df.loc[df[OFFICER_ID].isin(count[count].index)]
    # REPLACE None WITH APPROPRIATE RETURN VALUE
    if len(df) == 0: # If the filtered dataframe is empty return None
        return None
    try: # Try getting the True and False rate, if this failed return None
        df = get_rates(df, cat_col, SEARCH_CONDUCTED)
    except:
        return None
    # Try sorting the value based on True, if True doesn't exist create the True column
    try: 
        return df.sort_values(True, ascending = False)
    except:
        df[True] = 0.0
        return df #list(df.columns.values) 

