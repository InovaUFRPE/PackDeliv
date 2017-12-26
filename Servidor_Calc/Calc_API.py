#!/usr/bin/python3.5

# API related modules import statement
from flask import Flask, jsonify, request
import requests
from flask_cors import CORS

# Core and utils related modules import statement
from controller import combination
from utils import LatLng

# declarations
app = Flask(__name__)
combinationCtrl = combination.CombinationController()

CORS(app)


@app.route('/join-packages', methods=['POST'])
def match_packages():
    """Function responsible for IO related to combination of packages."""
    car = request.get_json()
    try:
        vol = int(car['vol'])
        position = LatLng(car['position'])
        info_service_order = combinationCtrl.join_packages(vol, position)
        return jsonify({'response': info_service_order})
    except ValueError:
        return jsonify({'error': 'Volume ou localização inválidos'})


@app.route('/routes', methods=['POST'])
def create_route():
    """Function responsible for IO related to route management."""
    address = request.get_json()
    pass


if __name__ == "__main__":
    app.run()
