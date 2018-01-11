import json
from flask import request, jsonify
from flask.views import MethodView
from Views.viewHelper import register_view
from sqlalchemy import inspect
from Models.DB.DB_helper import Delivery, model_from_dict, model_as_dict
from Rest_utils.entities_atributes_Names import *
from Controlers.delivery_control import DeliveryControl

class DeliveryView(MethodView):
    def get(self,id_delivery=None):
        if id_delivery == None:
            return jsonify({"error": "Please provide a id_delivery"}), 400

        try:
            delivery = DeliveryControl.find(id_delivery)
            if delivery == None:
                return jsonify({"error": "No delivery found with id " + str(id_delivery)}), 404
            else:
                return jsonify(model_as_dict(delivery)), 200
        except ValueError as error:
            return jsonify({"error": str(error)}), 500

    def post(self):
        json = request.get_json()
        if json == None:
            return jsonify({"error": "Please provide a JSON"}), 400

        delivery = model_from_dict(Delivery, json)
        missing_fields = DeliveryView.validate_required_fields_presence(delivery)

        if len(missing_fields) != 0:
            return jsonify({"error": "Missing fields:" + str(missing_fields)}), 400

        try:
            id_delivery = DeliveryControl.register(delivery)
            return jsonify({ "id": id_delivery }), 200
        except ValueError as error:
            return jsonify({"error": str(error)}), 500

    def put(self,id_delivery=None):
        json = request.get_json()
        if json == None:
            return jsonify({"error": "Please provide a JSON"}), 400
        if id_delivery == None:
            return jsonify({"error": "Please provide a id_delivery"}), 400

        delivery = model_from_dict(Delivery, json)
        delivery.id = id_delivery

        try:
            success = DeliveryControl.update(delivery)
            if success == True:
                return jsonify({"id": id_delivery}), 200
            else:
                return jsonify({"error": "Unable to update Delivery with id " + str(id_delivery)}), 500
        except ValueError as error:
            return jsonify({"error": str(error)}), 500

    def delete(self,id_delivery=None):
        if id_delivery == None:
            return jsonify({"error": "Please provide a id_delivery"}), 400

        try:
            if DeliveryControl.delete(id_delivery) == True:
                return jsonify({"id": id_delivery}), 200
            else:
                return jsonify({"error": "No delivery found with id " + str(id_delivery)}), 404
        except ValueError as error:
            return jsonify({"error": str(error)}), 400

    @staticmethod
    def validate_required_fields_presence(delivery):
        missing_fields = []

        if delivery.status == None:
            missing_fields.append(DELIVERY_STATUS)
        if delivery.type == None:
            missing_fields.append(DELIVERY_TYPE)

        return missing_fields

def initialize_view(app):
    endpoint='delivery_view'
    methods=['POST','GET','PUT','DELETE']
    url='/delivery/'
    pk='id_delivery'
    register_view(app,DeliveryView,endpoint,url,methods,pk)
