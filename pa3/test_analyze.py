# -*- coding: utf-8 -*-
"""Testing the tweet analysis code

This module contains the test for your
tweet analysis code. It runs the basic
analysis algorithms on test files of tweets.
"""

import os
import sys
import json
import pytest

from analyze import find_top_k_entities, find_min_count_entities
from analyze import find_frequent_entities, find_top_k_ngrams
from analyze import find_min_count_ngrams, find_frequent_ngrams
from analyze import find_top_k_ngrams_by_month
from util import sort_count_pairs

# Handle the fact that the grading code may not
# be in the same directory as analyze.py
sys.path.append(os.getcwd())

# Get the test files from the same directory as
# this file.
BASE_DIR = os.path.dirname(__file__)

######### Utilities #########

# DO NOT REMOVE THIS LINE OF CODE
# pylint: disable-msg=consider-using-ternary
def is_sequence(arg):
    '''
    Take this code as a black box, it checks whether an object is a list or
    tuple but not a string.

    Ref. stackoverflow.com/questions/1835018/python-check-if-an-object-is
        -a-list-or-tuple-but-not-string
    '''
    return (not hasattr(arg, "strip") and
            hasattr(arg, "__getitem__") or
            hasattr(arg, "__iter__"))

# DO NOT REMOVE THIS LINE OF CODE
# pylint: disable-msg=invalid-name
def check_type(l):
    '''
    Does l have the format: list-like value with tuples of length 2 as
    elements?
    '''
    if not is_sequence(l):
        return False
    for item in l:
        if not isinstance(item, tuple) or len(item) != 2:
            return False

    return True

######### Helpers #########


task_to_fn = {"task1": find_top_k_entities,
              "task2": find_min_count_entities,
              "task3": find_frequent_entities,
              "task4": find_top_k_ngrams,
              "task5": find_min_count_ngrams,
              "task6": find_frequent_ngrams,
              "task7": find_top_k_ngrams_by_month}

# DO NOT REMOVE THIS LINE OF CODE
# pylint: disable-msg=consider-using-enumerate, unused-variable
def get_expected(test_description):
    '''
    Get the expected value from the file and convert convert inner
    lists to tuples.  Why? Because JSON does not support tuples.
    '''

    try:
        expected = json.load(open(test_description["expected_filename"]))
    except OSError as e:
        return None

    if test_description["task"] in ["task1", "task2", "task3"]:
        for i in range(len(expected)):
            expected[i] = tuple(expected[i])
    elif test_description["task"] in ["task4", "task5", "task6"]:
        for i in range(len(expected)):
            expected[i] = (tuple(expected[i][0]), expected[i][1])
    else:
        assert test_description["task"] == "task7"
        for i in range(len(expected)):
            (year_month, topk) = expected[i]
            for j in range(len(topk)):
                (ngram, count) = topk[j]
                topk[j] = (tuple(ngram), count)
            expected[i] = (tuple(year_month), topk)

    return expected


# DO NOT REMOVE THIS LINE OF CODE
# pylint: disable-msg=broad-except
def helper(test_description):
    '''
    Do a test, check the result, report an error, if necessary.
    '''

    task = test_description["task"]

    # load the tweets from the file
    try:
        tweet_filename = os.path.join(BASE_DIR,
                                      test_description["tweet_filename"])
        tweets = json.load(open(tweet_filename))
    except OSError as e:
        pytest.fail("{}".format(e))

    expected = get_expected(test_description)
    if expected is None:
        pytest.fail("Could not open expected result file:" +
                    test_description["expected_filename"] + ":")

    try:
        actual = task_to_fn[task](tweets, test_description["arg1"],
                                  test_description["arg2"])
    except Exception as e:
        pytest.fail("{}".format(e))

    if not check_type(actual):
        s = ("Actual result has the wrong type."
             " The correct type is list of pairs "
             "(that is, tuples of length 2)")
        pytest.fail(s)

    if actual != expected:
        if len(actual) != len(expected):
            s = ("Length of actual result ({}) does not match "
                 "the length of the expected result ({})")
            pytest.fail(s.format(len(actual), len(expected)))

        if sort_count_pairs(actual) == expected:
            pytest.fail("Actual result is not sorted properly.")

        for i in range(len(actual)):
            if actual[i] != expected[i]:
                s = ("Actual result at index {} ({}) does not match"
                     "expected result ({}) at index {}.")
                pytest.fail(s.format(i, actual[i], expected[i], i))

    # Test succeeded if you get to here
    return

