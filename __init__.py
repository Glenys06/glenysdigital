from flask import Flask, render_template, request, redirect, url_for, flash, jsonify,session
from Forms import CreateOrderForm, CreateContactForm#, CustomFlavourCreator
from werkzeug.security import generate_password_hash, check_password_hash
import shelve, Orders, Contact#, FlavourCreator

app = Flask(__name__)
app.secret_key = 'your_secret_key_here'

users = {
    'user1': {'password': generate_password_hash('password1'), 'email': 'user1@example.com'},
    'user2': {'password': generate_password_hash('password2'), 'email': 'user2@example.com'}
}

@app.route('/')
def home():
    return render_template('home.html')

'''
@app.route('/createOrder', methods=['GET', 'POST'])
def create_order():
    create_order_form = CreateOrderForm(request.form)
    if request.method == 'POST' and create_order_form.validate():
        orders_dict = {}
        db = shelve.open('static/database/orders.db', 'c')
        try:
            orders_dict = db['Orders']
        except:
            print("Error in retrieving Orders from user.db.")
        order = Orders.Orders(create_order_form.flavour.data, create_order_form.scoops.data, create_order_form.serving_vessel.data,create_order_form.remarks.data)
        orders_dict[order.get_order_id()] = order
        db['Orders'] = orders_dict
        db.close()
        return redirect(url_for('retrieve_orders'))
    return render_template('createOrder.html', form=create_order_form)
@app.route('/retrieveOrders')
def retrieve_orders():
    {}
    db = shelve.open('static/database/orders.db', 'r')
    orders_dict = db['Orders']
    db.close()
    orders_list = []
    for key in orders_dict:
        order = orders_dict.get(key)
        orders_list.append(order)
    return render_template('retrieveOrders.html', count=len(orders_list), orders_list=orders_list)
@app.route('/updateOrder/<int:id>/', methods=['GET', 'POST'])
def update_order(id):
    update_order_form = CreateOrderForm(request.form)
    if request.method == 'POST' and update_order_form.validate():
        orders_dict = {}
        db = shelve.open('static/database/orders.db', 'w')
        orders_dict = db['Orders']
        order = orders_dict.get(id)
        order.set_flavour(update_order_form.flavour.data)
        order.set_scoops(update_order_form.scoops.data)
        order.set_serving_vessel(update_order_form.serving_vessel.data)
        order.set_remarks(update_order_form.remarks.data)
        db['Orders'] = orders_dict
        db.close()
        return redirect(url_for('retrieve_orders'))
    else:
        db = shelve.open('static/database/orders.db', 'r')
        orders_dict = db['Orders']
        db.close()
        order = orders_dict.get(id)
        update_order_form.flavour.data = order.get_flavour()
        update_order_form.scoops.data = order.get_scoops()
        update_order_form.serving_vessel.data = order.get_serving_vessel()
        update_order_form.remarks.data = order.get_remarks()
        return render_template('updateOrder.html', form=update_order_form)
@app.route('/deleteOrder/<int:id>', methods=['POST'])
def delete_order(id):
    orders_dict = {}
    db = shelve.open('/static/database/orders.db', 'w')
    orders_dict = db['Orders']
    orders_dict.pop(id)
    db['Orders'] = orders_dict
    db.close()
    return redirect(url_for('retrieve_orders'))
'''
@app.route('/chatbot')
def chatbot():
    welcome_message = (
        "Hello there! 👋 I'm Scoopy, your delectable virtual ice cream assistant.\n"
        "How can I assist you today on your search for the sweetest treat?\n"
        "Ask about our growing list of delicious flavors!\n"
        "Explore our delightful menu!\n"
        "Learn about special scrumptious promotions!\n"
        "Place a mouthwatering order for pickup or delivery!"
    )

    return render_template('chatbot.html', welcome_message=welcome_message)


