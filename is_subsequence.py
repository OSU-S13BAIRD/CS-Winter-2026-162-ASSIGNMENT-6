# Author: Sam Baird
# GitHub username: OSU-S13BAIRD
# Date: 02/11/2026
# Class: INTRO TO COMPUTER SCIENCE II (CS_162_400_F2025)
# Description: Contains a recursive function is_subsequence that checks if the
#              first string is a subsequence of the second string (characters
#              appear in the same relative order, not necessarily consecutive).


def is_subsequence(str1, str2, i1=0, i2=0):
    """
    Recursively checks if str1 is a subsequence of str2.

    Args:
        str1: The potential subsequence string
        str2: The string to search within
        i1:   Current index in str1 (default 0)
        i2:   Current index in str2 (default 0)

    Returns:
        True if str1 is a subsequence of str2, False otherwise
    """
    # Base case 1: all characters of str1 have been matched
    if i1 == len(str1):
        return True

    # Base case 2: exhausted str2 before matching all of str1
    if i2 == len(str2):
        return False

    # If current characters match, advance both indices
    if str1[i1] == str2[i2]:
        return is_subsequence(str1, str2, i1 + 1, i2 + 1)

    # No match — advance only through str2 and keep looking
    return is_subsequence(str1, str2, i1, i2 + 1)
