import mysql.connector

class database_operation:
    def __init__(self, hostname: str, username: str, pass_word: str, database_name: str) -> None:
        self.mydb = mysql.connector.connect(
        host=hostname,
        user=username,
        password=pass_word,
        database=database_name
        )

    def create_table(self, tablename):
        """
        Function to create table.
        """
        mycursor = self.mydb.cursor()
        sql = "CREATE TABLE " + tablename + " (name VARCHAR(255), points VARCHAR(255))"
        mycursor.execute(sql)
        return True

    def get_table_data(self, tablename):
        """
        Function to get data from table.
        """
        mycursor = self.mydb.cursor()
        sql = "SELECT * FROM "+tablename
        mycursor.execute(sql)
        myresult = mycursor.fetchall()
        return myresult

    def insert_table_data(self, sql, val):
        """
        Function to insert data.
        """
        mycursor = self.mydb.cursor()
        #sql = "INSERT INTO "+tablename+" (name, points) VALUES (%s, %s)"
        #val = ("Devid", "193")
        mycursor.execute(sql, val)
        self.mydb.commit()
        return True


#db = database_operation("127.0.0.1","root","","test")
#sql = "INSERT INTO player (name, points) VALUES (%s, %s)"
#val = ("Alex", "200")
#db.insert_table_data(sql, val)
#print(db.get_table_data("player"))