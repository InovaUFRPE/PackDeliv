# coding=utf-8
from flask import Flask, jsonify, request
from flask_cors import CORS
from Models.DB.DB_helper import INIT_API
from Views import(vehicle_view, company_view, deliveryman_view,
address_view, client_view, package_view, delivery_view, service_order_view, login_view,
area_view)
import requests

app = Flask(__name__)

INIT_API()
CORS(app)

@app.route('/cnpj/<cnpj>',methods=['GET'])
def cnpj(cnpj):
    if request.method == 'GET':

        r = requests.get('https://www.receitaws.com.br/v1/cnpj/'+ str(cnpj) )

        return jsonify(r.json())

if __name__ == '__main__' :
    vehicle_view.initialize_view(app)
    company_view.initialize_view(app)
    deliveryman_view.initialize_view(app)
    address_view.initialize_view(app)
    client_view.initialize_view(app)
    package_view.initialize_view(app)
    delivery_view.initialize_view(app)
    service_order_view.initialize_view(app)
    login_view.initialize_view(app)
    area_view.initialize_view(app)
    app.run(host='0.0.0.0')
