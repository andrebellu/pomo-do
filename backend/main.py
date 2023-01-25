import mysql.connector
from mysqlx import errorcode

# Connect to server
cnx = mysql.connector.connect(
    host="127.0.0.1",
    port=3306,
    user="root",
    password="")

DB_NAME = "tasksDB"
TABLES = {}

'''
TABLES["tasks"] = (
    "CREATE TABLE `tasks` ("
    "`id` INT(20) NOT NULL AUTO_INCREMENT,"
    "`titolo` VARCHAR(20) NOT NULL,"
    "`data` DATE NOT NULL,"
    "`contenuto` TEXT NOT NULL,"
    "`stato` BOOLEAN NOT NULL,"
    "PRIMARY KEY (`id`)"
    ") ENGINE=InnoDB"
)
'''


TABLES["tasks"] = (
    "CREATE TABLE `tasks` ("
    "`id` INT(20) NOT NULL AUTO_INCREMENT,"
    "`titolo` VARCHAR(20) NOT NULL,"
    "`data` DATE NOT NULL,"
    "`contenuto` TEXT NOT NULL,"
    "`stato` BOOLEAN NOT NULL,"
    "PRIMARY KEY (`id`)"
    ") ENGINE=InnoDB"
)

cur = cnx.cursor()


def create_database(cur):
    try:
        cur.execute(
            "CREATE DATABASE {} DEFAULT CHARACTER SET 'utf8'".format(DB_NAME))
    except mysql.connector.Error as err:
        print("Failed creating database: {}".format(err))
        exit(1)


try:
    cur.execute("USE {}".format(DB_NAME))
    print("Database {} already exists.".format(DB_NAME))
except mysql.connector.Error as err:
    print("Database {} does not exists.".format(DB_NAME))
    if err.errno == errorcode.ER_BAD_DB_ERROR:
        create_database(cur)
        print("Database {} created successfully.".format(DB_NAME))
        cnx.database = DB_NAME
    else:
        print(err)
        exit(1)


for table_name in TABLES:
    table_description = TABLES[table_name]
    try:
        print("Creating table {}: ".format(table_name), end='')
        cur.execute(table_description)
    except mysql.connector.Error as err:
        if err.errno == errorcode.ER_TABLE_EXISTS_ERROR:
            print("already exists.")
        else:
            print(err.msg)
    else:
        print("OK")

cur.close()
cnx.close()
