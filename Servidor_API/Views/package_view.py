import json
from flask import request, jsonify
from flask.views import MethodView
from Views.viewHelper import register_view
from sqlalchemy import inspect
from Models.DB.DB_helper import Package, model_from_dict, model_as_dict
from Rest_utils.entities_atributes_Names import *
from Controlers.package_control import PackageControl

class PackageView(MethodView):
    def get(self,id_package=None):
        if id_package == None:
            return jsonify({"error": "Please provide a id_package"}), 400

        try:
            package = PackageControl.find(id_package)
            if package == None:
                return jsonify({"error": "No package found with id " + str(id_package)}), 404
            else:
                return jsonify(package.as_dict()), 200
        except ValueError as error:
            return jsonify({"error": str(error)}), 500

    def post(self):
        json = request.get_json()
        if json == None:
            return jsonify({"error": "Please provide a JSON"}), 400

        package = model_from_dict(Package, json)
        missing_fields = PackageView.validate_required_fields_presence(package)

        if len(missing_fields) != 0:
            return jsonify({"error": "Missing fields:" + str(missing_fields)}), 400

        try:
            id_package = PackageControl.register(package)
            return jsonify({ "id": id_package }), 200
        except ValueError as error:
            return jsonify({"error": str(error)}), 500

    def put(self,id_package=None):
        json = request.get_json()
        if json == None:
            return jsonify({"error": "Please provide a JSON"}), 400
        if id_package == None:
            return jsonify({"error": "Please provide a id_package"}), 400

        package = model_from_dict(Package, json)
        package.id = id_package

        try:
            success = PackageControl.update(package)
            if success == True:
                return jsonify({"id": id_package}), 200
            else:
                return jsonify({"error": "Unable to update Package with id " + str(id_package)}), 500
        except ValueError as error:
            return jsonify({"error": str(error)}), 500

    def delete(self,id_package=None):
        if id_package == None:
            return jsonify({"error": "Please provide a id_package"}), 400

        try:
            if PackageControl.delete(id_package) == True:
                return jsonify({"id": id_package}), 200
            else:
                return jsonify({"error": "No package found with id " + str(id_package)}), 404
        except ValueError as error:
            return jsonify({"error": str(error)}), 400

    @staticmethod
    def validate_required_fields_presence(package):
        missing_fields = []

        if package.width == None:
            missing_fields.append('width')
        if package.height == None:
            missing_fields.append('height')
        if package.length == None:
            missing_fields.append('length')
        if package.weight == None:
            missing_fields.append('weight')
        if package.volume == None:
            missing_fields.append('volume')
        if package.id_address_start == None:
            missing_fields.append('id_address_start')
        if package.id_address_destiny == None:
            missing_fields.append('id_address_destiny')

        return missing_fields

def initialize_view(app):
    endpoint='package_view'
    methods=['GET','POST','PUT','DELETE']
    url='/package/'
    pk='id_package'
    register_view(app,PackageView,endpoint,url,methods,pk)
