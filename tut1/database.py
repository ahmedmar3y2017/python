import mysql.connector
from mysql.connector import errorcode


try:
    # ------------------------------- make connections ---------------------------------

    conn = mysql.connector.connect(
        user="root", password="root",  host="localhost")

    cur = conn.cursor()
    # -------------------------------- create new  database -----------------------
    cur.execute("create database tt")


except mysql.connector.Error as err:
    # check if database exists
    if(err.errno == errorcode.ER_DB_CREATE_EXISTS):
        print("Exists Database ")
    else:
        print("Failed Create Database : ",  format(err))
        exit(1)
# connect to database
conn.database = "tt"
try:
    #  -------------------------------------- create table -----------------------
    cur.execute("create table `user` (`id` int(10) primary key  not null auto_increment , `username` varchar(100) not null  , `address` varchar(100) not null   )")

except mysql.connector.Error as err:
    # IF Exits table
    if(err.errno == errorcode.ER_TABLE_EXISTS_ERROR):
        print("This table Exists : ")
    else:
        print(err.message)

# --------------------------- crud applications -----------------------

try:
    uuername = "mohamed"
    aadress = "cairo"
    # ------------------------------- Insert ------------------------------
    cur.execute(
        "insert into `user` (`username`, `address`) values ('ahmed' ,'tanta' )")
    # dynamic insert element into database
    cur.execute("insert into `user` (`username`, `address`) values ('%s', '%s' )" % (
        uuername, aadress))
    conn.commit()
except mysql.connector.Error as err:
    print(err.message)
    exit(1)

try:
    #  ---------------------------- update Operations -------------------------------
    cur.execute("update user set address = '%s' where id='%d'" % ("alex", 1))
    conn.commit()
except:
    conn.rollback()


try:
    cur.execute("delete from user where id='%d'" % (2))
    conn.commit()
except:
    conn.rollback()

try:
    # ------------------------------- select --------------------------
    # dynamic select
    cur.execute("select username, address from user where id < '%d'" % (5))

except mysql.connector.Error as err:
    print(err.message)
    exit(1)

results = cur.fetchall()
# print values
for row in results:
    print(row[0], "   **   ", row[1])


# colse connections
conn.close()

# check if program run itself or imported
if __name__ == '__main__':
    print("This program is run itself ")
else:
    print("Imported from another module ")
