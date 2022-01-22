from flask import Flask
from flask_restful import Resource, Api

app = Flask(__name__)
api = Api(app)


class HelloWorld(Resource):
    def get(self):
        return {'hello': 'world'}

    def post(self, name):
        return {"name": name}

    def put(self, name):
        return {"name": name}

    def delete(self, name):
        return {"name": name}


api.add_resource(HelloWorld, '/get', endpoint="get")
api.add_resource(HelloWorld, '/post/<string:name>', endpoint="post")
# api.add_resource(HelloWorld, '/put/<string:name>', endpoint="put")
# api.add_resource(HelloWorld, '/delete/<string:name>', endpoint="delete")

if __name__ == '__HelloWorld__':
    app.run(debug=True)


