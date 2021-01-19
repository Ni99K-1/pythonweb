#!"C:\Users\Himanshu Hamal\AppData\Local\Programs\Python\Python35-32\python"

print ("content-type: text/html\n")
import cgi, cgitb,pymysql

form = cgi.FieldStorage()
ctype=form.getvalue('ctype')
searchtext= form.getvalue('searchtext')
stype= form.getvalue('stype')
minp=form.getvalue('minp')
maxp=form.getvalue('maxp')
print (stype)
print(searchtext)
print(minp)
print(maxp)
# def dbsql(sql):
# 	con=pymysql.connect(host='localhost',user='root', password='', db='bookstore')
# 	dbo=con.cursor()
# 	print(sql)
# 	dbo.execute(sql)
# 	rows=dbo.fetchall()
# 	for row in rows:
# 		print("<tr>")
# 		for elem in row:
# 			print("<td>")
# 			print (elem)
# 			print("</td>")


	
# print("""
# 	<html>
# 	<head><title></title></head>
# 	<body>
# 	<table>
# 	<thead>
# 	<th>Categories</th>
# 	<th>ISBN</th>
# 	<th>Title</th>
# 	<th>Publisher</th>
# 	<th>Author/Artist</th>
# 	<th>Price</th>
# 	<th>Quantity</th>
# 	</thead>
# 	<tbody>
# 	""")


# if (stype=='Publisher'):
# 	sql="Select `categories`,`isbn`,`title`,`publisher`,`author`,`price`,`quantity` from products where publisher='"+stext+"';"
# 	dbsql(sql)
				
# elif (stype=='Author'):
# 	sql="Select `categories`,`isbn`,`title`,`publisher`,`author`,`price`,`quantity` from products where author='"+stext+"';)"
# 	dbsql(sql)
	
# elif(stype=='Price'):
# 	sql="Select `categories`,`isbn`,`title`,`publisher`,`author`,`price`,`quantity` from products where price between "+minp+" and "+maxp+";"
# 	dbsql(sql)
# elif (stype=='Category'):
# 	sql="Select `categories`,`isbn`,`title`,`publisher`,`author`,`price`,`quantity` from products where categories='"+stext+"';)"
# 	dbsql(sql)
# elif (stype=='Title'):
# 	sql="Select `categories`,`isbn`,`title`,`publisher`,`author`,`price`,`quantity` from products where title='"+stext+"';)"
# 	dbsql(sql)


# print("""


# 	</tbody>
# 	</table>

# 	</body>
# 	</html>

# 	""")