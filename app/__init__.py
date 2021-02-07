from app.app import api, app
from app.views.Userregistration import userregister,userlogin
app.add_url_rule("/", view_func=userlogin, methods=["GET","POST"])
app.add_url_rule("/register",view_func=userregister,methods=["POST"])
