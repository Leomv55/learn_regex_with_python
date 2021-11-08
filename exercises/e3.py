# Write a Python program that matches a string that has an a followed by zero or more b's.

TEST_CASES = {
    "case_1": 'baaa',
    "case_2": 'abbbbb',
    "case_3": 'abab',
    "case_4": 'aba',
    "case_5": 'a',
    "case_6": 'b'
}

PATTERN = r'^(a|A)(b|B)+$'
