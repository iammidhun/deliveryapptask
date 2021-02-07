from app.app import db
from app.models.usermodel import User

class OrderDetails(db.Document):
	itemname = db.StringField(required=True)
	pickupaddress = db.StringField(required=True)
	ordereduser = db.ReferenceField(User)
	statusoforder = db.StringField()
	deliveryusername = db.StringField()
	locationofagent =  db.StringField()
	deliveryuserphoneno = db.StringField()
	orderid = db.StringField(required=True)