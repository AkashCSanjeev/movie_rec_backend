from flask import Flask
from flask_restful import Api
from Resource.model import Model



app=Flask(__name__)
api=Api(app)

# @app.before_first_request
# def create_table():
#     db.create_all()

api.add_resource(Model,'/predict')
# api.add_resource(StoreList,'/stores')



if __name__ == '__main__':
      app.run(host='10.10.25.39', port=1234,debug=True)