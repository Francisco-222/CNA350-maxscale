
# References From
# https://mariadb.com/resources/blog/how-to-connect-python-programs-to-mariadb/
# https://www.w3schools.com/python/python_mysql_select.asp
# https://www.geeksforgeeks.org/connect-to-mysql-using-pymysql-in-python/
# And previous assingment from CNA 330
import pymysql
conn = pymysql.connect(user="maxuser",
                       passwd="maxpwd",
                       port=4006,
                       host="192.168.56.112")
cur = conn.cursor()


cur.execute("SELECT * FROM zipcodes_two.zipcodes_two ORDER BY Zipcode LIMIT 1")
data1 = cur.fetchall()
cur.execute("SELECT * FROM zipcodes_one.zipcodes_one ORDER BY Zipcode DESC LIMIT 1")
data2 = cur.fetchall()
cur.execute("SELECT * FROM zipcodes_two.zipcodes_two LIMIT 10")
data3 = cur.fetchall()
cur.execute("SELECT * FROM zipcodes_one.zipcodes_one LIMIT 9990,10")
data4 = cur.fetchall()

for data in data1,\
            data2, \
            data3, \
            data4:
    print(data)

conn.close()
