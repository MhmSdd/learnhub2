# config.py

import os

class Config:
    SQLALCHEMY_DATABASE_URI = 'mysql://root:@localhost/student_db'
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    SESSION_COOKIE_SAMESITE= 'Lax'
    SESSION_COOKIE_SECURE= True 
    SECRET_KEY = 'X7b9kL2mQz8pWvT3rYcN5jF0hG4iA9oD_eBxU6nM'
    LANGUAGES = {
        'en': 'English',
        'ar': 'Arabic'
    }

    BABEL_DEFAULT_LOCALE = 'en'
