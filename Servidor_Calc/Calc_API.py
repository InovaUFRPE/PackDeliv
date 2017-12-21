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

# route responsible to make the combination of packages
@app.route('/join-packages', methods=['POST'])

def match_packages():
    car = request.get_json()
    try:
        vol = int(car['vol'])
        position = LatLng(car['position'])
        info_service_order = combinationCtrl.join_packages(vol, position)
        return jsonify({'response': info_service_order})
    except ValueError:
        return jsonify({'error': 'Volume ou localização inválidos'})