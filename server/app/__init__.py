from flask import Flask
from .extensions import init_extentions
from .config import Config

'''Creating app '''
def create_app():
    app = Flask(__name__)
    app.config.from_object(Config)
    '''Registering Extentions'''
    init_extentions(app)

    '''Registering BluePrints'''
    from .routes.app.home import home_bp
    app.register_blueprint(home_bp, url_prefix = '/api/app/home')
    return app
    