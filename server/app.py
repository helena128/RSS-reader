
from flask import Flask, request, jsonify
from flask_cors import CORS, cross_origin

app = Flask(__name__)
cors = CORS(app)
app.config['CORS_HEADERS'] = 'Content-Type'

@app.route('/src')
@cross_origin()
def getSources():
	return "hi"

if __name__ == '__main__':
	app.run(port = 8000)