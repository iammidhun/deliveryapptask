#for user signup
from app.models.usermodel import User
from flask_restful import Resource
from flask import jsonify,request,render_template,redirect, url_for
def userlogin():
	return render_template('login.html')

def userregister():
	if request.method == 'POST':
		username = request.form["username"]
		userpassword = request.form["userpassword"]
		usermailid = request.form["usermailid"]
		userrole = request.form["userrole"]
		deliveryaddress = request.form["deliveryaddress"]
		userphoneno = request.form["userphoneno"]
		print(request.form)
		User.objects.create(username=username,userpassword=userpassword,
			usermailid=usermailid,userrole=userrole,
			deliveryaddress=deliveryaddress,userphoneno=userphoneno)
		return redirect(url_for('userlogin'))
	else:
		return render_template('register.html')