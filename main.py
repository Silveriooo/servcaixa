from flask_login import login_user, logout_user
from app import app, db, admin
from app.models import User
from flask_admin.contrib.sqla import ModelView

admin.add_view(ModelView(User, db.session))

app.run(debug=True)