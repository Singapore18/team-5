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

	output = {}
    output["firstName"]        = "Peter"
    output["familyName"]       = "Lee"
    output["gender"]           = "M"
    output["nric"]             = "S12312323G"
    output["address"]          = "Bishan"
    output["timeAvailability"] = "Weekdays"
    output["skills"]           = ["communication", "cleaning"]
	output["tag"]              = "Think Different." 
	output["assistance"]       = "Walking should be minimised."
	output["careerCoach"]      = "Jenny"

    return output



@app.route('/client', methods=['GET'])
def getallclients():
    fake_data = [
        {
            'Id':'1',
            'Name':'boo',
            'Tagline':'To be or not to be',
            'AssistanceDesc':'I need assistance with using something',
            'Interests':'Retail'
        },
        {
            'Id':'1',
            'Name':'lee',
            'Tagline':'Hello',
            'AssistanceDesc':'I need assistance with using another thing',
            'Interests':'Hospitality'
        }
    ]
    return jsonify(fake_data)
