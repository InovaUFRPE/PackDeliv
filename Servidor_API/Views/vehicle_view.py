import json
from flask import request, jsonify
from flask.views import MethodView
from Views.viewHelper import register_view
from Models.DB.DB_helper import Vehicle, model_from_dict
from Rest_utils.entities_atributes_Names import *
from Controlers.vehicle_control import VehicleControl

class VehicleView(MethodView):
    def get(self,id_vehicle=None):
        if id_vehicle == None:
            return jsonify({"error": "Please provide a id_vehicle"}), 400

        try:
            vehicle = VehicleControl.find(id_vehicle)
            if vehicle == None:
                return jsonify({"error": "No vehicle found with id " + str(id_vehicle)}), 404
            else:
                return jsonify(vehicle.as_dict()), 200
        except ValueError as error:
            return jsonify({"error": str(error)}), 500

    def post(self):
        json = request.get_json()
        if json == None:
            return jsonify({"error": "Please provide a JSON"}), 400

        vehicle = model_from_dict(Vehicle, json)

        if vehicle.license_plate == None:
            return jsonify({"error": "Missing " + VEHICLE_LICENSE_PLATE}), 400
        elif vehicle.year == None:
            return jsonify({"error": "Missing " + VEHICLE_YEAR}), 400
        elif vehicle.model == None:
            return jsonify({"error": "Missing " + VEHICLE_MODEL}), 400
        elif vehicle.volume == None:
            return jsonify({"error": "Missing " + VEHICLE_VOLUME}), 400

        try:
            id_vehicle = VehicleControl.register(vehicle)
            return jsonify({ "id": id_vehicle }), 200
        except ValueError as error:
            return jsonify({"error": str(error)}), 500

    def put(self,id_vehicle):
        json = request.get_json()
        if json == None:
            return jsonify({"error": "Please provide a JSON"}), 400
        if id_vehicle == None:
            return jsonify({"error": "Please provide a id_vehicle"}), 400

        vehicle = model_from_dict(Vehicle, json)
        vehicle.id = id_vehicle

        try:
            success = VehicleControl.update(vehicle)
            if success == True:
                return jsonify({"id": id_vehicle}), 200
            else:
                return jsonify({"error": "Unable to update Vehicle with id " + str(id_vehicle)}), 500
        except ValueError as error:
            return jsonify({"error": str(error)}), 500

    def delete(self,id_vehicle=None):
        if id_vehicle == None:
            return jsonify({"error": "Please provide a id_vehicle"}), 400

        try:
            if VehicleControl.delete(id_vehicle) == True:
                return jsonify({"id": id_vehicle}), 200
            else:
                return jsonify({"error": "No vehicle found with id " + str(id_vehicle)}), 404
        except ValueError as error:
            return jsonify({"error": str(error)}), 400


def initialize_view(app):
    endpoint='vehicle_view'
    methods=['GET','POST','PUT','DELETE']
    url='/vehicle/'
    pk='id_vehicle'
    register_view(app,VehicleView,endpoint,url,methods,pk)
