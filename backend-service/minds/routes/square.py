# import logging

from flask import request, jsonify

from minds import application as app

# logger = logging.getLogger(__name__)

@app.route('/echo', methods=['POST'])
def echo():
    data = request.get_json()
    result = data
    return jsonify(result)

