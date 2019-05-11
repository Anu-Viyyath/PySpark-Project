#!/usr/bin/env python

import cgi
import MySQLdb

print """content-type: text/html

<html>
 <head>
<meta charset="utf-8"/>
  <title>CSV File to HTML Table Using AJAX jQuery</title>
  <script src="https://ajax.googleapis.com/ajax/libs/jquery/3.1.0/jquery.min.js"></script>
  <link rel="stylesheet" href="https://maxcdn.bootstrapcdn.com/bootstrap/3.3.6/css/bootstrap.min.css" />
  <script src="https://maxcdn.bootstrapcdn.com/bootstrap/3.3.7/js/bootstrap.min.js"></script>
 </head>
<script>
$(document).ready(function(){
 $('#load_data').click(function(){
  $.ajax({
   url:"/usr/lib/cgi-bin/Project/employee.csv",
   dataType:"text",
   success:function(data)
   {
    var employee_data = data.split(/\r?\n|\r/);
    var table_data = '<table class="table table-bordered table-striped">';
    for(var count = 0; count<employee_data.length; count++)
    {
     var cell_data = employee_data[count].split(",");
     table_data += '<tr>';
     for(var cell_count=0; cell_count<cell_data.length; cell_count++)
     {
      if(count === 0)
      {
       table_data += '<th>'+cell_data[cell_count]+'</th>';
      }
      else
      {
       table_data += '<td>'+cell_data[cell_count]+'</td>';
      }
     }
     table_data += '</tr>';
    }
    table_data += '</table>';
    $('#employee_table').html(table_data);
   }
  });
 });
 
});
</script>
 <body>
  <div class="container">
   <div class="table-responsive">
    <h1 align="center">CSV File to HTML Table Using AJAX jQuery</h1>
    <br />
    <div align="center">
     <button type="button" name="load_data" id="load_data" class="btn btn-info">Load Data</button>
    </div>
    <br />
    <div id="employee_table">
    </div>
   </div>
  </div>
 </body>
</html>





  

"""
