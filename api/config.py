from flask import Flask 
from flask_sqlalchemy import SQLAlchemy
from flasgger import Swagger
from docs_api.swagger import SWAGGER_CONFIG, SWAGGER_TEMPLATE

app = Flask(__name__)

Swagger(app, template=SWAGGER_TEMPLATE, config=SWAGGER_CONFIG)

app.config['HOST'] = '0.0.0.0'
app.config['PORT'] = 8000
app.config['DEBUG'] = True

app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://postgres:Az1310750412@177.81.186.211:5432/escola'

db = SQLAlchemy(app)