import pytest
from src.string_opt import join_string, split_string, replace_string, change_case

@pytest.fixture
def updated_joined_text():
    return join_string("AA", "BB")

@pytest.fixture
def updated_split_string():
    return split_string("A-B", "-")

@pytest.fixture
def updated_replace_string():
    return replace_string("ABC", "B", "-")

@pytest.fixture
def updated_change_case():
    return change_case("Abc123")

def test_join_string(updated_joined_text):
    assert updated_joined_text == "AABB"

def test_split_string(updated_split_strin):
    assert updated_split_string == ['A', 'B']

def test_replace_string(updated_replace_strin):
    assert updated_replace_string == "A-C"

def test_change_case(updated_change_case):
    assert updated_change_case == ('ABC123', 'abc123')