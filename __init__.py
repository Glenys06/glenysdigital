from flask import Flask, render_template, request, redirect, url_for
from Forms import CreateUserForm, CreateCustomerForm
import shelve, User, Customer
import sqlite3, os
from sqlite3 import Error

app = Flask(__name__)
def home():
    return render_template('home.html')
if __name__ == '__main__':
    app.run()