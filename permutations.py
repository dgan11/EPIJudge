from typing import List

from test_framework import generic_test, test_utils

import copy 

# def permutations(A: List[int]) -> List[List[int]]:

def permutations(A):
    out = []
    helper(A, 0, out)
    return out

def helper(A, curIdx, out):
    if curIdx == len(A)-1:
        #print(A)
        out.append(copy.deepcopy(A))

    # -- Each number should be the first element in the list
    for j in range(curIdx, len(A)):
        #print("curIdx is: ", curIdx, "j is: ", j)
        A[curIdx], A[j] = A[j], A[curIdx]
        #print("initial switch: ", A)
        #  -- Generate all permutations for A[i+1]
        helper(A, curIdx+1, out)
        A[j], A[curIdx] = A[curIdx], A[j]
        #print("switch back: ", A)
    
"""
Time  : O(n * n!) -- n! recursive calls because n places to put the first number, n-1 places
                    to put the second and so on. Also in each of the recursive calls we do n work
                    in the worst case (j iteration).
Space : O(n!) -- number of recursive calls
"""

if __name__ == '__main__':
    exit(
        generic_test.generic_test_main('permutations.py', 'permutations.tsv',
                                       permutations,
                                       test_utils.unordered_compare))
