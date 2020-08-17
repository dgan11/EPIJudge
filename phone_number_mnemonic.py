from typing import List

from test_framework import generic_test, test_utils


# def phone_mnemonic(phone_number: str) -> List[str]:
#     # TODO - you fill in here.
#     return []

import copy

mapping = ["0", "1", "ABC", "DEF", "GHI", "JKL", "MNO", "PQRS", "TUV", "WXYZ"]

# --- Iterative ----
def phone_mnemonic_iter(phone_number):
    output = [""]
    dummy = []
    for digitIdx in range(len(phone_number)):
        curNum = int(phone_number[digitIdx])
        curLetters = mapping[curNum]
        for letter in curLetters:
            for out in output:
                dummy.append(out+letter)
        output = copy.deepcopy(dummy)
        dummy = []
    return output
"""

"""

# ---- Recursive Solution -----
def phone_mnemonic(phone_number):
    mapping = ["0", "1", "ABC", "DEF", "GHI", "JKL", "MNO", "PQRS", "TUV", "WXYZ"]
    output = []
    phoneHelper("", 0, phone_number, len(phone_number), output, mapping)
    return output

def phoneHelper(curStr, digitIdx, phone_number, n, output, mapping):
    if digitIdx == n:
        output.append(curStr)
        return
    curNum = int(phone_number[digitIdx])
    curLetters = mapping[curNum]
    for letter in curLetters:
        phoneHelper(curStr+letter, digitIdx+1, phone_number, n, output, mapping)

"""
Time  : O(4^n) -- in the worst case, there are 4 letters for each of the N numbers
Space : O(4^n) -- there are 4^n calls on the call stack
"""



if __name__ == '__main__':
    exit(
        generic_test.generic_test_main(
            'phone_number_mnemonic.py',
            'phone_number_mnemonic.tsv',
            phone_mnemonic,
            comparator=test_utils.unordered_compare))
