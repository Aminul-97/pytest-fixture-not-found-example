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

# Testing execute_sql function
def test_execute_sql(initialize_database):
    db = initialize_database
    # Creating table
    sql = """ CREATE TABLE Player (
            Name CHAR(70) NOT NULL,
            score INT
        ); """
    assert db.execute_sql(sql) == True
    # Inserting data
    sql = """INSERT INTO Player VALUES ('Alen', 120)"""
    assert db.execute_sql(sql) == True

# Testing get_table_data function
def test_get_table_data(initialize_database):
    db = initialize_database
    sql = '''SELECT * FROM Player'''
    assert db.get_table_data(sql) != None