######### API Test #########


def test_task1_api0():
    '''
    Test whether keys and subkeys are handled properly in find_top_k_entities
    '''

    tweets = [{'entities': {'dogs': [{'type': 'poodle'}]}}]
    assert (find_top_k_entities(tweets, ("dogs", "type"), 1) ==
            [('poodle', 1)])


def test_task1_api1():
    '''
    Test whether upper and lower case is handled properly
    '''
    tweets = [{'entities': {'dogs': [{'type': 'poodle'}]}},
              {'entities': {'dogs': [{'type': 'Poodle'}]}}]
    assert (find_top_k_entities(tweets, ("dogs", "type"), 1) ==
            [('poodle', 2)])


def test_task1_api2():
    '''
    Test whether entity multiplicity is handled properly
    '''
    tweets = [{'entities': {'dogs': [{'type': 'poodle'}, {'type': 'poodle'}]}}]
    assert (find_top_k_entities(tweets, ("dogs", "type"), 1) ==
            [('poodle', 2)])


def test_task1_api3():
    '''
    Test whether entity multiplicity is handled properly
    '''
    tweets = [{'entities': {'dogs': [{'type': 'poodle'}, {'type': 'poodle'}]}}]
    assert (find_top_k_entities(tweets, ("dogs", "type"), 1) ==
            [('poodle', 2)])


def test_task1_api4():
    '''
    Test whether functionality works
    '''
    tweets = [{'entities': {'hashtags': [{'text': '#abc'}]}},
              {'entities': {'hashtags': [{'text': '#bcd'}]}},
              {'entities': {'hashtags': [{'text': '#bad'}]}},
              {'entities': {'hashtags': [{'text': '#bcd'}]}},
              {'entities': {'hashtags': [{'text': '#abc'}]}}]

    assert (find_top_k_entities(tweets, ("hashtags", "text"), 2) ==
            [('#abc', 2), ('#bcd', 2)])


def test_task2_api0():
    '''
    Test whether keys and subkeys are handled properly in find_top_k_entities
    '''
    tweets = [{'entities': {'dogs': [{'type': 'poodle'}]}}]
    assert (find_min_count_entities(
        tweets, ("dogs", "type"), 1) == [('poodle', 1)])


def test_task2_api1():
    '''
    Test whether upper and lower case is handled properly
    '''
    tweets = [{'entities': {'dogs': [{'type': 'poodle'}]}},
              {'entities': {'dogs': [{'type': 'Poodle'}]}}]
    assert (find_min_count_entities(
        tweets, ("dogs", "type"), 1) == [('poodle', 2)])


def test_task2_api2():
    '''
    Test whether entity multiplicity is handled properly
    '''
    tweets = [{'entities': {'dogs': [{'type': 'poodle'}, {'type': 'poodle'}]}}]
    assert (find_min_count_entities(
        tweets, ("dogs", "type"), 1) == [('poodle', 2)])


def test_task2_api3():
    '''
    Test whether entity multiplicity is handled properly
    '''
    tweets = [{'entities': {'dogs': [{'type': 'poodle'}, {'type': 'poodle'}]}}]
    assert (find_min_count_entities(
        tweets, ("dogs", "type"), 1) == [('poodle', 2)])


