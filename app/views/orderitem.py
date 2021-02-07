import uuid
from flask import jsonify,request,render_template,redirect, url_for
from flask_login import current_user
from app.models.usermodel import User
from app.models.orderdetailmodel import OrderDetails
def orderitem():
	if request.method == 'POST':
		itemname = request.form["itemname"]
		pickupaddress = request.form["pickupaddress"]
		newaddress = request.form["newaddress"]
		deliveryaddress = request.form.get("deliveryaddress")
		if  newaddress:
			user =  User.objects.get(id=current_user.id)
			deliveryaddresslist = user.deliveryaddress
			deliveryaddresslist.append(newaddress)
			user.deliveryaddress = deliveryaddresslist
			user.save()
			deliveryaddress = newaddress
		else:
			deliveryaddress=deliveryaddress
		uniqueuid = uuid.uuid4().hex
		OrderDetails.objects.create(itemname=itemname,
			pickupaddress=pickupaddress,deliveryaddress=deliveryaddress,
			ordereduser = current_user.id,orderid=uniqueuid)
		user =  User.objects.get(id=current_user.id)
		orderitems = OrderDetails.objects(ordereduser=current_user.id)
		return render_template("order.html",user=user,orderitems=orderitems)
	else:
		user =  User.objects.get(id=current_user.id)
		orderitems = OrderDetails.objects(ordereduser=current_user.id)
		return render_template("order.html",user=user,orderitems=orderitems)
	

