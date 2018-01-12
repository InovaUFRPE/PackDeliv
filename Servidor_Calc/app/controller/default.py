#!/usr/bin/python3.5
"""API creation module."""

# Flask related imports
from flask import jsonify, request

# Core and utils related modules imports
from app import app
from app.controller.combination import CombinationController
from app.dao.combination import CombinationDAO
from app.lib.utils import LatLng

combinationCtrl = CombinationController()
combinationDAO = CombinationDAO()


@app.route('/join-packages', methods=['POST'])
def match_packages():
    """Function responsible for IO related to combination of packages."""
    vehicle = request.get_json()
    #vehicle['position'] = LatLng(vehicle['position'])
    info_service_order = combinationCtrl.join_packages(vehicle)
    return jsonify(info_service_order)


@app.route('/routes', methods=['POST'])
def create_route():
    """Function responsible for IO related to route management."""
    # address = request.get_json()
    pass