def test_task2_api4():
    '''
    Test whether functionality works end-to-end
    '''
    tweets = [{'entities': {'hashtags': [{'text': '#abc'}]}},
              {'entities': {'hashtags': [{'text': '#bcd'}]}},
              {'entities': {'hashtags': [{'text': '#bad'}]}},
              {'entities': {'hashtags': [{'text': '#bcd'}]}},
              {'entities': {'hashtags': [{'text': '#abc'}]}}]

    assert (find_min_count_entities(tweets, ("hashtags", "text"), 1) ==
            [('#abc', 2), ('#bcd', 2), ("#bad", 1)])
    assert (find_min_count_entities(tweets, ("hashtags", "text"), 2) ==
            [('#abc', 2), ('#bcd', 2)])
    assert find_min_count_entities(tweets, ("hashtags", "text"), 3) == []


def test_task3_api0():
    '''
    Test whether keys and subkeys are handled properly in
    find_frequent_entities
    '''
    tweets = [{'entities': {'dogs': [{'type': 'poodle'}]}}]
    assert (find_frequent_entities(
        tweets, ("dogs", "type"), 2) == [('poodle', 1)])


def test_task3_api1():
    '''
    Test whether upper and lower case is handled properly in
    find_frequent_entities
    '''
    tweets = [{'entities': {'dogs': [{'type': 'poodle'}]}},
              {'entities': {'dogs': [{'type': 'Poodle'}]}}]
    assert (find_frequent_entities(
        tweets, ("dogs", "type"), 2) == [('poodle', 2)])


def test_task3_api2():
    '''
    Test whether entity multiplicity is handled properly
    '''
    tweets = [{'entities': {'dogs': [{'type': 'poodle'}, {'type': 'poodle'}]}}]
    assert (find_min_count_entities(
        tweets, ("dogs", "type"), 1) == [('poodle', 2)])


def test_task3_api3():
    '''
    Test whether entity multiplicity is handled properly
    '''
    tweets = [{'entities': {'dogs': [{'type': 'poodle'}, {'type': 'poodle'}]}}]
    assert (find_min_count_entities(
        tweets, ("dogs", "type"), 1) == [('poodle', 2)])


def test_task3_api4():
    '''
    Test whether functionality works
    '''
    tweets = [{'entities': {'hashtags': [{'text': '#abc'}]}},
              {'entities': {'hashtags': [{'text': '#bcd'}]}},
              {'entities': {'hashtags': [{'text': '#bad'}]}},
              {'entities': {'hashtags': [{'text': '#bcd'}]}},
              {'entities': {'hashtags': [{'text': '#abc'}]}}]

    assert (find_frequent_entities(
        tweets, ("hashtags", "text"), 2) == [('#abc', 1)])
    assert (find_frequent_entities(tweets, ("hashtags", "text"), 3) ==
            [('#abc', 1), ('#bcd', 1)])
    assert (find_frequent_entities(tweets, ("hashtags", "text"), 4) ==
            [('#abc', 2), ('#bcd', 2), ('#bad', 1)])


def test_task4_api0():
    '''
    Test Stop word removal and ordering
    '''
    tweets = [{'text': 'the dog a dog'}]
    assert find_top_k_ngrams(tweets, 2, 1) == [(('dog', 'dog'), 1)]


def test_task4_api1():
    '''
    Test punctuation removal
    '''
    tweets = [{'text': 'the dog, a dog'}]
    assert find_top_k_ngrams(tweets, 2, 1) == [(('dog', 'dog'), 1)]


def test_task4_api2():
    '''
    Test handling cases
    '''
    tweets = [{'text': 'Dog dog'}]
    assert find_top_k_ngrams(tweets, 2, 1) == [(('dog', 'dog'), 1)]


def test_task4_api3():
    '''
    Test to see if prefix filtering is done properly
    '''
    tweets = [{'text': '@Dog dog'}]
    assert find_top_k_ngrams(tweets, 2, 1) == []


