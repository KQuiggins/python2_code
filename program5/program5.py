import sqlite3
from bottle import route, run, template, request, response


@route('/', method="GET")
def index():
    return template('login_page')  # initial login page


@route('/login', method='POST')
def login():
    user = request.forms.get("username")  # get username
    password = request.forms.get("password")  # get password

    # create a database connection and cursor
    conn = sqlite3.connect("travel_expenses.db")
    cur = conn.cursor()
    sql = "SELECT * FROM members WHERE username = ? AND password = ?"

    cur.execute(sql, (user, password))
    result = cur.fetchone()
    cur.close()

    if (result):
        return template('welcome')
    else:
        m = {'msg': "login failed"}
        return template('status', m)


@route('/display_trips', method='GET')
def display_trips():

    return template('show_trips')


@route('/trips', method='POST')
def trips():
    user = request.forms.get("username")  # get username
    conn = sqlite3.connect("travel_expenses.db")
    cur = conn.cursor()
    sql = "SELECT username, date, destination, miles, gallons FROM trips WHERE username = ?"
    cur.execute(sql, (user, ))
    result = cur.fetchall()
    print(result)
    cur.close()
    return template('trips', rows=result)


@route('/add_trips', method='GET')
def add_trip():
    return template('add_trips')


@route('/new_trip', method='POST')
def new_trip():
    record = []
    record.append(request.forms.get('name'))
    record.append(request.forms.get('date'))
    record.append(request.forms.get('destination'))
    record.append(request.forms.get('miles'))
    record.append(request.forms.get('gallons'))
    print(record)

    conn = sqlite3.connect("travel_expenses.db")
    cur = conn.cursor()
    sql = "INSERT  INTO trips (username, date, destination, miles, gallons) VALUES(?, ?, ?, ?, ?)"
    cur.execute(sql, record)
    conn.commit()
    cur.close()
    return template('trip_status', msg="Trip added successfully")


run(host='localhost', port=8080, debug=True)
