from flask import Flask , jsonify ,make_response , request
from flask_restful import Api , Resource , reqparse
from CVRP import VRP , CVRP

app = Flask( __name__ )

@app.route("/vrp" , methods = ['POST' , 'PUT'])
def vrp():
	try :
		values = request.json
		solver = VRP( values['vCount'] , values['depot'] , 
			values['locations'] , values['vCap'] , [] )
		res = solver.vrpNoConstraints( 1 )
		return jsonify( res ) , 200
	except :
		return jsonify( {} ) , 400

@app.route("/cvrp" , methods = ['POST' , 'PUT'])
def cvrp():
	try :
		values = request.json
		solver = CVRP( values['vCount'] , values['depot'] , 
			values['locations'] , values['vCap'] , values['demands'] )
		res = solver.cvrpConstrained( 1 )
		return jsonify( res ) , 200
	except :
		return jsonify( {} ) , 400

def main():
	app.run(  )

if __name__ == '__main__':
	main()