def test_task4_api4():
    '''
    Test emoji removal
    '''
    tweets = [{'text': ';)'}]
    assert find_top_k_ngrams(tweets, 2, 1) == []


def test_task4_api5():
    '''
    Test to end-to-end functionality
    '''
    tweets = [{'text': 'the cat in the hat'},
              {'text': "don't let the cat on the hat"},
              {'text': "the cat's hat"},
              {'text': "the hat cat"}]
    assert find_top_k_ngrams(tweets, 2, 1) == [(('cat', 'hat'), 2)]
    assert find_top_k_ngrams(tweets, 3, 1) == [(("don't", 'let', 'cat'), 1)]
    assert (find_top_k_ngrams(tweets, 4, 1) == [
        (("don't", 'let', 'cat', 'hat'), 1)])


def test_task5_api1():
    '''
    Test punctuation removal
    '''
    tweets = [{'text': 'the dog, a dog'}]
    assert find_min_count_ngrams(tweets, 2, 1) == [(('dog', 'dog'), 1)]


def test_task5_api2():
    '''
    Test upper and lower case handling
    '''
    tweets = [{'text': 'Dog dog'}]
    assert find_min_count_ngrams(tweets, 2, 1) == [(('dog', 'dog'), 1)]


def test_task5_api3():
    '''
    Test to see if prefix filtering is done properly
    '''
    tweets = [{'text': '@Dog dog'}]
    assert find_min_count_ngrams(tweets, 2, 1) == []


def test_task5_api4():
    '''
    Test emoji removal
    '''
    tweets = [{'text': ';)'}]
    assert find_min_count_ngrams(tweets, 2, 1) == []


def test_task5_api5():
    '''
    Test end-to-end functionality
    '''
    tweets = [{'text': 'the cat in the hat'},
              {'text': "don't let the cat on the hat"},
              {'text': "the cat's hat"},
              {'text': "the hat cat"}]
    assert find_min_count_ngrams(tweets, 2, 2) == [(('cat', 'hat'), 2)]
    assert find_min_count_ngrams(tweets, 3, 2) == []
    assert (find_min_count_ngrams(tweets, 4, 1) ==
            [(("don't", 'let', 'cat', 'hat'), 1)])


def test_task6_api1():
    '''
    Test punctuation removal
    '''
    tweets = [{'text': 'the dog, a dog'}]
    assert find_frequent_ngrams(tweets, 2, 2) == [(('dog', 'dog'), 1)]


def test_task6_api2():
    '''
    Test upper and lower case handling
    '''
    tweets = [{'text': 'Dog dog'}]
    assert find_frequent_ngrams(tweets, 2, 2) == [(('dog', 'dog'), 1)]


def test_task6_api3():
    '''
    Test to see if prefix filtering is done properlu
    '''
    tweets = [{'text': '@Dog dog'}]
    assert find_frequent_ngrams(tweets, 2, 2) == []


def test_task6_api4():
    '''
    Test emoji removal
    '''
    tweets = [{'text': ';)'}]
    assert find_frequent_ngrams(tweets, 2, 1) == []


def test_task6_api5():
    '''
    Test end-to-end functionality
    '''
    tweets = [{'text': 'the cat in the hat'},
              {'text': "don't let the cat on the hat"},
              {'text': "the cat's hat"},
              {'text': "the hat cat"}]
    assert find_frequent_ngrams(tweets, 2, 6)[0] == (('cat', 'hat'), 2)


######### Generated test code #########

def test_task1_0():
    '''
    top-k entities example
    '''
    helper({
        'task': 'task1', 'tweet_filename': 'data/theSNP.json', 'arg1':
        ('hashtags', 'text'), 'arg2': 3, 'expected_filename':
            'data/test-task1-0-expected.json'})


