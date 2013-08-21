from flask import Flask
import deal
import sys
sys.modules['deal'] = deal

application = Flask(__name__)
app = application
app.config.from_object('config')

from app import views
