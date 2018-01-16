import json
from flask import request, jsonify
from flask.views import MethodView
from Views.viewHelper import register_view
from Models.DB.DB_helper import Deliveryman, Vehicle, Address, model_from_dict
from Rest_utils.entities_atributes_Names import *
from Controlers.deliveryman_control import DeliverymanControl
from Views.company_view import CompanyView

class DeliverymanView(MethodView):
    def get(self,id_deliveryman=None):
        if id_deliveryman == None:
            return jsonify({"error": "Please provide a id_deliveryman"}), 400

        try:
            deliveryman = DeliverymanControl.find(id_deliveryman)
            if deliveryman == None:
                return jsonify({"error": "No deliveryman found with id " + str(id_deliveryman)}), 404
            else:
                return jsonify(deliveryman.as_dict()), 200
        except ValueError as error:
            return jsonify({"error": str(error)}), 500

    def post(self):
        json = request.get_json()
        if json == None:
            return jsonify({"error": "Please provide a JSON"}), 400

        deliveryman =  model_from_dict(Deliveryman, json)
        #deliveryman.vehicle = [ model_from_dict(Vehicle, dic) for dic in json['vehicle'] ]
        deliveryman.addresses = [ model_from_dict(Address, dic) for dic in json['addresses'] ]
        
        missing_fields = DeliverymanView.validate_required_fields_presence(deliveryman)

        if len(missing_fields) != 0:
            return jsonify({"error": "Missing fields:" + str(missing_fields)}), 400

        try:
            id_deliveryman = DeliverymanControl.register(deliveryman)
            return jsonify({ "id": id_deliveryman }), 200
        except ValueError as error:
            return jsonify({"error": str(error)}), 500

    def put(self,id_deliveryman=None):
        json = request.get_json()
        if json == None:
            return jsonify({"error": "Please provide a JSON"}), 400
        if id_deliveryman == None:
            return jsonify({"error": "Please provide a id_deliveryman"}), 400

        deliveryman =  model_from_dict(Deliveryman, json)
        #deliveryman.vehicle = [model_from_dict(Vehicle, dic) for dic in json['vehicle']]
        deliveryman.id = id_deliveryman

        try:
            success = DeliverymanControl.update(deliveryman)
            if success == True:
                return jsonify({"id": id_deliveryman}), 200
            else:
                return jsonify({"error": "Unable to update Deliveryman with id " + str(id_deliveryman)}), 500
        except ValueError as error:
            return jsonify({"error": str(error)}), 500

    def delete(self,id_deliveryman=None):
        if id_deliveryman == None:
            return jsonify({"error": "Please provide a id_deliveryman"}), 400

        try:
            if DeliverymanControl.delete(id_deliveryman) == True:
                return jsonify({"id": id_deliveryman}), 200
            else:
                return jsonify({"error": "No deliveryman found with id " + str(id_deliveryman)}), 404
        except ValueError as error:
            return jsonify({"error": str(error)}), 400

    @staticmethod
    def validate_required_fields_presence(deliveryman):
        missing_fields = CompanyView.validate_required_fields_presence(deliveryman)

        if deliveryman.name_deliveryman == None:
            missing_fields.append('name')
        if deliveryman.dui == None:
            missing_fields.append('dui')
        if deliveryman.status == None:
            missing_fields.append('status')
        if deliveryman.ready == None:
            missing_fields.append('ready')
        if deliveryman.lat == None:
            missing_fields.append('lat')
        if deliveryman.long == None:
            missing_fields.append('long')
        

        return missing_fields



def initialize_view(app):
    endpoint='deliveryman_view'
    methods=['GET','POST','PUT','DELETE']
    url='/deliveryman/'
    pk='id_deliveryman'
    register_view(app,DeliverymanView,endpoint,url,methods,pk)
