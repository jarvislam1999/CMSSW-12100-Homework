"""
DO NOT MODIFY THIS CODE!

Code to find punctuation.
"""

import sys
import unicodedata
import emoji

# Find all characters that are classified as punctuation in Unicode
# (except #, @, &) and combine them into a single string.


def keep_chr(char):
    """
    keep punctuation characters if they are not #, @, &
    """
    return (unicodedata.category(char).startswith('P') and
            (char != "#" and char != "@" and char != "&"))

PUNCTUATION = " ".join(
    [chr(i) for i in range(sys.maxunicode) if keep_chr(chr(i))])

# When processing tweets, ignore words, symbols, and emoji in this set.
WORDS = ["a", "an", "the", "this", "that", "of", "for", "or",
         "and", "on", "to", "be", "if", "we", "you", "in", "is",
         "at", "it", "rt", "mt", "with"]

SYMBOLS = [chr(i) for i in range(sys.maxunicode) if
           unicodedata.category(chr(i)) in ("Sm", "Sc", "Sk", "So")] + ["\n"]

EMOJI = list(emoji.UNICODE_EMOJI.keys())

STOP_WORDS = set(WORDS + SYMBOLS + EMOJI)

# When processing tweets, words w/ a prefix that appears in this list
# should be ignored.
STOP_PREFIXES = ("@", "#", "http", "&amp")