@app.route('/ask_chatbot', methods=['POST'])
def ask_chatbot():
    user_message = request.form['user_message']
    # Add your automatic chatbot responses here

    if 'business info' in user_message:
        bot_response = chatbot_responses['business_info']
    elif 'contact info' in user_message:
        bot_response = chatbot_responses['contact_info']
    elif 'product info' in user_message:
        bot_response = chatbot_responses['product_info']
    elif 'opening hours' in user_message:
        bot_response = chatbot_responses['opening_hours']
    elif 'hi' in user_message.lower():
        bot_response = chatbot_responses['hi']
    elif 'current flavors' in user_message.lower():
        bot_response = chatbot_responses['current_flavours']
    elif 'special promotions' in user_message.lower():
        bot_response = chatbot_responses['special_promotions']
    else:
        bot_response = (
            "I'm sorry, I didn't understand that. Please reach out to our staff for further details! Thank you. "
            "Email: contact@euphoricdelights.com. Contact number: +65 9898 9111"
        )

    return jsonify({'bot_response': bot_response})

chatbot_responses = {
    'business_info': "Welcome to Euphoric Delights! We take pride in providing delightful experiences through our ice cream creations.",
    'contact_info': "You can reach us at contact@euphoricdelights.com. Feel free to drop us an email anytime!",
    'product_info': "Indulge in the extraordinary taste of Euphoric Delights! Our signature product, 'Euphoria Bliss,' is a favorite among our customers.",
    'opening_hours': "We are open every day from 10 AM to 8 PM. Visit us to savor the magic of our ice creams!",
    'hi': "Hello there! 👋 Welcome to Euphoric Delights. I'm Scoopy, your virtual ice cream assistant.",
    'current_flavours': "Explore our current flavors, including classic chocolate, vanilla bean, and exciting seasonal varieties!",
    'special_promotions': "Discover our special promotions! Join our loyalty program for exclusive discounts and sweet surprises."
}
@app.route('/contactUs', methods=['GET', 'POST'])
def create_contact():
    create_contact_form = CreateContactForm(request.form)
    if request.method == 'POST' and create_contact_form.validate():
        contacts_dict = {}
        db = shelve.open('static/database/contact.db', 'c')

        try:
            contacts_dict = db['Contacts']
        except:
            print("Error in retrieving Contacts from contact.db.")

        contact = Contact.Contact(create_contact_form.first_name.data, create_contact_form.last_name.data,
                         create_contact_form.gender.data, create_contact_form.email_address.data,
                         create_contact_form.feedback.data)
        contacts_dict[contact.get_contact_id()] = contact
        db['Contacts'] = contacts_dict

        # Test codes
        contacts_dict = db['Contacts']
        contact = contacts_dict[contact.get_contact_id()]
        print(contact.get_first_name(), contact.get_last_name(),
              "was stored in static/database/contact.db successfully with contact_id ==", contact.get_contact_id())

        db.close()

        flash('YOUR FORM HAS BEEN SUBMITTED!', 'success')  # Flash success message
        return redirect(url_for('create_contact'))  # Redirect back to the createContact route


    return render_template('createContact.html', form=create_contact_form)



@app.route('/retrieveContacts')
def retrieve_contacts():
    contacts_dict = {}
    db = shelve.open('static/database/contact.db', 'r')
    contacts_dict = db['Contacts']
    db.close()

    contacts_list = []
    for key in contacts_dict:
        contact = contacts_dict.get(key)
        contacts_list.append(contact)  # Adjusted indentation

    return render_template('retrieveContacts.html', count=len(contacts_list), contacts_list=contacts_list)

@app.route('/updateContact/<int:id>/', methods=['GET', 'POST'])
def update_contact(id):
    update_contact_form = CreateContactForm(request.form)
    if request.method == 'POST' and update_contact_form.validate():
        contacts_dict = {}
        db = shelve.open('static/database/contact.db', 'w')
        contacts_dict = db['Contacts']
        contact = contacts_dict.get(id)

        contact.set_first_name(update_contact_form.first_name.data)
        contact.set_last_name(update_contact_form.last_name.data)
        contact.set_gender(update_contact_form.gender.data)
        contact.set_email_address(update_contact_form.email_address.data)
        contact.set_feedback(update_contact_form.feedback.data)
        db['Contacts'] = contacts_dict
        db.close()

        return redirect(url_for('retrieve_contacts'))
    else:
        contacts_dict = {}
        db = shelve.open('static/database/contact.db', 'r')
        contacts_dict = db['Contacts']
        db.close()
        contact = contacts_dict.get(id)
        update_contact_form.first_name.data = contact.get_first_name()
        update_contact_form.last_name.data = contact.get_last_name()
        update_contact_form.gender.data = contact.get_gender()
        update_contact_form.email_address.data = contact.get_email_address()
        update_contact_form.feedback.data = contact.get_feedback()
        return render_template('updateContact.html', form=update_contact_form)

