from flask import Flask, render_template, request, redirect, session
from Backend_Functions import addItem, calculate_interest

# import sqlite3

# conn = sqlite3.connect('mydatabase.db')
# c = conn.cursor()

# c.execute('SELECT * FROM users')
# users = c.fetchall()

# for user in users:
#     print(user)


app = Flask(__name__)
# app.secret_key = 'mysecretkey'

@app.route('/')
def login():
    # conn = sqlite3.connect('mydatabase.db')
    # c = conn.cursor()
    
    # c.execute('SELECT * FROM users')
    # users = c.fetchall()
    return render_template('login.html')

@app.route('/signup')
def signup():
    return render_template('signup.html')

# @app.route('/signup', methods=['GET', 'POST'])
# def do_signup():
#     if request.method == 'POST':
#         username = request.form['username']
#         password = request.form['password']
#         conn = sqlite3.connect('mydatabase.db')
#         c = conn.cursor()
#         c.execute('INSERT INTO users (username, password) VALUES (?, ?)', (username, password))
#         conn.commit()
#         conn.close()
#         session['username'] = username
#         return redirect('/')
#     else:
#         return '''
#             <form method="post">
#                 <input type="text" name="username" placeholder="Username">
#                 <input type="password" name="password" placeholder="Password">
#                 <button type="submit">Sign Up</button>
#             </form>
#         '''

@app.route('/register', methods=['POST'])
def do_signup():
    username = request.form['username']
    password = request.form['password']

    # save the username and password to a file
    with open('users.txt', 'a') as file:
        file.write(f"{username}:{password}\n")

    return "Registration successful!"

# old login method via text file 
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
            return render_template('index.html', username=request.form['username'])

    return "Invalid username or password."

# @app.route('/login', methods=['GET', 'POST'])
# def do_login():
#     if request.method == 'POST':
#         username = request.form['username']
#         password = request.form['password']
#         print("USERNAME ", username)
#         print("PASSWORD ", password)
#         conn = sqlite3.connect('mydatabase.db')
#         c = conn.cursor()
#         c.execute('SELECT * FROM users WHERE username = ? AND password = ?', (username, password))
#         user = c.fetchone()
#         conn.close()
#         if user is not None:
#             session['username'] = user[1]
#             return redirect('/')
#         else:
#             return 'Invalid username or password'
#     else:
#         return '''
#             <form method="post">
#                 <input type="text" name="username" placeholder="Username">
#                 <input type="password" name="password" placeholder="Password">
#                 <button type="submit">Log In</button>
#             </form>
#         '''

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
        
        # conn = sqlite3.connect('money.db')
        # c = conn.cursor()
        # c.execute("INSERT INTO expenses (name, amount, frequency) VALUES (?, ?, ?)", (name, amount, frequency))
        # conn.commit()
        # conn.close()
        
        return redirect('/expenses')
    else:
        # conn = sqlite3.connect('money.db')
        # c = conn.cursor()
        # c.execute("SELECT * FROM expenses")
        # expenses = c.fetchall()
        # conn.close()
        
        return render_template('expenses.html', expenses=expenses)
    
@app.route('/spend', methods = ['GET', 'POST'])
def spend():
    if request.method == 'POST':
        amount = request.form['amount']

    return render_template('spend.html')

@app.route('/income', methods = ['GET', 'POST'])
def income():
    if request.method == 'POST':
        amount = request.form['amount']
        frequency = request.form['frequency']

    return render_template('income.html')
    
if __name__ == '__main__':
    app.run()
