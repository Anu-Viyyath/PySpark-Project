#!/usr/bin/env python

import cgi
import MySQLdb

print """content-type: text/html

                                   
<!DOCTYPE HTML PUBLIC "-//W3C//DTD HTML 4.01 Transitional//EN" "http://www.w3.org/TR/html4/loose.dtd">
<html>
<head>
<meta http-equiv="Content-Type" content="text/html; charset=iso-8859-1">
<title>This is a test</title>
<script language="javascript" type="text/javascript">
function getPath() {
var inputName = document.getElementById('file1');
var imgPath;

imgPath = inputName.value;
document.getElementById('file_src').value = imgPath;
}
</script>
</head>

<body>
<form name="frm_upload" method="post" action="<?php echo $_SERVER['PHP_SELF']; ?>" onSubmit="getPath();">
<input name="file1" type="file"><br>
<input name="file_src" type="hidden" value="">
<input name="btn_submit" type="submit" value="show path">
</form>
<?php
	echo stripslashes($_POST["file_src"]);
?>
</body>
</html>





  

"""
print history
