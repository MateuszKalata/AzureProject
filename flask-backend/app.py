from flask import Flask
from flask import request
from flask_cors import CORS
from flask import jsonify
import json

app = Flask(__name__)
cors = CORS(app, resources={r"/api/*": {"origins": "*"}})

from utils import Utils
utils = Utils()

@app.route("/")
def hello():
	return "Tu możemy serwować nasze API. Ta strona stoi na flasku, więc możemy w załadować model tutaj w plikach i zwracać to co zwraca model."
	
@app.route("/home")
def home():
	return "['Ala ma kota', 'Burek lubi piłkę']"

@app.route("/api/search")
def api_search():
	query = request.args.get('query')
	out = utils.search(query)
	print("out = ", str(out))
	# out = []
	# elem = {
	# 			"title" : 'a',
	# 			"paragraph" : 'b',
	# 			"url" : 'c',
	# 			"index" : 1
	# 		}
	# out.append(elem)
	# out.append(elem)
	return json.dumps(out)
	# return json.dumps([{
	#     "elo": "yes"
	# }])

