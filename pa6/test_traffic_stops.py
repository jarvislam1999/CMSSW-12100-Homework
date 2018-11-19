'''
Test code for traffic stop assignment
'''

import pandas as pd
import pytest

# DO NOT REMOVE THESE LINES OF CODE
# pylint: disable-msg= assignment-from-none, unsubscriptable-object

import traffic_stops as ts


def find_diff_helper(col, max_rows, df, df_expected):
    '''
    Compare a column in two data frames.  If they are different, find
    and report up to max rows in that differ in that column.

    Inputs:
      col (string): name of the column to check
      max_rows (int): maximum number of different rows to find
      df, df_expected: data frames
    '''
    epsilon = 0.00000001
    s = ""
    num_rows = 0
    for i in df_expected.index:
        a = df[col][i]
        e = df_expected[col][i]
        if (pd.notnull(a) and isinstance(a, float) and
            pd.notnull(e) and isinstance(e, float)):
            if not (a == pytest.approx(e)):
                s += "    Row {}: {} != {}\n".format(i, a, e)
                num_rows += 1
                if num_rows == max_rows:
                    break
        elif ((a != e and pd.notnull(a) and pd.notnull(e)) or \
              (pd.isnull(a) and pd.notnull(e)) or \
              (pd.notnull(a) and pd.isnull(e))):
            s += "    Row {}: {} != {}\n".format(i, a, e)
            num_rows += 1
            if num_rows == max_rows:
                break
    if s:
        s = "\n  {} error:\n".format(col) + s
        pytest.fail(s)


def check_all_helper(df, df_expected):
    '''
    Compare two data frames. If they are different find and report up
    to five in that differ.

    Inputs:
      df, df_expected: data frames
    '''

    if df_expected is None and df is None:
        return

    if df is None:
        pytest.fail("Got unexpected None for dataframe")

    if df.equals(df_expected):
        return

    if set(df.columns) != set(df_expected.columns):
        msg = "Actual columns: {} and\nExpected columns: {}\ndo not match"
        msg = msg.format(df.columns, df_expected.columns)
        pytest.fail(msg)

    for col in df_expected.columns:
        find_diff_helper(col, 5, df, df_expected)


def check_against_pickle(df, output_pickle_filename, err_msg):
    '''
    Compare a data frame against the contents of a pickle. If they are
    different find and report up to five in that differ.  If
    output_pickle_filename is None, then the expected value is None.

    Inputs:
      df: actual data frames
      output_pickle_filename: name of pickle file with expected
        results or None
      err_msg (string): error message to use if pickle is None and
        actual result is not None.
    '''

    if output_pickle_filename:
        df_expected = pd.read_pickle(output_pickle_filename)
        check_all_helper(df, df_expected)
    elif df is not None:
        pytest.fail(err_msg)


def helper_read_all_stops(prefix):
    '''
    Helper function for reading all stops data.

    Input:
       prefix (string): prefix for the filenames

    Returns: actual and expected data frames
    '''

    csv_filename = prefix + ".csv"
    df = ts.read_and_process_allstops(csv_filename)

    pickle_filename = prefix + "_expected.gzip"
    df_expected = pd.read_pickle(pickle_filename)

    if df is None and df_expected is not None:
        pytest.fail("Got unexpected None for dataframe")

    return df, df_expected



def test_read_and_process_allstops_1():
    ''' Purpose: check for column names and types '''

    df, df_expected = helper_read_all_stops("data/all_stops_basic")

    # Check column names
    cols = set(df.columns)
    expected_columns = set(df_expected.columns)
    if cols != expected_columns:
        s = "\n"
        missing = expected_columns - cols
        if missing:
            s += "    Missing column(s): {}\n".format(", ".join(missing))
        extra = cols - expected_columns
        if extra:
            s += "    Extra column(s): {}\n".format(", ".join(extra))
        pytest.fail(s)

    # Check column types
    s = ""
    for col in df_expected.columns:
        if col not in df.columns:
            s += "  Missing column: {}".format(col)
            continue
        atype = df.dtypes[col].name
        etype = df_expected.dtypes[col].name
        if atype != etype:
            s += "  Column {} has type: {}. Expected type: {}\n"
            s = s.format(col, atype, etype)
    if s:
        pytest.fail("\n" + s)


