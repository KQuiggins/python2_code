<html>
<head>
    <title>Add Trips</title>
    <style>
        body{
            background-color: #f2f2f2;
        }
        
    </style>
</head>
<body>
<h2>Add Trips</h2>
<form action="/new_trip" method="POST">
    <p><input type="text" name="name" placeholder="Username"> Username</p>
    <p><input type="text" name="date" placeholder="Date"> Date</p>
    <p><input type="text" name="destination" placeholder="Destination"> Destination</p>
    <p><input type="text" name="miles" placeholder="Miles"> Miles</p>
    <p><input type="text" name="gallons" placeholder="Gallons"> Gallons</p>
    <p><input value="Submit" type="submit" size="20"></p>
</form>
</body>
</html>