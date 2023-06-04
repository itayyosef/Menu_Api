from db import db

class Category(db.Model): # represents a category that a dish can belong to
    id = db.Column(db.Integer,primary_key=True)
    category_name = db.Column(db.String(100),nullable=False,unique=True)
    image_url = db.Column(db.String(5000),nullable=False)
    dishes = db.relationship('Dish',backref='category')

    def serialize(self):
        return {
            "id":self.id,
            "category_name":self.category_name,
            "image_url":self.image_url,
            "dishes":[dish.serialize() for dish in self.dishes]
        }