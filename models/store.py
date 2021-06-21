from db import db


class StoreModel(db.Model):
    __tablename__ = "Stores"
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(20))

    items = db.relationship('ItemModel', lazy='dynamic')

    def json(self):
        return {'name': self.name, 'items': [items.json() for items in self.items.all()]}

    def __init__(self, name):
        self.name = name

    def store_to_db(self):
        db.session.add(self)
        db.commit()

    def delete_from_db(self):
        db.session.add(self)
        db.commit()

    @classmethod
    def find_by_name(cls, name):
        return cls.query.filter_by(name=name).first()
