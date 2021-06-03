import json 
import random
from CVRP import CVRP

LONG_TO_FLOAT_CONST = 1000000

def main():
	latlng = []
	with open( "in.json" , "r" ) as F :
		data = json.load(F)
		for v in data :
			latlng.append( ( int((float(v['lat']) *LONG_TO_FLOAT_CONST)) , int((float(v['lng']) * LONG_TO_FLOAT_CONST)) ) )
			# latlng.append( (float(v['lat']) , float(v['lng'])) )

	_locations = latlng[1:20:]
	_depot = latlng[0:1]
	_demands = [ random.randint(1 , 10) for _ in range( len(_locations) ) ]

	_num_vehicles = 10
	_vehicle_cap = [ random.randint(10 , 20) for _ in range( _num_vehicles ) ]

	solver = CVRP( _num_vehicles , _depot , _locations , _vehicle_cap , _demands )
	print( solver.cvrpConstrained( 7 ) )


if __name__ == '__main__':
	main()