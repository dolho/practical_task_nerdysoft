from flask import Flask, jsonify
from flasgger import Swagger
from app.blueprints.vocabulary_util.vocabulary_util import blueprint_vocabulary
import os

app = Flask(__name__)


app.register_blueprint(blueprint_vocabulary)

swagger = Swagger(app)


def create_app():
    app = Flask(__name__)
    # app.register_blueprint(blueprint_user)
    # app.register_blueprint(blueprint_converter)
    app.register_blueprint(blueprint_vocabulary)
    swagger = Swagger(app)
    return app

@app.cli.command()
def setup():
    import app.blueprints.vocabulary_util.database_handler.tables.setup

if __name__ == "__main__":
    app.run()