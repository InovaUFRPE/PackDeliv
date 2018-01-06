import json
from flask import request, jsonify
from flask.views import MethodView
from viewHelper import register_view

class ServiceOrderView(MethodView):

    def get(self,id_service_order=None):
        return jsonify({"testeGet": id_service_order})
    #def post(self):
        #return jsonify({"testePost": "123"})
    def put(self,id_service_order):
        return jsonify({"testePut": id_service_order})
    def delete(self,id_service_order):
        return jsonify({"testeDElete": id_service_order})

def initializeView(app):
    endpoint='service_order_view'
    methods=['GET','PUT','DELETE']
    url='/service_order/'
    pk='id_service_order'
    register_view(app,ServiceOrderView,endpoint,url,methods,pk)
