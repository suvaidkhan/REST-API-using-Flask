from db import db
from flask_restful import Resource
from models.store import StoreModel


class Store(Resource):

    def get(self, name):
        data = StoreModel.find_by_name(name)
        if data is None:
            return {'message': 'Store not present'}, 404
        return data.json()

    def post(self, name):
        data = StoreModel.find_by_name(name)
        if data:
            return {'message': 'Store already exists'}
        store = StoreModel(name)
        store.store_to_db()
        return store.json()

    def delete(self, name):
        store = StoreModel.find_by_name()
        if store:
            store.delete_from_db()

        return {'message': 'Store has been deleted'}, 200

class StoreList(Resource):

    def get(self):
        return {'stores': [store.json() for store in StoreModel.query.all()]}

