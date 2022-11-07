import mysql.connector

firstname = "Sheila"
lastname = "Prunier"
street = "241 East Road"
city = "Hampstead"
st = "NH"
zip = "03841"

passwd = input("Enter the database password: ")

conn = mysql.connector.connect(host='FystemsMac02', database='homedata',user='lfister',password=passwd)
cursor = conn.cursor()

query = "SELECT * FROM people;"

cursor.execute(query)

for row in cursor.fetchall():
    print(row)

#conn.commit()
cursor.close()
conn.close()    
