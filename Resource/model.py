from flask_restful import Resource,reqparse
import pickle,numpy as np
from flask import Response




list = []
class Model(Resource):

    def get(self):
        popular_df = pickle.load(open('popularMovies.pkl','rb'))
        
        return Response(popular_df.to_json())

