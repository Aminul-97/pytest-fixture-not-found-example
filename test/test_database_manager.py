import pytest
from src.database_manager import database_operation

@pytest.fixture
def initialize_database():
    db = database_operation("player.db")
    return db

## This function will generate a "fixture not found" error
def initialize_database():
    db = database_operation("player.db")
    return db

# Testing connection
def test_connection(initialize_database):
    db = initialize_database
    assert db.check_connection() == True

# Testing create table function
def test_create_table(initialize_database):
    db = initialize_database
    sql = """ CREATE TABLE Player (
            Name CHAR(70) NOT NULL,
            score INT
        ); """
    assert db.create_table(sql) == True

# Testing insert_data function
def test_insert_data(initialize_database):
    db = initialize_database
    sql = """INSERT INTO Player VALUES ('Alen', 120)"""
    assert db.insert_data(sql) == True

# Testing get_table_data function
def test_get_table_data(initialize_database):
    db = initialize_database
    sql = '''SELECT * FROM Player'''
    assert db.get_table_data(sql) != None


