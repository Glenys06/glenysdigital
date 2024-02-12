from flask import Flask, render_template, request, redirect, url_for, flash, jsonify
from Forms import CreateUserForm
import shelve, User
from flask import Flask, render_template

app = Flask(__name__)
app.secret_key = 'your_secret_key'  # Set a secret key for flash messagesv

chatbot_responses = {
    'business_info':
    "Welcome to Euphoric Delights! We take pride in providing delightful experiences through our ice cream creations.",
    'contact_info':
    "You can reach us at contact@euphoricdelights.com. Feel free to drop us an email anytime!",
    'product_info':
    "Indulge in the extraordinary taste of Euphoric Delights! Our signature product, 'Euphoria Bliss,' is a favorite among our customers.",
    'opening_hours':
    "We are open every day from 10 AM to 8 PM. Visit us to savor the magic of our ice creams!",
    'hi':
    "Hello there! 👋 Welcome to Euphoric Delights. I'm Scoopy, your virtual ice cream assistant.",
    'current_flavours':
    "Explore our current flavors, including classic chocolate, vanilla bean, and exciting seasonal varieties!",
    'special_promotions':
    "Discover our special promotions! Join our loyalty program for exclusive discounts and sweet surprises."
}


@app.route('/')
def home():
  return render_template('home.html')


@app.route('/chatbot')
def chatbot():
  welcome_message = (
      "Hello there! 👋 I'm Scoopy, your virtual ice cream assistant.\n"
      "How can I assist you today?\n"
      "Ask about our current flavors!\n"
      "Explore our menu!\n"
      "Learn about special promotions!\n"
      "Place an order for pickup or delivery!")

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
        "Email: contact@euphoricdelights.com. Contact number: +65 9898 9111")

  return jsonify({'bot_response': bot_response})


@app.route('/createUser', methods=['GET', 'POST'])
def create_user():
  create_user_form = CreateUserForm(request.form)
  if request.method == 'POST' and create_user_form.validate():
    users_dict = {}
    db = shelve.open('user.db', 'c')

    try:
      users_dict = db['Users']
    except:
      print("Error in retrieving Users from user.db.")

    user = User.User(create_user_form.first_name.data,
                     create_user_form.last_name.data,
                     create_user_form.gender.data,
                     create_user_form.email_address.data,
                     create_user_form.feedback.data)
    users_dict[user.get_user_id()] = user
    db['Users'] = users_dict

    # Test codes
    users_dict = db['Users']
    user = users_dict[user.get_user_id()]
    print(user.get_first_name(), user.get_last_name(),
          "was stored in user.db successfully with user_id ==",
          user.get_user_id())

    db.close()

    flash('YOUR FORM HAS BEEN SUBMITTED!', 'success')  # Flash success message
    return redirect(
        url_for('create_user'))  # Redirect back to the createUser route

  return render_template('createUser.html', form=create_user_form)


@app.route('/retrieveUsers')
def retrieve_users():
  users_dict = {}
  db = shelve.open('user.db', 'r')
  users_dict = db['Users']
  db.close()

  users_list = []
  for key in users_dict:
    user = users_dict.get(key)
    users_list.append(user)  # Adjusted indentation

  return render_template('retrieveUsers.html',
                         count=len(users_list),
                         users_list=users_list)


@app.route('/updateUser/<int:id>/', methods=['GET', 'POST'])
def update_user(id):
  update_user_form = CreateUserForm(request.form)
  if request.method == 'POST' and update_user_form.validate():
    users_dict = {}
    db = shelve.open('user.db', 'w')
    users_dict = db['Users']
    user = users_dict.get(id)

    user.set_first_name(update_user_form.first_name.data)
    user.set_last_name(update_user_form.last_name.data)
    user.set_gender(update_user_form.gender.data)
    user.set_email_address(update_user_form.email_address.data)
    user.set_feedback(update_user_form.feedback.data)
    db['Users'] = users_dict
    db.close()

    return redirect(url_for('retrieve_users'))
  else:
    users_dict = {}
    db = shelve.open('user.db', 'r')
    users_dict = db['Users']
    db.close()
    user = users_dict.get(id)
    update_user_form.first_name.data = user.get_first_name()
    update_user_form.last_name.data = user.get_last_name()
    update_user_form.gender.data = user.get_gender()
    update_user_form.email_address.data = user.get_email_address()
    update_user_form.feedback.data = user.get_feedback()
    return render_template('updateUser.html', form=update_user_form)


@app.route('/deleteUser/<int:id>', methods=['POST'])
def delete_user(id):
  users_dict = {}

  db = shelve.open('user.db', 'w')
  users_dict = db['Users']

  users_dict.pop(id)

  db['Users'] = users_dict
  db.close()

  return redirect(url_for('retrieve_users'))


if __name__ == '__main__':
  app.run()
