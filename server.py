from flask import Flask,request
from controllers.categories import CategoryAll
from controllers.dishes import DishesAll
from flask_restful import Api
from flask_cors import CORS
from db import db

app = Flask(__name__)

app.config['SQLALCHEMY_DATABASE_URI'] = f'postgresql+psycopg2://itayyosef:Python_Project@restaurant-db.postgres.database.azure.com/postgres'
app.config['SECRET_KEY'] = 'asdf87sd6gf978fg3457gf39084fh7349028fh902fjdsa'
CORS(app)
db.init_app(app)
api = Api(app)

with app.app_context():
    db.create_all()

api.add_resource(DishesAll,'/dishes')
api.add_resource(CategoryAll,'/categories')

if __name__ == '__main__':
    app.run(debug=True,host="0.0.0.0")