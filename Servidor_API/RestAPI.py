# coding=utf-8
from flask import Flask

from flask_cors import CORS
from DB.DB_helper import INIT_API
from Views.viewHelper import app

INIT_API()

CORS(app)

if __name__ == '__main__' :
    app.run()
