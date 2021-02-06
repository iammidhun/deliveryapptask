from flask import Flask
from flask_restful import  Api
app = Flask(__name__)
app.secret_key = b'_5#y2L"Fjnmb\n\xec]/'
api = Api(app)