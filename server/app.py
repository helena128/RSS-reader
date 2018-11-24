from flask import Flask, request, jsonify, Response
from flask_cors import CORS, cross_origin
import json
import service

app = Flask(__name__)
cors = CORS(app)
app.config['CORS_HEADERS'] = 'Content-Type'

@app.route('/topics')
@cross_origin()
def get_all_rss():
	result = service.get_all_rss()
	return Response(result, mimetype = 'application/json')

@app.route('/feeds')
@cross_origin()
def get_all_feeds():
	source = request.args.get('source')
	page = request.args.get('page')
	size = request.args.get('size')
	print(source + " " + page + " " + size)
	result = service.get_feeds(source, size, page)
	return Response(result, mimetype = 'application/json')

@app.route('/rss', methods = ['POST'])
@cross_origin()
def add_rss():
	link = request.form('link')
	return Response(service.get_all_rss())

if __name__ == '__main__':
	app.run(port = 8000)