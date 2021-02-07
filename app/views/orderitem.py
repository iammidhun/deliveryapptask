from flask import jsonify,request,render_template,redirect, url_for
from flask_login import current_user
from app.models.usermodel import User
from app.models.orderdetailmodel import OrderDetails
def orderitem():
	if request.method == 'POST':
		itemname = request.form["itemname"]
		pickupaddress = request.form["pickupaddress"]
		deliveryaddresstype = request.form["pickupaddress"]
		deliveryaddress = request.form["deliveryaddress"]
		if  deliveryaddresstype == "new":
			user =  User.objects.get(id=current_user.id)
			deliveryaddresslist = user.deliveryaddress
			deliveryaddresslist.append(deliveryaddress)
			user.deliveryaddress = deliveryaddresslist
			user.save()
		
	

