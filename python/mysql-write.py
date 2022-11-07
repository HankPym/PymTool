import mysql.connector

passwd = input("Enter the database password: ")

conn = mysql.connector.connect(host='FystemsMac02', database='homedata',user='lfister',password=passwd)
cursor = conn.cursor()

firstname = "www"
lastname = "www"
labelname = ""
street = ""

city = ""
st = ""
zip = ""
email = ""
homephone = ""
cellphone = ""
workphone = ""

query = f"""INSERT INTO people (firstname,lastname,labelname,street,city,st,zip,email,homephone,cellphone,workphone)
    VALUES('{firstname}','{lastname}','{labelname}','{street}','{city}','{st}','{zip}','{email}','{homephone}','{cellphone}','{workphone}');"""

cursor.execute(query)

conn.commit()
cursor.close()
conn.close()

print(f"{firstname} {lastname} has been added to the people database")
