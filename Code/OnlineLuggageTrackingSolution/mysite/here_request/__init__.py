from flask import Flask


app = Flask(__name__)
app.config['SECRET_KEY'] = '02d9899c28cdb5e02e51d942cbd8e848' 

from here_request import routes
