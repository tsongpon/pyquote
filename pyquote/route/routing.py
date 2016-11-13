from flask import Response, request
from pyquote import app
import json
from pyquote.data.ad_repository import QuoteRepository


@app.route('/ping', methods=['GET'])
def index():
    repository = QuoteRepository()
    repository.ping_db()
    return "pong"
