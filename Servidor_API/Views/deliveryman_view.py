import json
from flask import request, jsonify
from flask.views import MethodView
from viewHelper import register_view,app 
 




class DeliverymanView(MethodView):

    def get(self,id_deliveryman=None):
        return jsonify({"testeGet": id_deliveryman})
    def post(self):
        return jsonify({"testePost": "123"})
    def put(self,id_deliveryman):
        return jsonify({"testePut": id_deliveryman})
    def delete(self,id_deliveryman):
        return jsonify({"testeDElete": id_deliveryman})

endpoint='deliveryman_view'
methods=['GET','POST','PUT','DELETE']
url='/deliveryman/'
pk='id_deliveryman'
register_view(DeliverymanView,endpoint,url,methods,pk)
