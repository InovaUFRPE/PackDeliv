import json
from flask import request, jsonify
from flask.views import MethodView
from viewHelper import register_view,app 


class CompanyView(MethodView):

    def get(self,id_company=None):
        return jsonify({"testeGet": id_company})
    
    def post(self):
        json = request.get_json()
        return jsonify({"testePost":json })
    
    def put(self,id_company):
        return jsonify({"testePut": id_company})
    
    def delete(self,id_company):
        return jsonify({"testeDElete": id_company})

endpoint='company_view'
methods=['GET','POST','PUT','DELETE']
url='/company/'
pk='id_company'
register_view(app,CompanyView,endpoint,url,methods,pk)


