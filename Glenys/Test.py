from flask import Flask, render_template, request, redirect, url_for, session
from werkzeug.security import generate_password_hash, check_password_hash
from flask import flash

app = Flask(__name__)

# Set the secret key for session management
app.secret_key = 'your_secret_key_here'

users = {
    'user1': {'password': generate_password_hash('password1'), 'email': 'user1@example.com'},
    'user2': {'password': generate_password_hash('password2'), 'email': 'user2@example.com'}
}


# ... (rest of your code)


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

def is_password_strong(password):
    # Check if the password is strong (at least 8 characters, includes both letters and numbers)
    return len(password) >= 8 and any(char.isalpha() for char in password) and any(char.isdigit() for char in password)

@app.route('/create_account', methods=['GET', 'POST'])
def create_account():
    if request.method == 'POST':
        username = request.form['new_username']
        password = request.form['new_password']
        email = request.form['email']

        # Validate password strength
        if not is_password_strong(password):
            return render_template('create_account.html', error='Weak password. Password should be at least 8 characters long and include both letters and numbers.')

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
        new_email = request.form['new_email']

        # Validate password strength
        if not is_password_strong(new_password):
            error_message = 'Weak password. Password should be at least 8 characters long and include both letters and numbers.'
            return render_template('forgot_password.html', error=error_message)

        # Check if username and email match and reset the password
        found_user = None
        for user, info in users.items():
            if user == username and info['email'] == email:
                found_user = user
                break

        if found_user:
            # Using generate_password_hash to hash the new password only once
            hashed_password = generate_password_hash(new_password)
            users[found_user]['password'] = hashed_password
            users[found_user]['email'] = new_email
            return f"Password and email reset successfully for {found_user}!"
        else:
            return render_template('forgot_password.html', error='Invalid credentials.')

    return render_template('forgot_password.html')


@app.route('/view_user/<username>')  # http://127.0.0.1:5000/view_user/Glenys
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


@app.route('/delete_user/<username>')  # http://127.0.0.1:5000/delete_user/Glenys
def delete_user(username):
    if username in users:
        del users[username]
        return f"User {username} deleted successfully!"
    else:
        return "User not found."


@app.route('/about_us')
def about_us():
    return render_template('about_us.html')


# Products Page
@app.route('/products')
def products():
    # Define your products here. Each product is a dictionary with keys for 'name', 'description', 'price', and 'image'.
    products = [
        {
            'id': '1',
            'name': 'Vanilla Ice Cream',
            'description': 'A classic flavor made with real vanilla beans.',
            'price': '5.00',
            'image': 'https://www.benjerry.com.sg/files/live/sites/systemsite/files/US%20and%20Global%20Assets/Flavors/Product%20Assets/US/Vanilla%20Ice%20Cream/web_Tower_Vanilla_RGB_HR2_60M.png'
        },
        {
            'id': '2',
            'name': 'Chocolate Chip Cookie Dough',
            'description': 'Vanilla ice cream with chunks of chocolate chip cookie dough.',
            'price': '6.00',
            'image': 'https://www.mingoicecream.com.sg/wp-content/uploads/2017/12/MGOscoop_chocochip-hi.png'
        },
        {
            'id': '3',
            'name': 'Strawberry Swirl',
            'description': 'Creamy ice cream with a decadent sweet strawberry swirl.',
            'price': '5.50',
            'image': 'https://scoopjackandremi.com/cdn/shop/files/JR_Strawberry-Szn-Garnish.png?v=1695712997'
        },
        {
            'id': '4',
            'name': 'Mango Delight',
            'description': ' A tropical delight with rich, fruity sweetness in every scoop.',
            'price': '5.50',
            'image': 'https://www.mingoicecream.com.sg/wp-content/uploads/2017/12/MGOscoop_mango-hi.png'
        }
        # Add more products as needed
    ]

    # Pass the products to the template
    return render_template('products.html', products=products)


# Define your products as a list of dictionaries
products = [
    {'id': '1', 'name': 'Vanilla Ice Cream', 'price': '5.00'},
    {'id': '2', 'name': 'Chocolate Chip Cookie Dough', 'price': '6.00'},
    {'id': '3', 'name': 'Strawberry swirl', 'price': '5.50'},
    {'id': '4', 'name': 'Mango Delight', 'price': '5.50'},  # Changed id from '3' to '4'
]


# Function to get product details by ID
def get_product_details(product_id):
    for product in products:
        if product['id'] == product_id:
            return {
                'id': product['id'],
                'name': product['name'],
                'price': product['price'],
            }
    return None

  @app.route('/add_to_cart', methods=['POST'])
  def add_to_cart():
      # Get the list of selected products
      selected_products = request.form.getlist('product')

      # If no product is selected, flash an error message and redirect back to the products page
      if not selected_products:
          flash('Please select at least one product.')
          return redirect(url_for('products'))

      # Clear the existing cart in the session
      session.pop('cart', None)

      # Initialize the cart in the session if not already present
      session.setdefault('cart', [])

      # Iterate over each product in the form data
      for product_id in selected_products:
          quantity = int(request.form.get('quantity_' + product_id, 1))

          # Ensure the quantity is within the allowed limit
          max_quantity = 20
          if quantity < 1 or quantity > max_quantity:
              quantity = max_quantity

          # Fetch the product details based on product_id
          product_details = get_product_details(product_id)

          if product_details:
              # Check if the product is already in the cart
              for item in session['cart']:
                  if str(item['id']) == str(product_id):
                      item['quantity'] += quantity
                      item['total_price'] = item['quantity'] * float(item['price'])
                      break
              else:
                  # If the product is not in the cart, add it
                  session['cart'].append({
                      'id': product_id,
                      'name': product_details['name'],
                      'quantity': quantity,
                      'price': product_details['price'],
                      'total_price': quantity * float(product_details['price']),
                      # Add other product details as needed
                  })

      return redirect(url_for('cart'))

@app.route('/cart')
def cart():
    # Retrieve cart items from the session
    # Retrieve cart items from the session
    cart_items = session.get('cart', [])

    # Calculate the total price
    total_price = sum(item['total_price'] for item in cart_items)

    print("session['cart']:", session.get('cart'))
    print("cart_items:", cart_items)
    return render_template('cart.html', cart_items=cart_items,total_price=total_price)


if __name__ == '__main__':
    app.run(debug=True)
