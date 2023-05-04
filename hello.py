from flask import Flask, render_template, request, redirect, session, flash
from Backend_Functions import addExpense, addIncome, getExpenses, getIncome, getPrices, can_I_Spend_It
import os



app = Flask(__name__)
app.secret_key = 'mysecretkey'

@app.route('/')
def login():
    return render_template('login.html')

@app.route('/signup')
def signup():
    return render_template('signup.html')

@app.route('/register', methods=['POST'])
def do_signup():
    username = request.form['username']
    password = request.form['password']
    income = 0
    expenses = 0
    if add_user_data(username, password, income, expenses):

        print("account created, redirect to login")
        return redirect('/')
    else:
        flash('Username already exists, Try Again')
        print("username exits, redirect to /register") #debugging
        return redirect('/signup')
    
# old working signup 
# @app.route('/register', methods=['POST'])
# def do_signup():
#     username = request.form['username']
#     password = request.form['password']

#     # save the username and password to a file
#     with open('users.txt', 'a') as file:
#         file.write(f"{username}:{password}:{0}:{0}\n")

#     return render_template('login.html', username=username)

def get_all_usernames():
    # Open the user database file and read all lines
    with open('users.txt', 'r') as f:
        lines = f.readlines()

    # Extract the username from each line and return as a list
    usernames = [line.split(':')[0].strip() for line in lines]
    return usernames

def check_user_credentials(username, password):
    user_data = get_user_data(username)
    print(user_data) #debugging
    if user_data is not None and user_data['password'] == password:
        session['username'] = username
        session['income'] = user_data['income']
        session['expenses'] = user_data['expenses']
        return True
    return False


# def add_user_data(username, password, income, expenses):
#     # Check if the username is available
#     if username in get_all_usernames():
#         return False

#     # Create a new user data file
#     with open(f'{username}.txt', 'w') as f:
#         f.write(f'{password}\n')
#         f.write(f'{income}\n')
#         f.write(f'{expenses}\n')
    
#     return True

def add_user_data(username, password, income, expenses):
    if username in get_all_usernames():
        return False
    # Open the user database file in append mode
    with open('users.txt', 'a') as f:
        # Write the user data to a new line in the file
        f.write(f"{username}:{password}:{income}:{expenses}\n")
    return True

def get_user_data(username):
    print ("Current user: ",username) #debugging
    with open('users.txt', 'r') as f:
        for line in f:
            stored_username, stored_password, stored_income, stored_expenses = line.strip().split(':')
            if stored_username == username:
                return {'password':str(stored_password), 'income': float(stored_income), 'expenses': float(stored_expenses)}
    return None

# old login method via text file 
@app.route('/login', methods=['POST'])
def do_login():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']

    # check if the username and password are correct by reading the file
    # with open('users.txt', 'r') as file:
    #     users = file.readlines()

    # for user in users:
    #     u, p = user.strip().split(':')
    #     if u == username and p == password:
    #         return render_template('index.html', username=request.form['username'])

    # return "Invalid username or password."
        if check_user_credentials(username, password):
            session['username'] = username
            return redirect('/index')
        else:
            return 'Invalid username or password'

    # Show the login form
    return render_template('login.html')

@app.route('/logout')
def logout():
    # Clear the session data
    session.clear()

    # Redirect the user to the login page
    return redirect(('/'))

@app.route('/index')
def index():
    if 'username' not in session:
        return redirect('/login')

    # Get the user's data from the database
    username = session['username']
    user_data = get_user_data(username)
    income = getIncome(username)
    expenses = getExpenses(username)
    spend = getPrices(username)

    # Render the template with the user's data
    return render_template('index.html', username=username, user_data=user_data, income=income, expenses=expenses, spend=spend)

@app.route('/home')
def go_home():
    # username = session['username']
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
    username = session['username']
    user_data = get_user_data(username)
    if request.method == 'POST':
        # name = request.form['name']
        amount = request.form['amount']
        frequency = request.form['frequency']
        
        print("expenses ", username, " : ", amount, " : ", frequency) #debugging 
        addExpense(username, amount, frequency)
        flash("expense added")
        return redirect('/expenses')
    else:
        return render_template('expenses.html', expenses=expenses, username = username)
    
@app.route('/spend', methods = ['GET', 'POST'])
def spend():
    username = session['username']
    spend = getPrices(username)/12
    spend = float(spend)
    if request.method == 'POST':
        amount = request.form['amount']
        amount = float(amount)
        # spendx = can_I_Spend_It(username, amount)
        # print ("this is the backend function can i spend it: ", spendx)
        print("this is spend: ", spend)
        if (amount <= spend):
            flash("You are good to go, make sure to add this as a one time expense if you decide to spend it.")
        else:
            flash("You cannot spend more than you have")
    return render_template('spend.html', username = username, spend= spend)

@app.route('/income', methods = ['GET', 'POST'])
def income():
    username = session['username']
    if request.method == 'POST':
        amount = request.form['amount']
        frequency = request.form['frequency']
        print("Income ", username, " : ", amount, " : ", frequency, " sent to backend ") #debugging 
        addIncome(username, amount, frequency)
        flash("income added")

    return render_template('income.html', username = username)

# def get_expenses(username):
#     filename = username + ".txt"
#     with open(filename, "r") as file:
#         # Skip the first line (income)
#         next(file)
#         # Read the second line (expense)
#         expense = float(file.readline().strip())
#     return expense

# def get_income(username):
#     filename = username + ".txt"
#     with open(filename, "r") as file:
#         # Skip the first line (income)
#         # Read the second line (expense)
#         income = float(file.readline().strip())
#     return income

# def get_spend(username):
#     filename = username + ".txt"
#     with open(filename, "r") as file:
#         # Skip the first line (income)
#         next(file)
#         # Skip the second line (expense)
#         next(file)
#         # Read the third line (spend)
#         spend = float(file.readline().strip())
#     return spend

    
if __name__ == '__main__':
    app.run()