def test_task1_1():
    '''
    basic test
    '''
    helper({'task': 'task1', 'tweet_filename': 'data/UKLabour-May-week1.json',
            'arg1': ('user_mentions', 'screen_name'), 'arg2': 1,
            'expected_filename': 'data/test-task1-1-expected.json'})


def test_task1_2():
    '''
    corner case: list of tweets is empty
    '''
    helper({'task': 'task1', 'tweet_filename': 'data/zero-tweets.json',
            'arg1': ('hashtags', 'text'), 'arg2': 1, 'expected_filename':
            'data/test-task1-2-expected.json'})


def test_task1_3():
    '''
    corner case:k is 0
    '''
    helper({'task': 'task1', 'tweet_filename': 'data/UKLabour-May-week1.json',
            'arg1': ('hashtags', 'text'), 'arg2': 0, 'expected_filename':
            'data/test-task1-3-expected.json'})


def test_task1_4():
    '''
    corner case: corner-2 has one tweet w/ 0 hashtags
    '''
    helper({'task': 'task1', 'tweet_filename': 'data/corner-2.json', 'arg1':
            ('hashtags', 'text'), 'arg2': 1, 'expected_filename':
            'data/test-task1-4-expected.json'})


def test_task1_5():
    '''
    corner case: corner-2 has one tweet w/ 0 urls
    '''
    helper({'task': 'task1', 'tweet_filename': 'data/corner-2.json', 'arg1':
            ('urls', 'url'), 'arg2': 1, 'expected_filename':
            'data/test-task1-5-expected.json'})


def test_task1_6():
    '''
    corner case: corner-2 has one tweet w/ 0 user mentions
    '''
    helper({'task': 'task1', 'tweet_filename': 'data/corner-2.json', 'arg1':
            ('user_mentions', 'screen_name'), 'arg2': 1, 'expected_filename':
            'data/test-task1-6-expected.json'})


def test_task1_7():
    '''
    corner case: one tweet w/ 1 hashtags
    '''
    helper({'task': 'task1', 'tweet_filename': 'data/corner-3.json', 'arg1':
            ('hashtags', 'text'), 'arg2': 3, 'expected_filename':
            'data/test-task1-7-expected.json'})


def test_task2_0():
    '''
    min count entities example
    '''
    helper({'task': 'task2', 'tweet_filename': 'data/LibDems.json', 'arg1':
            ('user_mentions', 'screen_name'), 'arg2': 100, 'expected_filename':
            'data/test-task2-0-expected.json'})


def test_task2_1():
    '''
    basic test
    '''
    helper({'task': 'task2', 'tweet_filename': 'data/UKLabour-May-week1.json',
            'arg1': ('urls', 'url'), 'arg2': 2, 'expected_filename':
            'data/test-task2-1-expected.json'})


def test_task2_2():
    '''
    corner case: list of tweets is empty
    '''
    helper({'task': 'task2', 'tweet_filename': 'data/zero-tweets.json',
            'arg1': ('hashtags', 'text'), 'arg2': 1, 'expected_filename':
            'data/test-task2-2-expected.json'})


def test_task2_3():
    '''
    corner case: k is 0
    '''
    helper({'task': 'task2', 'tweet_filename': 'data/UKLabour-May-week1.json',
            'arg1': ('hashtags', 'text'), 'arg2': 0, 'expected_filename':
            'data/test-task2-3-expected.json'})


def test_task2_4():
    '''
    corner case: one tweet with one 1 hashtag
    '''
    helper({'task': 'task2', 'tweet_filename': 'data/corner-2.json', 'arg1':
            ('hashtags', 'text'), 'arg2': 1, 'expected_filename':
            'data/test-task2-4-expected.json'})


def test_task2_5():
    '''
    corner case: one tweet with one hashtag, k greater than 1
    '''
    helper({'task': 'task2', 'tweet_filename': 'data/corner-2.json', 'arg1':
            ('hashtags', 'text'), 'arg2': 3, 'expected_filename':
            'data/test-task2-5-expected.json'})