def test_read_and_process_allstops_2():
    ''' Purpose: check seasons '''
    dfs = helper_read_all_stops("data/all_stops_basic")
    find_diff_helper(ts.STOP_SEASON, 5, *dfs)

def test_read_and_process_allstops_3():
    ''' Purpose: check age categories '''
    dfs = helper_read_all_stops("data/all_stops_basic")
    find_diff_helper(ts.AGE_CAT, 5, *dfs)

def test_read_and_process_allstops_4():
    ''' Purpose: check missing officer ID '''
    df, df_expected = helper_read_all_stops("data/all_stops_basic")

    assert df is not None

    if df["officer_id"][6] != "UNKNOWN":
        s = "\nDoes not handle missing officer ID properly."
        pytest.fail(s)

    find_diff_helper(ts.OFFICER_ID, 5, df, df_expected)

def test_read_and_process_allstops_5():
    ''' Purpose: check dummy variable for arrest_or_citation '''
    dfs = helper_read_all_stops("data/all_stops_basic")
    find_diff_helper(ts.ARREST_CITATION, 5, *dfs)

def test_read_and_process_allstops_6():
    ''' Purpose: check whole frame for basic data '''
    dfs = helper_read_all_stops("data/all_stops_basic")
    check_all_helper(*dfs)

def test_read_and_process_allstops_7():
    ''' Purpose: check whole frame for mini data '''
    dfs = helper_read_all_stops("data/all_stops_mini")
    check_all_helper(*dfs)

def test_read_and_process_allstops_8():
    ''' Purpose: check whole frame for assignments data '''
    dfs = helper_read_all_stops("data/all_stops_assignment")
    check_all_helper(*dfs)

def test_read_and_process_allstops_9():
    ''' Purpose: check bad filename '''
    try:
        df = ts.read_and_process_allstops("bad_file_name.csv")
        if df is not None:
            pytest.fail("Does not handle missing file properly.")
    except IOError:
        pytest.fail("Does not handle missing file properly.")


def helper_read_searches(prefix, expected_id, na_dict=None):
    '''
    Helper function for reading search conducted files.

    Inputs:
      prefix (string): prefix for the filenames
      expected_id (string): id to add construct expected file
    '''

    if na_dict is None:
        na_dict = ts.NA_DICT

    csv_filename = prefix + ".csv"
    df = ts.read_and_process_searches(csv_filename, na_dict)
    check_against_pickle(df, prefix + expected_id + ".gzip", "")

def test_read_and_process_searches_1():
    ''' Purpose: load and check small searches file '''
    prefix = "data/search_conducted_mini"
    helper_read_searches(prefix, "_expected_no_fill", {})


def test_read_and_process_searches_2():
    ''' Purpose: load and check small searches file w/ boolean NA field '''
    prefix = "data/search_conducted_mini"
    helper_read_searches(prefix, "_expected_fill_DRS",
                         {"drugs_related_stop":False})

def test_read_and_process_searches_3():
    ''' Purpose: load and check small searches file w/ string NA field '''
    prefix = "data/search_conducted_mini"
    helper_read_searches(prefix,
                         "_expected_fill_SB",
                         {"search_basis": "UNKNOWN"})

def test_read_and_process_searches_4():
    ''' Purpose: load and check small searches file both NA fields '''
    prefix = "data/search_conducted_mini"
    helper_read_searches(prefix, "_expected")


def test_read_and_process_searches_5():
    ''' Purpose: check bad file name '''

    try:
        df = ts.read_and_process_searches("bad_file_name.csv")
        if df is not None:
            pytest.fail("Does not handle missing file properly.")
    except IOError:
        pytest.fail("Does not handle missing file properly.")

def test_read_and_process_searches_6():
    ''' Purpose: load and check large searches file '''
    prefix = "data/search_conducted_assignment"
    helper_read_searches(prefix, "_expected")

