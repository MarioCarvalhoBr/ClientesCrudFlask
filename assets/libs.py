import email_validator
from flask_wtf import FlaskForm
from wtforms import StringField
from wtforms.validators import DataRequired, Email
from wtforms import ValidationError
from wtforms import HiddenField
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from dotenv import load_dotenv
import os
import pipreqs
