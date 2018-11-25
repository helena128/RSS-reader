from flask import Flask, request, jsonify, Response
from flask_cors import CORS, cross_origin
import json
import service

app = Flask(__name__)
cors = CORS(app)
app.config['CORS_HEADERS'] = 'Content-Type'

@app.route('/rss', methods = ['GET'])
@cross_origin()
def get_all_rss():
	rss_id = request.args.get('id')
	if not rss_id:
		result = service.get_all_rss()
	else:
		result = service.get_rss_info(rss_id)
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

@app.route('/total', methods = ['GET'])
@cross_origin()
def get_number_of_feeds():
	rss_id = request.args.get('id')
	return Response(service.get_number_of_feeds(rss_id))

if __name__ == '__main__':
	app.run(port = 8000)