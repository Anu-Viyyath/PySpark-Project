#! usr/local/bin/python
import cgi;
import cgitb;
import Cookie;
import os;
import sqlite3;

cgitb.enable()
username= None
form= cgi.FieldStorage()

#open connection
conn= sqlite3.connect("manager.db")
cur= conn.cursor()

pagehead= """
    <html>
        <head> Redirecting </head>
        <body>

            """
pagefoot="""<form method= POST action="http://localhost:8000/cgi-bin/page1.py">
            <p> Validated! <input type="submit" value="Enter"/> </p>
            </form>
        </body>
    </html> """
errorpagefoot= """
<form action="http://localhost:8000/cgi-bin/index.py">
<p> Error! <input type="submit" value="Go Back"/> </p>
</form>
</body>
</html>"""


userName= form.getvalue('usernameLogin')
userPW= form.getvalue('passwordLogin')
userPWDatabase = conn.execute("SELECT username,passwrd FROM login WHERE username=? and passwrd=?",[userName,userPW])
cur.fetchone()
for result in userPWDatabase:
    userDb= result[0]
    pwDb= result[1]
    if userDb == userName and pwDb == userPW:
        #Create Cookie
        C= Cookie.SimpleCookie()
        #take the value of usernameLogin into the variable username
        username= form.getvalue('usernameLogin')
        #Set-Cookie header with the usernameLogin key
        C['usernameLogin'] = username
        print C
    elif userDb != userName and pwDb != userPW:
        print errorpagefoot

print "Content_type: text/html\n\n"
print pagehead
if username:
    print pagefoot
else:
    print errorpagefoot

