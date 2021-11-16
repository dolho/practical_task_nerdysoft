from flask import Flask, jsonify, redirect
from flasgger import Swagger
from app.blueprints.vocabulary_util.vocabulary_util import blueprint_vocabulary
import os

app = Flask(__name__)


app.register_blueprint(blueprint_vocabulary)

swagger = Swagger(app)



@app.route("/")
def index():
    return redirect("/apidocs")

@app.cli.command()
def setup():
    import app.blueprints.vocabulary_util.database_handler.tables.setup

if __name__ == "__main__":
    app.run()