@app.route('/deleteContact/<int:id>', methods=['POST'])
def delete_contact(id):
    contacts_dict = {}

    db = shelve.open('static/database/contact.db', 'w')
    contacts_dict = db['Contacts']

    contacts_dict.pop(id)

    db['Contacts'] = contacts_dict
    db.close()

    return redirect(url_for('retrieveContacts'))
@app.route('/mission')
def mission():
    return render_template('mission.html')

@app.errorhandler(404) 
def not_found(e):
    return render_template("404.html")


@app.route('/login', methods=['GET', 'POST']) 
def login():
  
  message = ''  # Initialize message
  login_successful = False  # Initialize login_successful
  
  if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']

        if username in users and check_password_hash(users[username]['password'], password):
          message = f"Welcome, {username}! Redirecting to the homepage in 5 seconds..."
          login_successful = True
        else:
            return render_template('login.html', error='Invalid credentials. Please try again.')

  return render_template('login.html',message=message, login_successful=login_successful)

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


# Products Page
@app.route('/products')
def products():
    # Define your products here. Each product is a dictionary with keys for 'name', 'description', 'price', and 'image'.
    products = [
        {
            'id': '1',
            'name': 'Velvety Vanilla',
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
        },
        {
            'id': '5',
            'name': 'Blueberry Blast',
            'description': 'A blissful frozen treat with a burst of fruity sweetness.',
            'price': '5.50',
            'image': 'https://www.mingoicecream.com.sg/wp-content/uploads/2017/12/MGOscoop_blueberry-hi.png'
        },
        {
            'id': '6',
            'name': 'Cotton Candy Carnival',
            'description': 'A velvety indulgence that captures the whimsy of carnival joy in every bite.',
            'price': '5.50',
            'image': 'https://www.fnncreameries.com/wp-content/uploads/2020/02/132-1.png'
        },
        {
            'id': '7',
            'name': 'Pomegranate Punch',
            'description': 'Invigorating fusion of juicy pomegranate that packs a delightful punch in every scoop.',
            'price': '5.50',
            'image': 'https://brandsitesplatform-res.cloudinary.com/image/fetch/w_auto:100,c_scale,q_auto:eco,f_auto,fl_lossy,dpr_auto,e_sharpen:85/https://assets.brandplatform.generalmills.com%2F-%2Fmedia%2Fproject%2Fgmi%2Fhaagendazs%2Fhaagendazs-master%2Fbsp%2Fhd%2Fproduct-images%2Fscoops%2Fraspberry-sorbet-v2.png%3Frev%3Da4eebb90257f41248024154e5b234b39'
        },
        {
            'id': '8',
            'name': 'Mint',
            'description': 'Refreshing bite of mint herbal with a tad bit of sweetness.',
            'price': '5.50',
            'image': 'https://www.mingoicecream.com.sg/wp-content/uploads/2017/12/MGOscoop_mintchoco-hi.png'
        }

        # Add more products as needed
    ]

    # Pass the products to the template
    return render_template('products.html', products=products)


# Define your products as a list of dictionaries
products = [
    {'id': '1', 'name': 'Velvety Vanilla', 'price': '5.00'},
    {'id': '2', 'name': 'Chocolate Chip Cookie Dough', 'price': '6.00'},
    {'id': '3', 'name': 'Strawberry swirl', 'price': '5.50'},
    {'id': '4', 'name': 'Mango Delight', 'price': '5.50'}, 
    {'id': '5', 'name': 'Blueberry Blast', 'price': '5.50'},
    {'id': '6', 'name': 'Cotton Candy Carnival', 'price': '5.50'},
    {'id': '7', 'name': 'Pomegranate Punch', 'price': '5.50'},
    {'id': '8', 'name': 'Mint', 'price': '5.50'},
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
  
@app.route('/payment', methods=['GET', 'POST'])
def payment():
    # You can handle payment processing logic here
    return render_template('payment.html')
  
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
  app.run(host='0.0.0.0')
