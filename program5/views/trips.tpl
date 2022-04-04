<html>
<head>
    <title>Trips</title>
    <style>
        body{
            background-color: #f2f2f2;
        }

        table{
            border-collapse: collapse;
            width: 100%;
            color: #588c7e;
            font-family: monospace;
            font-size: 25px;
            text-align: left;
            margin-top: 50px;
        }

    </style>
</head>
<body>
<table cellspacing="8">
<tr>
    <th>Username</th>
    <th>Date</th>
    <th>Destination</th>
    <th>Miles</th>
    <th>Gallons Used</th>
</tr>
%for row in rows:
    <tr>
    %for col in row:
        <td>{{col}}</td>
    %end
    </tr>
%end
</table>
</body>
</html>