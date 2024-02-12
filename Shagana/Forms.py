from wtforms import Form, StringField, SelectField, TextAreaField, validators, EmailField
from wtforms.validators import Regexp


class CreateUserForm(Form):
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
