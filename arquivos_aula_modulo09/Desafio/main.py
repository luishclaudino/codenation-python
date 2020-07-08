# .travis.yml
config = """
language: python

# current default Python on Travis CI
python:
    - "2.7"
    - "3.7"
    - "pypy"
    - "pypy3"

# command to install dependencies
install:
    - pip install -r requirements.txt

# command to run tests
script: pytest
"""
