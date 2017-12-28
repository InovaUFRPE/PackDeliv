#!/usr/bin/python3.5
"""API creation module."""

# Flask related imports
from flask import jsonify, request

# Core and utils related modules import statement
from app import app
from app.controller.combination import CombinationController
from app.dao.combination import CombinationDAO
from pprint import pprint

combinationCtrl = CombinationController()
combinationDAO = CombinationDAO()


@app.route('/join-packages', methods=['POST'])
def match_packages():
    """Function responsible for IO related to combination of packages."""
    car = request.get_json()
    try:
        vol = int(car['vol'])
        # position = LatLng(car['position'])
        info_service_order = combinationCtrl.join_packages(vol, None)
        return jsonify(info_service_order)
    except ValueError:
        return jsonify({'error': 'Volume ou localização inválidos'})


@app.route('/routes', methods=['POST'])
def create_route():
    """Function responsible for IO related to route management."""
    # address = request.get_json()
    pass


@app.route('/test', methods=['GET'])
def test():
    """Test function."""
    pprint(combinationDAO.select_packages(None))
    return jsonify()
