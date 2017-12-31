# coding=utf-8
from flask import Flask
from flask_cors import CORS
from Models.DB.DB_helper import INIT_API
from Views import vehicle_view

app = Flask(__name__)

INIT_API()
CORS(app)

if __name__ == '__main__' :
    vehicle_view.initializeView(app)
    
    app.run()
