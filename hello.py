from flask import Flask, render_template, request
from Backend_Functions import addItem, calculate_interest

import sqlite3

conn = sqlite3.connect('mydatabase.db')
c = conn.cursor()

c.execute('SELECT * FROM users')
users = c.fetchall()

for user in users:
    print(user)


app = Flask(__name__)
app.secret_key = 'mysecretkey'

@app.route('/')
def login():
    conn = sqlite3.connect('mydatabase.db')
    c = conn.cursor()
    
    c.execute('SELECT * FROM users')
    users = c.fetchall()
    return render_template('login.html', users=users)

@app.route('/signup')
def signup():
    return render_template('signup.html')

@app.route('/register', methods=['POST'])
def do_signup():
    username = request.form['username']
    password = request.form['password']

    # save the username and password to a file
    with open('users.txt', 'a') as file:
        file.write(f"{username}:{password}\n")

    return "Registration successful!"

@app.route('/login', methods=['POST'])
def do_login():
    username = request.form['username']
    password = request.form['password']

    # check if the username and password are correct by reading the file
    with open('users.txt', 'r') as file:
        users = file.readlines()

    for user in users:
        u, p = user.strip().split(':')
        if u == username and p == password:
            return render_template('index.html')

    return "Invalid username or password."

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/calculate', methods=['POST'])
def calculate():
    # Get user input from form
    present_value = float(request.form['present_value'])
    interest_rate = float(request.form['interest_rate'])
    years = int(request.form['years'])
    
    # Calculate future value
    future_value = present_value * (1 + interest_rate/100) ** years
    
    # Render the results template with the calculated value
    return render_template('result.html', result=future_value)


@app.route('/expenses', methods=['GET', 'POST'])
def expenses():
    if request.method == 'POST':
        name = request.form['name']
        amount = request.form['amount']
        frequency = request.form['frequency']
        
        conn = sqlite3.connect('money.db')
        c = conn.cursor()
        c.execute("INSERT INTO expenses (name, amount, frequency) VALUES (?, ?, ?)", (name, amount, frequency))
        conn.commit()
        conn.close()
        
        return redirect('/expenses')
    else:
        conn = sqlite3.connect('money.db')
        c = conn.cursor()
        c.execute("SELECT * FROM expenses")
        expenses = c.fetchall()
        conn.close()
        
        return render_template('expenses.html', expenses=expenses)

if __name__ == '__main__':
    app.run()
