#for user and delivery user databse
from app.app import db

class User(db.Document):
	username = db.StringField(required=True)
	usermailid = db.StringField(required=True)
	userrole = db.StringField(required=True)
	userpassword = db.StringField(required=True)
	deliveryaddress = db.StringField()
	userphoneno = db.StringField(required=True)