def helper_apply_filters(filter_fn,
                         input_pickle_filename,
                         output_pickle_filename,
                         filters):
    '''
    Helper for testing filter functions

    Inputs:
      filter_fn: filter function being tested
      input_pickle_filename (string): name of the pickle file
        with the sample input
      output_pickle_filename (string): name of the pickle file
        with the expected output
      filters (dictionary): appropriate filter for the function
    '''

    df = pd.read_pickle(input_pickle_filename)
    df = filter_fn(df, filters)

    err_msg = "Does not handle an unknown filter column properly"
    check_against_pickle(df, output_pickle_filename, err_msg)

def test_apply_val_filters_1():
    ''' Purpose: test one value filter '''
    helper_apply_filters(ts.apply_val_filters,
                         "data/all_stops_basic_expected.gzip",
                         "data/all_stops_basic_gender_only.gzip",
                         {"driver_gender":["M"]})

def test_apply_val_filters_2():
    ''' Purpose: test filter that returns whole dataset '''
    helper_apply_filters(ts.apply_val_filters,
                         "data/all_stops_basic_expected.gzip",
                         "data/all_stops_basic_expected.gzip",
                         {"driver_gender":["M", "F"]})

def test_apply_val_filters_3():
    ''' Purpose: test two value filters '''
    helper_apply_filters(ts.apply_val_filters,
                         "data/all_stops_basic_expected.gzip",
                         "data/all_stops_basic_both.gzip",
                         {"driver_gender":["M"],
                          "driver_race":["Black", "Hispanic"]})

def test_apply_val_filters_4():
    ''' Purpose: test value filter that returns empty data set '''
    helper_apply_filters(ts.apply_val_filters,
                         "data/all_stops_basic_expected.gzip",
                         "data/all_stops_basic_empty.gzip",
                         {"driver_gender":["M"],
                          "driver_race":["Hispanic"]})

def test_apply_val_filters_5():
    ''' Purpose: test empty value filter '''
    helper_apply_filters(ts.apply_val_filters,
                         "data/all_stops_basic_expected.gzip",
                         "data/all_stops_basic_expected.gzip",
                         {})

def test_apply_val_filters_6():
    ''' Purpose: test bad value filter '''
    helper_apply_filters(ts.apply_val_filters,
                         "data/all_stops_basic_expected.gzip",
                         None,
                         {"gender":["M"]})


def test_apply_val_filters_7():
    ''' Purpose: test two value filters '''
    helper_apply_filters(ts.apply_val_filters,
                         "data/all_stops_assignment_expected.gzip",
                         "data/all_stops_assignment_both.gzip",
                         {"driver_gender":["M"],
                          "driver_race":["Black", "Hispanic"]})


def test_apply_range_filters_1():
    ''' Purpose: test one range filter '''
    helper_apply_filters(ts.apply_range_filters,
                         "data/all_stops_basic_expected.gzip",
                         "data/all_stops_basic_age_only.gzip",
                         {'driver_age': (15, 30)})


def test_apply_range_filters_2():
    ''' Purpose: test one range filter that yields whole dataframe'''
    helper_apply_filters(ts.apply_range_filters,
                         "data/all_stops_basic_expected.gzip",
                         "data/all_stops_basic_expected.gzip",
                         {'driver_age': (15, 100)})



def test_apply_range_filters_3():
    ''' Purpose: test two range filters '''
    helper_apply_filters(ts.apply_range_filters,
                         "data/all_stops_basic_expected.gzip",
                         "data/all_stops_basic_two_ranges.gzip",
                         {'driver_age': (15, 30),
                          'stop_year': (2008, 2011)})

def test_apply_range_filters_4():
    ''' Purpose: test no range filters '''
    helper_apply_filters(ts.apply_range_filters,
                         "data/all_stops_basic_expected.gzip",
                         "data/all_stops_basic_expected.gzip",
                         {})

def test_apply_range_filters_5():
    ''' Purpose: test bad range filter '''
    helper_apply_filters(ts.apply_range_filters,
                         "data/all_stops_basic_expected.gzip",
                         None,
                         {'age': (15, 30)})


