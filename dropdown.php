<html>
    <head>
        <title>Create dyanamic dropdown list in javascript</title>
        <meta http-equiv="Content-Type" content="text/html; charset=utf-8" />
    </head>
    <title>Dynamic Drop Down List</title>
    <body>
        < ?php
        $servername = "localhost";
        $username = "bda";
        $password = "bda";
        $dbname = "sw200";
        
        // Create connection
        $conn = new mysqli($servername, $username, $password, $dbname);
        // Check connection
        if ($conn->connect_error) {
            die("Connection failed: " . $conn->connect_error);
        }
        
        $sql = "SELECT * from language";
        $result = $conn->query($sql);
        
        $sqlFramework = "SELECT * FROM `framework`";
        $resultFramework = $conn->query($sqlFramework);
        $rowFrameworkResult = array();
        if ($resultFramework->num_rows > 0) {
            while($rowFramework = mysqli_fetch_assoc($resultFramework)) {
                $rowFrameworkResult[] = $rowFramework;
            }
        }
        ?>
        <div class="category_div" id="category_div">Please specify language:
            <select name="category" class="required-entry" id="category" onchange="javascript: dynamicdropdown(this.options[this.selectedIndex].value);">
                <option value="">Select Language</option>
                < ?php if ($result->num_rows > 0) { ?>
                    < ?php while($row = mysqli_fetch_assoc($result)) { ?>
                    <option value="<?php echo $row['id']; ?>">< ?php echo $row['name']; ?></option>
                    < ?php } ?>
                < ?php } ?>
            </select>
        </div>
        <script type='text/javascript'>
        
        </script>
        <div class="sub_category_div" id="sub_category_div">Please select framework:
            <script type="text/javascript" language="JavaScript">
                document.write('<select name="subcategory" id="subcategory"><option value="">Please select framework</option></select>')
            </script>
            <noscript>
                <select name="subcategory" id="subcategory">
                    <option value="">Please select framework</option>
                </select>
            </noscript>
        </div>
        <script language="javascript" type="text/javascript">
            var rowFrameworkResultInJs =< ?php echo json_encode($rowFrameworkResult);?>;
            function dynamicdropdown(listindex)
            {
                document.getElementById("subcategory").length = 0;
                document.getElementById("subcategory").options[0]=new Option("Please select framework","");
                if (listindex) {
                    var lookup = {};
                    var j = 1;
                    for (var i = 0, len = rowFrameworkResultInJs.length; i < len; i++) {
                        if (rowFrameworkResultInJs[i].lang_id == listindex) {
                            document.getElementById("subcategory").options[j]=new Option(rowFrameworkResultInJs[i].framework_name,rowFrameworkResultInJs[i].id);
                            j = j+1;
                        }
                    }
                }
                
                return true;
            }
       </script>
        < ?php $conn->close(); ?>
    </script></body>
</html>