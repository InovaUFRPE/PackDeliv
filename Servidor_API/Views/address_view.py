import json
from flask import request, jsonify
from flask.views import MethodView
from Views.viewHelper import register_view
from sqlalchemy import inspect
from Models.DB.DB_helper import Address, model_from_dict, model_as_dict
from Rest_utils.entities_atributes_Names import *
from Controlers.address_control import AddressControl

class AddressView(MethodView):
    def get(self,id_address=None):
        if id_address == None:
            return jsonify({"error": "Please provide a id_address"}), 400

        try:
            address = AddressControl.find(id_address)
            if address == None:
                return jsonify({"error": "No address found with id " + str(id_address)}), 404
            else:
                return jsonify(model_as_dict(address)), 200
        except ValueError as error:
            return jsonify({"error": str(error)}), 500

    def post(self):
        json = request.get_json()
        if json == None:
            return jsonify({"error": "Please provide a JSON"}), 400

        address = model_from_dict(Address, json)
        missing_fields = AddressView.validate_required_fields_presence(address)

        if len(missing_fields) != 0:
            return jsonify({"error": "Missing fields:" + str(missing_fields)}), 400

        try:
            id_address = AddressControl.register(address)
            return jsonify({ "id": id_address }), 200
        except ValueError as error:
            return jsonify({"error": str(error)}), 500

    def put(self,id_address=None):
        json = request.get_json()
        if json == None:
            return jsonify({"error": "Please provide a JSON"}), 400
        if id_address == None:
            return jsonify({"error": "Please provide a id_address"}), 400

        address = model_from_dict(Address, json)
        address.id = id_address

        try:
            success = AddressControl.update(address)
            if success == True:
                return jsonify({"id": id_address}), 200
            else:
                return jsonify({"error": "Unable to update Address with id " + str(id_address)}), 500
        except ValueError as error:
            return jsonify({"error": str(error)}), 500

    def delete(self,id_address=None):
        if id_address == None:
            return jsonify({"error": "Please provide a id_address"}), 400

        try:
            if AddressControl.delete(id_address) == True:
                return jsonify({"id": id_address}), 200
            else:
                return jsonify({"error": "No address found with id " + str(id_address)}), 404
        except ValueError as error:
            return jsonify({"error": str(error)}), 400

    @staticmethod
    def validate_required_fields_presence(address):
        missing_fields = []

        if address.street == None:
            missing_fields.append(ADDRESS_STREET)
        if address.number == None:
            missing_fields.append(ADDRESS_NUMBER)
        if address.district == None:
            missing_fields.append(ADDRESS_DISTRICT)
        if address.postal_code == None:
            missing_fields.append(ADDRESS_POSTAL_CODE)
        if address.city == None:
            missing_fields.append(ADDRESS_CITY)
        if address.state == None:
            missing_fields.append(ADDRESS_STATE)
        if address.country == None:
            missing_fields.append(ADDRESS_COUNTRY)
        if address.lat == None:
            missing_fields.append(LOCALIZATION_LAT)
        if address.long == None:
            missing_fields.append(LOCALIZATION_LONG)
        if address.id_company == None and address.id_client == None:
            missing_fields.append(COMPANY+'_'+COMPANY_ID)
            missing_fields.append(CLIENT+'_'+CLIENT_ID)

        return missing_fields

def initializeView(app):
    endpoint='address_view'
    methods=['GET','PUT','POST','DELETE']
    url='/address/'
    pk='id_address'
    register_view(app,AddressView,endpoint,url,methods,pk)
