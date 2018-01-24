import json
from flask import request, jsonify
from flask.views import MethodView
from Views.viewHelper import register_view
from Models.DB.DB_helper import Area, Package, model_from_dict
from Rest_utils.entities_atributes_Names import *
from Controlers.area_control import AreaControl
from Views.package_view import PackageView

class AreaView(MethodView):
    def get(self,id_area=None):
        try:
            area = AreaControl.find(id_area)
            if area == None:
                return jsonify({"error": "No area found with id " + str(id_area)}), 404
            else:
                if id_area == None:
                    return jsonify( [ item.as_dict() for item in area] ), 200
                return jsonify(area.as_dict()), 200
        except ValueError as error:
            return jsonify({"error": str(error)}), 500

    def post(self):
        json = request.get_json()
        if json == None:
            return jsonify({"error": "Please provide a JSON"}), 400

        area = AreaView.build_area_and_packages(json)
        missing_fields = AreaView.validate_required_fields_presence(area)

        if len(missing_fields) != 0:
            return jsonify({"error": "Missing fields:" + str(missing_fields)}), 400

        try:
            id_area = AreaControl.register(area)
            return jsonify({ "id": id_area }), 200
        except ValueError as error:
            return jsonify({"error": str(error)}), 500

    def put(self,id_area=None):
        json = request.get_json()
        if json == None:
            return jsonify({"error": "Please provide a JSON"}), 400
        if id_area == None:
            return jsonify({"error": "Please provide an id_area"}), 400

        area = AreaView.build_area_and_packages(json)
        area.id = id_area

        try:
            success = AreaControl.update(area)
            if success == True:
                return jsonify({"id": id_area}), 200
            else:
                return jsonify({"error": "Unable to update Area with id " + str(id_area)}), 500
        except ValueError as error:
            return jsonify({"error": str(error)}), 500

    def delete(self,id_area=None):
        if id_area == None:
            return jsonify({"error": "Please provide an id_area"}), 400

        try:
            if AreaControl.delete(id_area) == True:
                return jsonify({"id": id_area}), 200
            else:
                return jsonify({"error": "No area found with id " + str(id_area)}), 404
        except ValueError as error:
            return jsonify({"error": str(error)}), 400

    @staticmethod
    def build_area_and_packages(area_json):
        area = model_from_dict(Area, area_json)
        packages_json = area_json.get("packages", None)
        if packages_json != None:
            area.packages = [model_from_dict(Package, package_json) for package_json in packages_json]
        return area

    @staticmethod
    def validate_required_fields_presence(area):
        missing_fields = []

        if area.lat == None:
            missing_fields.append('lat')
        if area.long == None:
            missing_fields.append('long')
        if area.area_radius == None:
            missing_fields.append('area_radius')
        if area.packages == []:
            missing_fields.append('packages')

        return missing_fields

def initialize_view(app):
    endpoint='area_view'
    methods=['GET','POST','PUT','DELETE']
    url='/area/'
    pk='id_area'
    register_view(app,AreaView,endpoint,url,methods,pk)
