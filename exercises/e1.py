# Write a Python program to check that a string contains only a certain set of characters (in this case a-z, A-Z and 0-9).

TEST_CASES = {
    "case_1": 'Hi',
    "case_2": 'Hi!^&*()',
    "case_3": 'Hi89',
    "case_4": '89',
}

PATTERN = r'^[a-zA-Z0-9]*$'


