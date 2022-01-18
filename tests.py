# the tests
# required imports
import pytest
from main import less_than_ten
import os


# test to check for empty data
def test_empty_data():
    assert less_than_ten()

# test to check for all data to be less than ten
def test_less_than_ten():
    data = less_than_ten()

    for key, value in data.items():
        assert value < 10