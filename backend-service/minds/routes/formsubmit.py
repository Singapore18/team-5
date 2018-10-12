# import logging

from flask import request, jsonify

from minds import application as app

# logger = logging.getLogger(__name__)

@app.route('/submitform', methods=['POST'])
def submitform():
    data = request.get_json()
    app.logger.info("data sent for evaluation {}".format(data))
    inputValue = data.get("input")
    result = inputValue * inputValue
    app.logger.info("My result :{}".format(result))
    return jsonify(result)



@app.route('/client', methods=['GET'])
def submitform():
    
    return jsonify(result)
