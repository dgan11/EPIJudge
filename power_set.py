from typing import List

from test_framework import generic_test, test_utils


# def generate_power_set(input_set: List[int]) -> List[List[int]]:
#     # TODO - you fill in here.


def generate_power_set(input_set):
    # TODO - you fill in here.
    out = [[]]
    return find_powerset_of_ith_index(input_set, len(input_set)-1, out)


def find_powerset_of_ith_index(input_set, i, out):
    if i == -1:
        return out

    # P(x) = P(x-1) and then adding input_set at index x to all the previous sets
    out = find_powerset_of_ith_index(input_set, i-1, out)
    #print("out: ", out)
    # Add the number from the ith index to all the previous subsets
    out += [prevSet + [input_set[i]] for prevSet in out]
    return out

"""
Time  : O(n * 2^n) Each element can be in or not in a set of the powerset. So O(2^n) recursive calls and 
        for each call doing O(n) work in worst case (looping through the previous set and adding the new element)

Space : O(2^n) will have the number of recursive calls on the call stack. Also have an array of 2^n elements at the end.
"""


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main('power_set.py', 'power_set.tsv',
                                       generate_power_set,
                                       test_utils.unordered_compare))
