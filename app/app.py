from flask import Flask
from flask_mongoengine import MongoEngine
from flask_restful import  Api
app = Flask(__name__)
app.config["MONGODB_SETTINGS"] = {
	"db":"deliveryapp",
	"host":"localhost",
	"port":27017
}
app.secret_key = b'_5#y2L"Fjnmb\n\xec]/'
api = Api(app)