import pytest
from src.database_manager import database_operation

# Fixture to initialize database. We intentionally made a mistake here with the name of the fixture to demonstrate the error.
@pytest.fixture
def initialize_db():
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
    print(db.get_table_data(sql))
    assert db.get_table_data(sql) != None


