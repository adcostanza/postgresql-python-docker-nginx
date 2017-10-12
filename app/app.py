from flask import Flask, request, jsonify
from flask_restful import reqparse, Resource, Api
from show_schedule import airing_shows

from db import DB

app = Flask(__name__)
api = Api(app)

def options(self):
    pass
	
class Airing(Resource):
	def get(self):
		episodes = airing_shows()
		return jsonify(episodes)
		
class DBTest(Resource):
	def post(self,txt):
		db = DB()
		db.addPost(txt,1)
		return jsonify(success=True)
class DBTestList(Resource):
	def get(self):
		db = DB()
		return jsonify(db.getAllLinks())
api.add_resource(Airing,'/airing/')
api.add_resource(DBTest,'/db/<txt>')
api.add_resource(DBTestList,'/db/')

if __name__ == '__main__':
     app.run(host='0.0.0.0', port=8080)
    