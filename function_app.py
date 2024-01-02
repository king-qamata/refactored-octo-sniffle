import azure.functions as func
import datetime
import json
import logging
from Func1.main import app1
from Func2.main import app_flask

app = func.FunctionApp()

app.register_functions(app1)


app = func.WsgiFunctionApp(app=app_flask.wsgi_app, 
                           http_auth_level=func.AuthLevel.ANONYMOUS) 

#app.register_functions(app_flask)