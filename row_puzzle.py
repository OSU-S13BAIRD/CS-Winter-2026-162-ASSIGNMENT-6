# Author: Sam Baird
# GitHub username: OSU-S13BAIRD
# Date: 02/11/2026
# Class: INTRO TO COMPUTER SCIENCE II (CS_162_400_F2025)
# Description: Contains a recursive function row_puzzle that takes a list of
#              nonnegative integers and returns True if a token starting at the
#              leftmost square can reach the rightmost square by moving exactly
#              the value of the current square left or right each turn.


def row_puzzle(row, index=0, visited=None):
    """
    Recursively determines if the row puzzle is solvable.

    Args:
        row:     A list of nonnegative integers with a zero in the rightmost square
        index:   Current position of the token (default 0)
        visited: Set of already-visited indices to avoid cycles (default None)

    Returns:
        True if the token can reach the rightmost square, False otherwise
    """
    # Initialize visited set on first call (avoids mutable default argument)
    if visited is None:
        visited = set()

    # Base case: token has reached the rightmost square
    if index == len(row) - 1:
        return True

    # If this index has already been visited, this path leads to a cycle
    if index in visited:
        return False

    # Mark current index as visited
    visited.add(index)

    step = row[index]
    right = index + step
    left = index - step

    # Try moving right if within bounds
    right_result = right < len(row) and row_puzzle(row, right, visited)

    # Try moving left if within bounds
    left_result = left >= 0 and row_puzzle(row, left, visited)

    # Unmark current index so the list state is restored for other paths
    visited.remove(index)

    return right_result or left_result
