import json

from flask import Flask, request
from flask_restful import Api, Resource

app = Flask(__name__)
api = Api(app)


class Vaccination(Resource):

    @staticmethod
    def get():
        name = request.args.get('name')

        database = open('database.json', 'r')

        data = json.load(database)

        if name in data.keys():
            certificate_dict = {'certificate': data[name]}
            response = app.response_class(
                response=json.dumps(certificate_dict),
                status=200,
                mimetype='application/json'
            )
            return response
        else:
            response = app.response_class(
                response=json.dumps("Error"),
                status=404,
                mimetype='application/json'
            )
            return response


api.add_resource(Vaccination, "/vaccination/")

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=9001)
