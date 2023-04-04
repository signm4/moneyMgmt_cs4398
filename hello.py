from flask import Flask, render_template, request

app = Flask(__name__)

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
            return render_template('hello.html')

    return "Invalid username or password."

if __name__ == '__main__':
    app.run()