def test_task3_0():
    '''
    frequent entities example
    '''
    helper({'task': 'task3', 'tweet_filename': 'data/Conservatives.json',
            'arg1': ('hashtags', 'text'), 'arg2': 5, 'expected_filename':
            'data/test-task3-0-expected.json'})


def test_task3_1():
    '''
    basic test
    '''
    helper({'task': 'task3', 'tweet_filename': 'data/UKLabour-May-week1.json',
            'arg1': ('user_mentions', 'screen_name'), 'arg2': 4,
            'expected_filename': 'data/test-task3-1-expected.json'})


def test_task3_2():
    '''
    corner case: list of tweets is empty
    '''
    helper({'task': 'task3', 'tweet_filename': 'data/zero-tweets.json', 'arg1':
            ('hashtags', 'text'), 'arg2': 1, 'expected_filename':
            'data/test-task3-2-expected.json'})


def test_task3_3():
    '''
    corner case: result should be empty
    '''
    helper({'task': 'task3', 'tweet_filename': 'data/UKLabour-May-week1.json',
            'arg1': ('user_mentions', 'screen_name'), 'arg2': 2,
            'expected_filename': 'data/test-task3-3-expected.json'})


def test_task3_4():
    '''
    corner case: result should have one value
    '''
    helper({'task': 'task3', 'tweet_filename': 'data/corner-2.json', 'arg1':
            ('hashtags', 'text'), 'arg2': 3, 'expected_filename':
            'data/test-task3-4-expected.json'})


def test_task3_5():
    '''
    K of 1 should always return [], because it is not possible to exceed 100%
    '''
    helper({'task': 'task3', 'tweet_filename': 'data/UKLabour-May-week1.json',
            'arg1': ('hashtags', 'text'), 'arg2': 1, 'expected_filename':
            'data/test-task3-5-expected.json'})


def test_task4_0():
    '''
    top k ngrams example
    '''
    helper({'task': 'task4', 'tweet_filename': 'data/theSNP.json', 'arg1': 2,
            'arg2': 3, 'expected_filename': 'data/test-task4-0-expected.json'})


def test_task4_1():
    '''
    basic test
    '''
    helper({'task': 'task4', 'tweet_filename': 'data/UKLabour-May-week1.json',
            'arg1': 1, 'arg2': 3, 'expected_filename':
            'data/test-task4-1-expected.json'})


def test_task4_2():
    '''
    basic test
    '''
    helper({'task': 'task4', 'tweet_filename': 'data/UKLabour-May-week1.json',
            'arg1': 3, 'arg2': 3, 'expected_filename':
            'data/test-task4-2-expected.json'})


def test_task4_3():
    '''
    corner cases: list of tweets is empty
    '''
    helper({'task': 'task4', 'tweet_filename': 'data/zero-tweets.json',
            'arg1': 1, 'arg2': 1, 'expected_filename':
            'data/test-task4-3-expected.json'})


def test_task4_4():
    '''
    corner cases: k is 0
    '''
    helper({'task': 'task4', 'tweet_filename': 'data/UKLabour-May-week1.json',
            'arg1': 1, 'arg2': 0, 'expected_filename':
            'data/test-task4-4-expected.json'})


def test_task4_5():
    '''
    corner case: check empty sets for stop words and stop prefixes.
    '''
    helper({'task': 'task4', 'tweet_filename': 'data/UKLabour-May-week1.json',
            'arg1': 1, 'arg2': 3, 'expected_filename':
            'data/test-task4-5-expected.json'})


def test_task4_6():
    '''
    corner case: file contains a single tweet that contains only hashtags,
urls, and user_mentions.  Preprocessing the text will
yield an empty list of ngrams
    '''
    helper({'task': 'task4', 'tweet_filename': 'data/entities-only.json',
            'arg1': 1, 'arg2': 3, 'expected_filename':
            'data/test-task4-6-expected.json'})


