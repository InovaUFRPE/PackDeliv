import json
from flask import request, jsonify
from flask.views import MethodView
from viewHelper import register_view,app 




class VehicleView(MethodView):

    def get(self,id_vehicle=None):
        return jsonify({"testeGet": id_vehicle})
    #def post(self):
        #return jsonify({"testePost": "123"})
    def put(self,id_vehicle):
        return jsonify({"testePut": id_vehicle})
    def delete(self,id_vehicle):
        return jsonify({"testeDElete": id_vehicle})

endpoint='vehicle_view'
methods=['GET','PUT','DELETE']
url='/vehicle/'
pk='id_vehicle'
register_view(app,VehicleView,endpoint,url,methods,pk)
