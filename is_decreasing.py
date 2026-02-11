# Author: Sam Baird
# GitHub username: OSU-S13BAIRD
# Date: 02/11/2026
# Class: INTRO TO COMPUTER SCIENCE II (CS_162_400_F2025)
# Description: Contains a recursive function is_decreasing that takes a list of
#              numbers and returns True if the list is strictly decreasing
#              (each element less than the preceding one), False otherwise.


def is_decreasing(numbers, index=0):
    """
    Recursively checks if a list of numbers is strictly decreasing.

    Args:
        numbers: A list of numbers with at least two elements
        index:   Current position being compared (default 0)

    Returns:
        True if the list is strictly decreasing, False otherwise
    """
    # Base case: reached the last consecutive pair
    if index == len(numbers) - 2:
        return numbers[index] > numbers[index + 1]

    # If current element is not greater than the next, not strictly decreasing
    if numbers[index] <= numbers[index + 1]:
        return False

    # Recursive case: move to the next pair
    return is_decreasing(numbers, index + 1)
