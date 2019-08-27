from flaskimport Flask

from .extentions import db, guard
from .models import User

def create_app():
    app = Flask(__name__)

    db.init_app((app))
    guard.init_app(app,User)


    return app