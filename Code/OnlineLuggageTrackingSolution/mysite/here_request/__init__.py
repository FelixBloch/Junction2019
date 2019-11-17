from flask import Flask

# from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config['SECRET_KEY'] = '02d9899c28cdb5e02e51d942cbd8e848' 
# app.config['SQLACLHEMY_DATABASE_URI'] = 'sqlite:///site.db'
# db = SQLAlchemy(app)

from here_request import routes
