# coding=utf-8
from flask import Flask

from flask_cors import CORS
from Models.DB.DB_helper import INIT_API
from test.teste import teste
app = Flask(__name__)

INIT_API()

CORS(app)

teste()

if __name__ == '__main__' :
    app.run()

