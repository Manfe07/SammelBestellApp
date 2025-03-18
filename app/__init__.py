from flask import Flask, render_template

from app.config import Config
from app.extensions import db

def create_app(config_class=Config):
    app = Flask(__name__)
    app.config.from_object(config_class)

    # Initialize Flask extensions here

    # Register blueprints here
    from app.module_main import bp as main_bp
    app.register_blueprint(main_bp)

    @app.route('/test')
    def test():
        return render_template('test.html')


    return app