from flask import Flask    #import Flask module from the flask package

app = Flask(__name__)        #Create a Flask object with the imported Flask module. 
                            #This object will be our WSGI application called app
from app import views