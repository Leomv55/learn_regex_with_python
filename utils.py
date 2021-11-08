import re

def check_match_and_pretty_print(pattern: str, test_cases: dict):
    for (test_case_key, test_case_val) in test_cases.items():
        matcher = re.fullmatch(pattern, test_case_val)
        is_match = True if matcher else False
        print(test_case_key, test_case_val, is_match)