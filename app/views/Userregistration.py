#for user signup
from app.models.usermodel import User
from flask_restful import Resource
from flask import jsonify,request,render_template
def userlogin():
	return render_template('login.html')

def useregister():
	username = request.form["username"]
	userpassword = request.form["userpassword"]
	usermailid = request.form["usermailid"]
	userrole = request.form["userrole"]
	deliveryaddress = request.form["deliveryaddress"]
	userphoneno = request.form["userphoneno"]
	User.objects.create(username=username,userpassword=userpassword
		usermailid=usermailid,userrole=userrole,
		deliveryaddress=deliveryaddress,userphoneno=userphoneno)
	return ("success")