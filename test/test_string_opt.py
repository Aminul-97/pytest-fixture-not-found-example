import pytest
from src.string_opt import join_string, split_string, replace_string, change_case

@pytest.fixture
def updated_joined_text():
    # Holds the output from joined_text()
    return join_string("This is", " a text.")

@pytest.fixture
def updated_split_string():
    # Holds the output from split_string()
    return split_string("Text one-Text two", "-")

@pytest.fixture
def updated_replace_string():
    # Holds the output from replace_string()
    return replace_string("Hellow world!!!", "world", "Jack")

@pytest.fixture
def updated_change_case():
    # Holds the output from change_case()
    return change_case("This is a test")

def test_join_string(updated_joined_text):
    assert updated_joined_text == "This is a text."

def test_split_string(updated_split_string):
    assert updated_split_string == ['Text one', 'Text two']

def test_replace_string(updated_replace_string):
    assert updated_replace_string == "Hellow Jack!!!"

def test_change_case(updated_change_case):
    assert updated_change_case == ('THIS IS A TEST', 'this is a test')