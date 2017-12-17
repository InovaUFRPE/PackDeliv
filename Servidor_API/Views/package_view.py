import json
from flask import request, jsonify
from flask.views import MethodView
from viewHelper import register_view,app 




class PackageView(MethodView):

    def get(self,id_package=None):
        return jsonify({"testeGet": id_package})
    
    def post(self):
        return jsonify({"testePost": "123"})
    
    def put(self,id_package):
        return jsonify({"testePut": id_package})
    
    def delete(self,id_package):
        return jsonify({"testeDElete": id_package})

endpoint='package_view'
methods=['GET','POST','PUT','DELETE']
url='/package/'
pk='id_package'
register_view(app,PackageView,endpoint,url,methods,pk)