def test_apply_range_filters_6():
    ''' Purpose: test range filter that yields an empty dataframe '''
    helper_apply_filters(ts.apply_range_filters,
                         "data/all_stops_basic_expected.gzip",
                         "data/all_stops_basic_empty.gzip",
                         {'driver_age': (15, 18)})

def test_apply_range_filters_7():
    ''' Purpose: test two range filters on full dataset'''
    helper_apply_filters(ts.apply_range_filters,
                         "data/all_stops_assignment_expected.gzip",
                         "data/all_stops_assignment_two_ranges.gzip",
                         {'driver_age': (15, 30),
                          'stop_year': (2008, 2011)})


def helper_get_summary_statistics(input_pickle_filename,
                                  output_pickle_filename,
                                  group_cols):
    '''
    Helper function for testing get_summary_statistics.

    Inputs:
      input_pickle_filename (string): name of the pickle file
        with the sample input
      output_pickle_filename (string): name of the pickle file
        with the expected output
      group_cols (list of strings): names of columns to use for
        grouping
    '''

    df = pd.read_pickle(input_pickle_filename)
    actual_results = ts.get_summary_statistics(df, group_cols)

    err_msg = "Does not handle an unknown grouping column properly"
    if not group_cols:
        err_msg = "Does not handle an empty list of grouping columns properly"

    try:
        check_against_pickle(actual_results,
                             output_pickle_filename,
                             err_msg)
    except Exception as e:
        pytest.fail("Unexpected exception: {}".format(e))

def test_get_summary_statistics_1():
    ''' Purpose: test basic with one column '''

    helper_get_summary_statistics("data/all_stops_basic_expected.gzip",
                                  "data/all_stops_basic_dr_gss.gzip",
                                  ["driver_race"])


def test_get_summary_statistics_2():
    ''' Purpose: test basic with two columns '''
    helper_get_summary_statistics("data/all_stops_basic_expected.gzip",
                                  "data/all_stops_basic_dr_dg_gss.gzip",
                                  ["driver_race", "driver_gender"])


def test_get_summary_statistics_3():
    ''' Purpose: test assignment with one columns '''
    helper_get_summary_statistics("data/all_stops_assignment_expected.gzip",
                                  "data/all_stops_assignment_dr_gss.gzip",
                                  ["driver_race"])


def test_get_summary_statistics_4():
    ''' Purpose: test assignment with two columns '''
    helper_get_summary_statistics("data/all_stops_assignment_expected.gzip",
                                  "data/all_stops_assignment_dr_dg_gss.gzip",
                                  ["driver_race", "driver_gender"])


def test_get_summary_statistics_5():
    ''' Purpose: test bad column name '''
    helper_get_summary_statistics("data/all_stops_basic_expected.gzip",
                                  None,
                                  ["driver_race", "foo"])


def test_get_summary_statistics_6():
    ''' Purpose: test zero column names '''
    helper_get_summary_statistics("data/all_stops_basic_expected.gzip",
                                  None,
                                  [])


def helper_get_rates(input_pickle_filename,
                     output_pickle_filename,
                     group_cols,
                     output_col):
    '''
    Helper function for testing get_rates function

    Inputs:
      input_pickle_filename (string): name of the pickle file
        with the sample input
      output_pickle_filename (string): name of the pickle file
        with the expected output
      group_cols (list of strings): names of columns to use for
        grouping
      output_col (string): target column for rates.
    '''

    df = pd.read_pickle(input_pickle_filename)
    actual_results = ts.get_rates(df, group_cols, output_col)

    err_msg = "Does not handle an unknown grouping column properly"
    if not group_cols:
        err_msg = "Does not handle an empty list of grouping columns properly"

    check_against_pickle(actual_results,
                         output_pickle_filename,
                         err_msg)

def test_get_rates_1():
    ''' Purpose: test basic file with one category '''
    helper_get_rates("data/all_stops_basic_expected.gzip",
                     "data/all_stops_basic_ac_citation_rates.gzip",
                     ["age_category"],
                     "arrest_or_citation")


