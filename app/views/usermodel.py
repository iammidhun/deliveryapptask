#for user and delivery user databse
from app.app import db

class User(db.Document):
	username = db.StringFiled(required=True)
	usermailid = db.StringFiled(required=True)
	userrole = db.StringFiled(required=Truddddddde)
	userpassword = db.StringFiled(required=True)
	deliveryaddress = db.StringFiled()
	userphoneno = db.StringFiled(required=True)