def test_task4_7():
    '''
    corner case: check whether punctuation is stripped properly.
    file contains a single synthetic tweet:
        'Hillary $$Hillary Hillary.hillary ..Hillary..'
    '''
    helper({'task': 'task4', 'tweet_filename': 'data/syn-0.json', 'arg1': 1,
            'arg2': 1, 'expected_filename': 'data/test-task4-7-expected.json'})


def test_task4_8():
    '''
    corner case: check whether tweets that have fewer than
    n words are handled properly.
    file contains a single synthetic tweet:   'hillary'
    '''
    helper({'task': 'task4', 'tweet_filename': 'data/syn-1.json', 'arg1': 2,
            'arg2': 1, 'expected_filename': 'data/test-task4-8-expected.json'})


def test_task5_0():
    '''
    min count ngrams example
    '''
    helper({'task': 'task5', 'tweet_filename': 'data/LibDems.json', 'arg1': 2,
            'arg2': 100, 'expected_filename':
            'data/test-task5-0-expected.json'})


def test_task5_1():
    '''
    basic test
    '''
    helper({'task': 'task5', 'tweet_filename': 'data/UKLabour-May-week1.json',
            'arg1': 1, 'arg2': 30, 'expected_filename':
            'data/test-task5-1-expected.json'})


def test_task5_2():
    '''
    corner cases: list of tweets is empty
    '''
    helper({'task': 'task5', 'tweet_filename': 'data/zero-tweets.json',
            'arg1': 1, 'arg2': 1, 'expected_filename':
            'data/test-task5-2-expected.json'})


def test_task5_3():
    '''
    corner case: no single word occurs at least 150 times.
    '''
    helper({'task': 'task5', 'tweet_filename': 'data/UKLabour-May-week1.json',
            'arg1': 1, 'arg2': 150, 'expected_filename':
            'data/test-task5-3-expected.json'})


'''
# This test has been removed due to issues with the emoji
# library.
def test_task6_0():

    helper({'task': 'task6', 'tweet_filename': 'data/Conservatives.json', 'arg1': 2,
            'arg2': 3, 'expected_filename': 'data/test-task6-0-expected.json'})
'''


def test_task6_1():
    '''
    corner cases: list of tweets is empty
    '''
    helper({'task': 'task6', 'tweet_filename': 'data/zero-tweets.json',
            'arg1': 1, 'arg2': 1, 'expected_filename':
            'data/test-task6-1-expected.json'})


def test_task6_2():
    '''
    corner case: result should be empty
    '''
    helper({'task': 'task6', 'tweet_filename': 'data/UKLabour-May-week1.json',
            'arg1': 2, 'arg2': 2, 'expected_filename':
            'data/test-task6-2-expected.json'})


def test_task7_0():
    '''
    top k by month example
    '''
    helper({'task': 'task7', 'tweet_filename': 'data/UKLabour.json', 'arg1': 2,
            'arg2': 3, 'expected_filename': 'data/test-task7-0-expected.json'})


def test_task7_1():
    '''
    basic test
    '''
    helper({'task': 'task7', 'tweet_filename': 'data/Conservatives.json',
            'arg1': 2, 'arg2': 3, 'expected_filename':
            'data/test-task7-1-expected.json'})


def test_task7_2():
    '''
    corner cases: list of tweets is empty
    '''
    helper({'task': 'task7', 'tweet_filename': 'data/zero-tweets.json',
            'arg1': 1, 'arg2': 1, 'expected_filename':
            'data/test-task7-2-expected.json'})


def test_task7_3():
    '''
    corner cases: one tweet
    '''
    helper({'task': 'task7', 'tweet_filename': 'data/corner-2.json', 'arg1': 1,
            'arg2': 1, 'expected_filename': 'data/test-task7-3-expected.json'})
