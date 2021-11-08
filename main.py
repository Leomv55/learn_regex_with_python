import sys

import utils
import config
 
def execute_exercises(module_name: str):

    exercise_module = config.MODULES.get(module_name)
    if exercise_module is None:
        raise NotImplementedError(f'Module {module_name} is not implemented yet.')

    PATTERN = getattr(exercise_module, 'PATTERN')
    TEST_CASES = getattr(exercise_module, 'TEST_CASES')

    utils.check_match_and_pretty_print(PATTERN, TEST_CASES)

if __name__ == "__main__":
    exercise_module = sys.argv[1] if len(sys.argv) >= 2 else 'e1'
    execute_exercises(exercise_module)