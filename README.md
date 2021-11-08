# Learn regex with python

## File structure
- `exercises`
  - `e1.py`
  - `e2.py`
  - `e3.py`
- `main.py`
- `utils.py`
- `config.py`

## Exercises

### Exercise 1 (`e1.py`)
> Q: Write a Python program to check that a string contains only a certain set of characters (in this case a-z, A-Z and 0-9).

### Exercise 2 (`e2.py`)
> Q: Write a Python program that matches a string that has an a followed by zero or more b's.

### Exercise 3 (`e3.py`)
> Q: Write a Python program that matches a string that has an a followed by zero or more b's.

## How to run ?
1. Checkout to the `main` branch.
2. Run `python3 main.py <module_name>` Eg: `python3 main.py e2`

## How to add a new exercise ?
1. Create a new file inside exercises with file name `e<serial_number>.py`.
2. Add 
  ```
  TEST_CASES = {
    "case_1": "case 1 string",
    "case_2": "case 2 string"
  }
  PATTERN = <Your Pattern here>
  ```  
  to the newly created file.

3. Go to `__init__.py` and import the newly added module.
4. Go to `config.py` and add the new module to `MODULES`

## How to contribute
1. Create an issue 
2. Fork this repo
3. Create a PR to the `development` branch with the issue reference.



