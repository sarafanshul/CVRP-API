import numpy as np

class Data :
    points = []
    depot = []
    num_vehicles = 0 
    vehicle_cap = []
    demands = []

    def __init__(self , _num_vehicles , _depot , locations , _vehicle_cap , _demands ):
        self.points = locations # [ [x , y] , [x , y] .. ]
        self.depot = _depot # [ [ x , y ] ]
        self.demands = _demands 
        self.vehicle_cap = _vehicle_cap
        self.num_vehicles = _num_vehicles

    def merge(self , a , b ):
        return a + b 

    def get_distance(self , p1 , p2 ): # manhattan distance , modify as per use
        return abs( p1[0] - p2[0] ) + abs( p1[1] - p2[1] ) 

    def generate_distance_matrix(self , locations ):
        n = len(locations)
        res = np.zeros( shape = (n , n) )
        for i in range( n ):
            for j in range( n ):
                if( i != j ): res[i][j] = self.get_distance( locations[i] , locations[j] )
        return res 

    def create_data_model(self):
        locations = self.merge( self.depot , self.points )
        distance_matrix = self.generate_distance_matrix( locations )
        
        data = {}
        data['distance_matrix'] = distance_matrix
        data['demands'] = self.demands
        data['vehicle_capacities'] = self.vehicle_cap
        data['num_vehicles'] = self.num_vehicles
        data['depot'] = 0 # at idx 0 in locations
        return data
