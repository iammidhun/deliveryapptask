from app.app import db
from app.models.usermodel import User

class OrderDetails(db.Document):
	itemname = db.StringField(required=True)
	pickupaddress = db.StringField(required=True)
	ordereduser = db.ReferenceField(User)