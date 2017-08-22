from flask import Flask
from flask_restful import Resource, Api
from flask_httpauth import HTTPBasicAuth

app = Flask(__name__)
apiobj = Api(app)
auth = HTTPBasicAuth()


import secrets
import easyrash.api
import easyrash.models
