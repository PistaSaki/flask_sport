import os
from flask import Flask

def create_app(test_config=None):
    # create and configure the app
    app = Flask(__name__, instance_relative_config=True)
    app.config.from_mapping(
        SECRET_KEY='dev',
    )
    
    if test_config is None:
        # load the instance config, if it exists, when not testing
        app.config.from_pyfile("config.py", silent=True)
    else:
        app.config.from_mapping(test_config)
        
    # ensure the instande folder exists
    os.makedirs(app.instance_path, exist_ok=True)
    
    # a simple page that says hello
    @app.route('/hello')
    def hello():
        return 'Hello world!'
    
    from .blueprints import addition_blueprint
    app.register_blueprint(addition_blueprint.bp)
    
    return app