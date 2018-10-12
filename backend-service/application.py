import logging
import os
from minds import application

@application.route('/', methods=['GET'])
def default_route():
    return "CFG Team 5 backend page. Hello"

if __name__ == "__main__":
    application.run(host="0.0.0.0", port=5000)

