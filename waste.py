#!/usr/bin/env python

import cgi
import MySQLdb


timeStr = "fdghfdhfd"
print """content-type: text/html

<!DOCTYPE html>
<html lang = "en-US">
 <body>
<p>The current Central date and time is:  {timeStr}</p>
 </body>
</html>



"""

