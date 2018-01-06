from flask import Flask
from flask_cors import CORS
from Models.DB.DB_helper import INIT_API

def register_view(app, view, endpoint, url, choiceMethods=['GET'], pk=None, pk_type='int'):
    view_func = view.as_view(endpoint)
    if ('GET' in choiceMethods):
        app.add_url_rule(url, defaults={pk: None},view_func=view_func, methods=['GET',])

    if ('POST' in choiceMethods):
        app.add_url_rule(url, view_func=view_func, methods=['POST',])

    if any(x in ['GET', 'PUT', 'DELETE'] for x in choiceMethods ) and pk != None :
        app.add_url_rule('%s<%s:%s>' % (url, pk_type, pk), view_func=view_func,methods=[x for x in ['GET', 'PUT', 'DELETE'] if x in choiceMethods])
    
