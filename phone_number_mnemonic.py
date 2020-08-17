from typing import List

from test_framework import generic_test, test_utils


# def phone_mnemonic(phone_number: str) -> List[str]:
#     # TODO - you fill in here.
#     return []

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


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main(
            'phone_number_mnemonic.py',
            'phone_number_mnemonic.tsv',
            phone_mnemonic,
            comparator=test_utils.unordered_compare))
