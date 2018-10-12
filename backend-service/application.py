import logging
import os
from minds import application
# logger = logging.getLogger(__name__)

@application.route('/', methods=['GET'])
def default_route():
    # application.logger.info("base url requested. saying hello")
    return "CFG Team 5 backend page. Hello"

if __name__ == "__main__":
    # if 'DYNO' not in os.environ:   
    #     logFormatter = logging.Formatter("%(asctime)s [%(filename)s] [%(funcName)s] [%(lineno)d] [%(levelname)-5.5s]  %(message)s")
    #     rootLogger = logging.getLogger()

    #     rootLogger.setLevel(logging.INFO)

    #     fileHandler = logging.FileHandler("team.log")
    #     fileHandler.setFormatter(logFormatter)
    #     rootLogger.addHandler(fileHandler)

    #     consoleHandler = logging.StreamHandler()
    #     consoleHandler.setFormatter(logFormatter)
    #     rootLogger.addHandler(consoleHandler)

        # logger.info("Starting application ...")
    application.run(host="0.0.0.0", port=5000)
    # app.run(debug=True)