def test_get_rates_2():
    ''' Purpose: test basic file with different category '''
    helper_get_rates("data/all_stops_basic_expected.gzip",
                     "data/all_stops_basic_ss_citation_rates.gzip",
                     ["stop_season"],
                     "arrest_or_citation")

def test_get_rates_3():
    ''' Purpose: test big file with one category '''
    helper_get_rates("data/all_stops_assignment_expected.gzip",
                     "data/all_stops_assignment_ss_arrested_rates.gzip",
                     ["stop_season"],
                     "is_arrested")

def test_get_rates_4():
    ''' Purpose: test big file with two categories '''
    helper_get_rates("data/all_stops_assignment_expected.gzip",
                     "data/all_stops_assignment_ac_dg_arrested_rates.gzip",
                     ["age_category", "driver_gender"],
                     "is_arrested")



def test_get_rates_5():
    ''' Purpose: test bad grouping column name '''
    helper_get_rates("data/all_stops_basic_expected.gzip",
                     None,
                     ["category", "driver_gender"],
                     "arrest_or_citation")

def test_get_rates_6():
    ''' Purpose: test bad outcome column name '''
    helper_get_rates("data/all_stops_basic_expected.gzip",
                     None,
                     ["age_category", "driver_gender"],
                     "foo")



def helper_compute_search_share(stops_pickle_filename,
                                searches_pickle_filename,
                                output_pickle_filename,
                                cat_col,
                                min_stops):
    '''
    Helper function for testing compute_search_share

    Inputs:
      stops_pickle_filename (string): name of the pickle file
        with the stops sample data
      searches_pickle_filename (string): name of the pickle file
        with the searches conducted sample data
      output_pickle_filename (string): name of the pickle file
        with the expected output
      cat_cols (list of strings): names of columns to use for
        grouping
      min_stops (int): minimum number of searches required for
        inclusion
    '''

    stops_df = pd.read_pickle(stops_pickle_filename)
    searches_df = pd.read_pickle(searches_pickle_filename)

    actual_results = ts.compute_search_share(stops_df, searches_df,
                                             cat_col, min_stops)

    err_msg = "Does not handle an unknown cat columns properly"
    if not cat_col:
        err_msg = "Does not handle an empty list of cat columns properly"

    check_against_pickle(actual_results,
                         output_pickle_filename,
                         err_msg)

def test_compute_search_share_1():
    '''
    Purpose: test from writeup
    '''
    helper_compute_search_share(
        "data/all_stops_assignment_expected.gzip",
        "data/search_conducted_assignment_expected.gzip",
        "data/css_assignment_oid_25.gzip",
        ["officer_id"],
        25)

def test_compute_search_share_2():
    '''
    Purpose: test from writeup w/ more stringent filter
    '''

    helper_compute_search_share(
        "data/all_stops_assignment_expected.gzip",
        "data/search_conducted_assignment_expected.gzip",
        "data/css_assignment_oid_1000.gzip",
        ["officer_id"],
        1000)

def test_compute_search_share_3():
    '''
    Purpose: test multiple columns for grouping
    '''

    helper_compute_search_share(
        "data/all_stops_assignment_expected.gzip",
        "data/search_conducted_assignment_expected.gzip",
        "data/css_assignment_oid_dr_1000.gzip",
        ["officer_id", "driver_race"],
        1000)


def test_compute_search_share_4():
    '''
    Purpose: test minimum value larger largest number of stops.
    '''

    helper_compute_search_share(
        "data/all_stops_assignment_expected.gzip",
        "data/search_conducted_assignment_expected.gzip",
        None,
        ["officer_id"],
        1000000)


def test_compute_search_share_5():
    '''
    Purpose: test case where there were no searches conducted, so
    the result from get_rates does not include True
    '''

    helper_compute_search_share("data/all_stops_mini_expected.gzip",
                                "data/search_conducted_mini_expected.gzip",
                                "data/css_mini_oid_1.gzip",
                                ["officer_id"],
                                1)
