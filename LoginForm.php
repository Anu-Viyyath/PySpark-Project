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

//Style.css
/* Sample CSS - Modify it as per your taste */
input[type=text], input[type=password] {
background-color: #EEEEEE;
border: none;
color: black;
width:auto;
padding: 8px 52px;
text-decoration: none;
margin: 4px 2px;
cursor: pointer;
}
 
input[type=button], input[type=submit], input[type=reset] {
background-color: #4CAF50;
border: none;
color: white;
padding: 16px 32px;
text-decoration: none;
margin: 4px 2px;
cursor: pointer;
}
 
body{&nbsp;
text-align:right;&nbsp; &nbsp;
margin: 50px 400px;
}