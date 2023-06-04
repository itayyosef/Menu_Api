from flask import Flask,request
from flask_restful import Api

from controllers.categories import CategoryAll
from controllers.dishes import DishesAll

from flask_cors import CORS
from db import db
app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = "sqlite:///db.sqlite3"
CORS(app)
db.init_app(app)
api = Api(app)

with app.app_context():
    db.create_all()

api.add_resource(DishesAll,'')

api.add_resource()
if __name__ == '__main__':
    app.run(debug=True)