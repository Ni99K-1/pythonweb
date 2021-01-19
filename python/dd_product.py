#!"C:\Users\Himanshu Hamal\AppData\Local\Programs\Python\Python35-32\python"

print ("content-type: text/html\n")
import cgi, cgitb,pymysql

form = cgi.FieldStorage()
title = form.getvalue('title')
isbn=form.getvalue('isbn')
categories=form.getvalue('category')
authors=form.getvalue('author')
publisher=form.getvalue('publisher')
quantity=form.getvalue('quantity')
price=form.getvalue('price')
image=form.getvalue('image')
print(title,isbn,categories,authors,publisher,quantity,price)
# con=pymysql.connect(host='localhost',user='root', password='', db='bookstore')
# dbo=con.cursor()
# sql="insert into products (title,isbn,author,publisher,categories,price,quantity) values('"+title+"','"+isbn+"','"+authors+"','"+publisher+"','"+categories+"','"+price+"','"+quantity+"');"
# # print(sql)
# dbo.execute(sql)
# con.commit()
# print("""
# 	<script>
# 	window.location.href='../maintain.py';
# 	</script>
# 	</body>
# 	</html>


# 	""")