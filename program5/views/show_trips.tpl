<html>
<head>
    <title>Display Trips</title>
    <style>
        body{
            background-color: #f2f2f2;
        }

        h2{
            text-align: center;
            color: #2e6da4;
        }

        form{
            text-align: center;
        }
    </style>
</head>
<body>
<h2>Enter the name of the user to view their trips</h2>
<form action="/trips" method="POST">
   <p><input type="text" name="username" placeholder="Enter name"> Enter Name</p>
   <input type="submit" value="Submit">
</form>
</body>
</html>