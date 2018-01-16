import json
from flask import request, jsonify
from flask.views import MethodView
from Views.viewHelper import register_view
from sqlalchemy import inspect
from Models.DB.DB_helper import ServiceOrder, Delivery, model_from_dict, model_as_dict
from Rest_utils.entities_atributes_Names import *
from Controlers.service_order_control import ServiceOrderControl

class ServiceOrderView(MethodView):
    def get(self,id_service_order=None):
        if id_service_order == None:
            return jsonify({"error": "Please provide a id_service_order"}), 400

        try:
            service_order = ServiceOrderControl.find(id_service_order)
            if service_order == None:
                return jsonify({"error": "No service_order found with id " + str(id_service_order)}), 404
            else:
                return jsonify(service_order.as_dict()), 200
        except ValueError as error:
            return jsonify({"error": str(error)}), 500

    def post(self):
        json = request.get_json()
        if json == None:
            return jsonify({"error": "Please provide a JSON"}), 400

        service_order = model_from_dict(ServiceOrder, json)
        if "deliveries" in json.keys() and json['deliveries'] != None:
            service_order.deliveries = [ model_from_dict(Delivery, dic) for dic in json['deliveries']]
        missing_fields = ServiceOrderView.validate_required_fields_presence(service_order)

        if len(missing_fields) != 0:
            return jsonify({"error": "Missing fields:" + str(missing_fields)}), 400

        try:
            id_service_order = ServiceOrderControl.register(service_order)
            return jsonify({ "id": id_service_order }), 200
        except ValueError as error:
            return jsonify({"error": str(error)}), 500

    def put(self,id_service_order=None):
        json = request.get_json()
        if json == None:
            return jsonify({"error": "Please provide a JSON"}), 400
        if id_service_order == None:
            return jsonify({"error": "Please provide a id_service_order"}), 400

        service_order = model_from_dict(ServiceOrder, json)
        if json['deliveries'] != None:
            service_order.deliveries = [ model_from_dict(Delivery, dic) for dic in json['deliveries']]
        service_order.id = id_service_order

        try:
            success = ServiceOrderControl.update(service_order)
            if success == True:
                return jsonify({"id": id_service_order}), 200
            else:
                return jsonify({"error": "Unable to update ServiceOrder with id " + str(id_service_order)}), 500
        except ValueError as error:
            return jsonify({"error": str(error)}), 500

    def delete(self,id_service_order=None):
        if id_service_order == None:
            return jsonify({"error": "Please provide a id_service_order"}), 400

        try:
            if ServiceOrderControl.delete(id_service_order) == True:
                return jsonify({"id": id_service_order}), 200
            else:
                return jsonify({"error": "No service_order found with id " + str(id_service_order)}), 404
        except ValueError as error:
            return jsonify({"error": str(error)}), 400

    @staticmethod
    def validate_required_fields_presence(service_order):
        missing_fields = []

        if service_order.code == None:
            missing_fields.append('code')
        if service_order.status == None:
            missing_fields.append('status')

        return missing_fields

def initialize_view(app):
    endpoint='service_order_view'
    methods=['POST','GET','PUT','DELETE']
    url='/service_order/'
    pk='id_service_order'
    register_view(app,ServiceOrderView,endpoint,url,methods,pk)
