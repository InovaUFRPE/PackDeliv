import json
from flask import request, jsonify
from flask.views import MethodView
from viewHelper import register_view

class DeliveryView(MethodView):

    def get(self,id_delivery=None):
        return jsonify({"testeGet": id})
    #def post(self):
        #return jsonify({"testePost": "123"})
    def put(self,id_delivery):
        return jsonify({"testePut": id})
    def delete(self,id_delivery):
        return jsonify({"testeDElete": id})

def initializeView(app):
    endpoint='delivery_view'
    methods=['GET','PUT','DELETE']
    url='/delivery/'
    pk='id_delivery'
    register_view(app,DeliveryView,endpoint,url,methods,pk)
