from wtforms import Form, StringField, RadioField, SelectField, TextAreaField, validators
from wtforms.fields import EmailField, DateField, SelectField, IntegerField
from wtforms.validators import Regexp
class CreateUserForm(Form):
    first_name = StringField('First Name', [validators.Length(min=1, max=150), validators.DataRequired()])
    last_name = StringField('Last Name', [validators.Length(min=1, max=150), validators.DataRequired()])
    gender = SelectField('Gender', [validators.DataRequired()], choices=[('', 'Select'), ('F', 'Female'), ('M', 'Male')],
    default='')
    membership = RadioField('Membership', choices=[('F', 'Fellow'), ('S', 'Senior'), ('P', 'Professional')], default='F')
    remarks = TextAreaField('Remarks', [validators.Optional()])
class CreateCustomerForm(Form):
    first_name = StringField('First Name', [validators.Length(min=1, max=150), validators.DataRequired()])
    last_name = StringField('Last Name', [validators.Length(min=1, max=150), validators.DataRequired()])
    gender = SelectField('Gender', [validators.DataRequired()], choices=[('', 'Select'), ('F', 'Female'), ('M', 'Male')], default='')
    email = EmailField('Email', [validators.Email(), validators.DataRequired()])
    date_joined = DateField('Date Joined', format='%Y-%m-%d')
    address = TextAreaField('Mailing Address', [validators.length(max=200), validators.DataRequired()])
    membership = RadioField('Membership', choices=[('F', 'Fellow'), ('S', 'Senior'), ('P', 'Professional')], default='F')
    remarks = TextAreaField('Remarks', [validators.Optional()])
class CustomFlavourCreator(Form):
    creationBase1 = RadioField('Base Flavour', choices=[('01', 'Vanilla'), ('02', 'Chocolate'), ('03', 'Strawberry'), ('04', 'Mint'), ('05', 'Blue Moon')], default='01')
    creationMixIn1 = RadioField('Mix-In', choices=[('01', 'Almonds'), ('02', 'Walnuts'), ('03', 'Pistachios')], default='01')
    creationTopping1 = RadioField('Topping', choices=[('01', 'Maple Syrup'), ('02', 'Strawberry Syrup'), ('03', 'Butterscotch Syrup'), ('04', 'Blueberry Syrup'), ('05', 'Chocholate Syrup')], default='01')
class CreateOrderForm(Form):
    flavour = SelectField('Flavour', [validators.DataRequired()], choices=[('', 'Select'), ('01', 'Velvety Vanilla'), ('02', 'Cotton Candy Carnival'), ('03', 'Pomegranate Punch'), ('04', 'Blueberry Blast'), ('05', 'Chocolate Convergence')], default='')
    scoops = IntegerField('Scoops', [validators.NumberRange(min=1, max=5)])
    serving_vessel = RadioField('Serving Vessel', choices=[('B', 'Cup/Bowl'), ('C', 'Cone')], default='B')
    remarks = TextAreaField('Remarks', [validators.Optional()])
class CreateContactForm(Form):
  first_name = StringField('First Name', [
      validators.Length(min=1, max=150),
      validators.DataRequired(),
      Regexp('^[a-zA-Z]*$', message='Only alphabetical characters allowed')
  ])
  last_name = StringField('Last Name', [
      validators.Length(min=1, max=150),
      validators.DataRequired(),
      Regexp('^[a-zA-Z]*$', message='Only alphabetical characters allowed')
  ])
  gender = SelectField('Gender', [validators.DataRequired()],
                       choices=[('', 'Select'), ('F', 'Female'),
                                ('M', 'Male')],
                       default='')
  email_address = EmailField(
      'Email',
      [validators.Email(), validators.DataRequired()])
  feedback = TextAreaField('FeedbacK', [validators.Optional()])

class CreateReviewsForm(Form):
    first_name = StringField('First Name', [validators.Length(min=1, max=150), validators.DataRequired()])
    last_name = StringField('Last Name', [validators.Length(min=1, max=150), validators.DataRequired()])
    date_of_review = DateField('Date of Review', format='%Y-%m-%d')
    remarks = TextAreaField('Review', [validators.Optional()])