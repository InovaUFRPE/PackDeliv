import json
from flask import request, jsonify
from flask.views import MethodView
from Views.viewHelper import register_view
from Models.DB.DB_helper import Company, Address, model_from_dict
from Rest_utils.entities_atributes_Names import *
from Controlers.company_control import CompanyControl

class CompanyView(MethodView):
    
    def get(self,id_company=None):
        if id_company == None:
            return jsonify({"error": "Please provide a id_company"}), 400

        try:
            company = CompanyControl.find(id_company)
            if company == None:
                return jsonify({"error": "No company found with id " + str(id_company)}), 404
            else:
                return jsonify(company.as_dict()), 200
        except ValueError as error:
            return jsonify({"error": str(error)}), 500

    def post(self):
        json = request.get_json()
        if json == None:
            return jsonify({"error": "Please provide a JSON"}), 400

        company = model_from_dict(Company, json)
        company.addresses = [model_from_dict(Address, dic) for dic in json['addresses']]
        missing_fields = CompanyView.validate_required_fields_presence(company)

        if len(missing_fields) != 0:
            return jsonify({"error": "Missing fields:" + str(missing_fields)}), 400

        try:
            id_company = CompanyControl.register(company)
            return jsonify({ "id": id_company }), 200
        except ValueError as error:
            return jsonify({"error": str(error)}), 500

    def put(self,id_company=None):
        json = request.get_json()
        if json == None:
            return jsonify({"error": "Please provide a JSON"}), 400
        if id_company == None:
            return jsonify({"error": "Please provide a id_company"}), 400

        company = model_from_dict(Company, json)
        company.addresses = [model_from_dict(Address, dic) for dic in json['addresses']]
        company.id = id_company

        try:
            success = CompanyControl.update(company)
            if success == True:
                return jsonify({"id": id_company}), 200
            else:
                return jsonify({"error": "Unable to update Company with id " + str(id_company)}), 500
        except ValueError as error:
            return jsonify({"error": str(error)}), 500

    def delete(self,id_company=None):
        if id_company == None:
            return jsonify({"error": "Please provide a id_company"}), 400

        try:
            if CompanyControl.delete(id_company) == True:
                return jsonify({"id": id_company}), 200
            else:
                return jsonify({"error": "No company found with id " + str(id_company)}), 404
        except ValueError as error:
            return jsonify({"error": str(error)}), 400

    @staticmethod
    def validate_required_fields_presence(company):
        missing_fields = []
        if company.name == None:
            missing_fields.append('name')
        if company.password == None:
            missing_fields.append('password')
        if company.login == None:
            missing_fields.append('login')
        if company.email == None:
            missing_fields.append('email')
        if company.uci == None:
            missing_fields.append('uci')

        return missing_fields


def initialize_view(app):
    endpoint='company_view'
    methods=['GET','POST','PUT','DELETE']
    url='/company/'
    pk='id_company'
    register_view(app,CompanyView,endpoint,url,methods,pk)
