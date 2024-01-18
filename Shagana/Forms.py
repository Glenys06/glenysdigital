from wtforms import Form, StringField, SelectField, TextAreaField, validators, EmailField


class CreateUserForm(Form):
    first_name = StringField('First Name', [validators.Length(min=1, max=150), validators.DataRequired()])
    last_name = StringField('Last Name', [validators.Length(min=1, max=150), validators.DataRequired()])
    gender = SelectField('Gender', [validators.DataRequired()], choices=[('', 'Select'), ('F', 'Female'), ('M', 'Male')],
    default='')
    email_address = EmailField('Email', [validators.Email(), validators.DataRequired()])
    feedback = TextAreaField('FeedbacK', [validators.Optional()])