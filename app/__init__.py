from app.app import api, app
from app.views.Userregistration import userregister
app.add_url_rule("/", view_func=userregister, methods=["GET","POST"])