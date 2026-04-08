from flask import Flask
from flask_migrate import Migrate
from flask_login import LoginManager
from models import db
from config import config
from routes.itineraries_blueprint import itineraries_bp
from routes.auth_blueprint import auth_bp

def create_app(config_name='default'):
    app = Flask(__name__, template_folder='templates')

    # Load configuration
    app.config.from_object(config[config_name])

    # Initialize database
    db.init_app(app)

    # Initialize Flask-Migrate
    migrate = Migrate(app, db)

    # Initialize Flask-Login
    login_manager = LoginManager()
    login_manager.init_app(app)
    login_manager.login_view = 'auth.login'

    @login_manager.user_loader
    def load_user(user_id):
        from models import User
        return User.query.get(int(user_id))

    # Register blueprints
    app.register_blueprint(itineraries_bp)
    app.register_blueprint(auth_bp)

    # Create database tables
    with app.app_context():
        db.create_all()

    return app

# For development server
if __name__ == '__main__':
    app = create_app('development')
    app.run(debug=True)
