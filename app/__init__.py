from app.app import api, app, login_manager
from app.models.usermodel import User
from app.views.Userregistration import userregister,userlogin
from app.views.orderitem import orderitem,orderupdate
login_manager.init_app(app)
@login_manager.user_loader
def load_user(user):
    """current user details"""
    return User.objects.get(id=user)
app.add_url_rule("/", view_func=userlogin, methods=["GET","POST"])
app.add_url_rule("/register",view_func=userregister,methods=["GET","POST"])
app.add_url_rule("/orderitem",view_func=orderitem,methods=["GET","POST"])
app.add_url_rule("/orderupdate",view_func=orderupdate,methods=["GET","POST"])