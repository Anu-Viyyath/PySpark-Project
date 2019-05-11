
	
//LoginForm.php
<!DOCTYPE HTML>
<html>
<head>
<title>LoginForm.php</title>
<!-- Using external stylesheet to make the registration form look attractive -->
<link rel = "stylesheet" type = "text/css" href="Style.css"/>
<!-- Javascript validation for user inputs -->
<script type="text/javascript">
 
function validate()
{
var username = document.login.username.value;
var password = document.login.password.value;
 
if (username==null || username=="")
{
  alert("Username can't be blank");
  return false;
}
else if (password==null || password=="")
{
  alert("password can't be blank");
  return false;
}
}
</script>
</head>
<body>
 
<!-- Make a note that the method type used is post, action page is Login.php and validate() function will get called on submit -->
<div style="text-align:center"><h1>PHP Login Form using MySQL</h1></div>
<br>
<form name="login" method="post" action="Login.php" onsubmit="return validate();" >
<div>Username: <input type="text" name="username" /> </div>
<div>Password: <input type="password" name="password" /> </div>
<div><input type="submit" value="Login"></input> <input type="reset" value="Reset"></input></div>
</form>
</body>
</html>