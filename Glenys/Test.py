from flask import Flask, render_template, request
from werkzeug.security import generate_password_hash, check_password_hash

app = Flask(__name__)


users = {
    'user1': {'password': generate_password_hash('password1'), 'email': 'user1@example.com'},
    'user2': {'password': generate_password_hash('password2'), 'email': 'user2@example.com'}
}

@app.route('/', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']

        if username in users and check_password_hash(users[username]['password'], password):
            return f"Welcome, {username}!"
        else:
            return render_template('login.html', error='Invalid credentials. Please try again.')

    return render_template('login.html')

@app.route('/create_account', methods=['GET', 'POST'])
def create_account():
    if request.method == 'POST':
        username = request.form['new_username']
        password = request.form['new_password']
        email = request.form['email']

        if username not in users:
            # Using generate_password_hash to hash the password
            hashed_password = generate_password_hash(password)
            users[username] = {'password': hashed_password, 'email': email}
            return f"Account created successfully for {username}!"
        else:
            return render_template('create_account.html', error='Username already exists. Please choose another username.')

    return render_template('create_account.html')

@app.route('/forgot_password', methods=['GET', 'POST'])
def forgot_password():
    if request.method == 'POST':
        username = request.form['username']
        email = request.form['email']
        new_password = request.form['new_password']
        new_email = request.form['new_email']  # New field for the new email

        # Check if username and email match and reset the password
        found_user = None
        for user, info in users.items():
            if user == username and info['email'] == email:
                found_user = user
                break

        if found_user:
            # Using generate_password_hash to hash the new password only once
            hashed_password = generate_password_hash(new_password)
            users[found_user]['password'] = hashed_password  # Assign hashed_password here
            users[found_user]['email'] = new_email  # Update the email here
            return f"Password and email reset successfully for {found_user}!"
        else:
            return render_template('forgot_password.html', error='Invalid credentials.')

    return render_template('forgot_password.html')


@app.route('/view_user/<username>') #http://127.0.0.1:5000/view_user/Glenys
def view_user(username):
    if username in users:
        return f"Username: {username}, Email: {users[username]['email']}"
    else:
        return "User not found."

@app.route('/update_user/<username>', methods=['GET', 'POST'])
def update_user(username):
    if request.method == 'POST':
        new_password = request.form['new_password']
        new_email = request.form['new_email']

        if username in users:
            users[username]['password'] = generate_password_hash(new_password)
            users[username]['email'] = new_email
            return f"User {username} updated successfully!"
        else:
            return "User not found."

    return render_template('update_user.html', username=username)

@app.route('/delete_user/<username>')  #http://127.0.0.1:5000/delete_user/Glenys
def delete_user(username):
    if username in users:
        del users[username]
        return f"User {username} deleted successfully!"
    else:
        return "User not found."

if __name__ == '__main__':
    app.run(debug=True)



