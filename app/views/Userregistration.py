#for user signup
from app.models.usermodel import User
from flask_restful import Resource
from flask import jsonify,request,render_template
def userregister():
	return render_template('login.html')
