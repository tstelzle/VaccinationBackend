import json

from flask import Flask, request
from flask_restful import Api, Resource

app = Flask(__name__)
api = Api(app)


class Vaccination(Resource):

    def get(self):
        name = request.args.get('name')
        certificate = request.args.get('certificate')

        database = open('database.json', 'r')

        data = json.load(database)

        if name in data.keys():
            return data[name], 200
        else:
            return 'Name not found', 404

    def post(self):
        print('server2')

        return 'post'


api.add_resource(Vaccination, "/vaccination/")

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=9001)
