import sys

import utils
import config
 
def execute_exercises(module_name: str):

    module = config.MODULES.get(test_file_name)
    if module is None:
        raise NotImplementedError(f'Module {module_name} is not implemented yet.')

    PATTERN = getattr(module, 'PATTERN')
    TEST_CASES = getattr(module, 'TEST_CASES')

    utils.check_match_and_pretty_print(PATTERN, TEST_CASES)

if __name__ == "__main__":
    test_file_name = sys.argv[1] if len(sys.argv) >= 2 else 'e1'
    execute_exercises(test_file_name)