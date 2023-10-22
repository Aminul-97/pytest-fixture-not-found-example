import pytest
from src.database_manager import database_operation

@pytest.fixture
def initialize_database():
    db = database_operation("127.0.0.1","root","","test")
    return db

def initialize_database():
    db = database_operation("127.10.0.1","root","","test")
    return db

# Testing connection
def test_connection(initialize_database):
    db = initialize_database
    assert db.mydb.is_connected() == True

# Testing create table function
def test_create_table(initialize_database):
    db = initialize_database
    assert db.create_table("player") == True

# Testing insert_data function
def test_insert_data(initialize_database):
    db = initialize_database
    sql = "INSERT INTO player (name, points) VALUES (%s, %s)"
    val = ("Alex", "200")
    assert db.insert_table_data(sql, val) == True

# Testing get_table_data function
def test_get_table_data(initialize_database):
    db = initialize_database
    assert db.get_table_data("player") != None


