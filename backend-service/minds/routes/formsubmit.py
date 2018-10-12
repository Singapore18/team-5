# import logging

from flask import request, jsonify

from minds import application as app
from minds import db
# logger = logging.getLogger(__name__)



paragraph = {
    "retail": "Clothing always appeal to me. When I can help someone find the perfect clothing of the right size and color, I feel accomplished and at the same time happy for that customer. I will like to bring smiles to all my customers by helping them.",
    "f&b": "I am very hardworking and love helping people. To be able to anticipate what a guest expects from his stay and to consistently deliver above and beyond those expectations, by recognizing each individual guest is why I love the f&b industry. If I can make the guests’ dining experience better I will try my best.",
    "hospitality": "I like to render my services whenever someone needs me."
}

paragraph_str = {
    "motivated": "He shows up to work on time and takes his breaks on time. He eagerly looks forward to any training that might help him do better. He is reliable and consistently meets his daily job goals.",
    "hardworking": " Stays focused on the tasks before him and spends little time chatting with other employees. His work is consistently of acceptable to excellent quality, and he looks for more work if everything assigned to him is done.",
    "friendly": "Love to smile and greet others."
}


@app.route('/submitform', methods=['POST'])
def submitform():
    data = request.get_json()

    if 'firstName' in data and data['firstName'] == "":
        return jsonify({"status": "form rejected. have a name pls"})

    if 'industries' in data and data['industries'] in ('retail', 'industries', 'f&b'):
        data['ind_paragraph'] = paragraph[data['industries']]
    if 'strength' in data and data['strength'] in ('motivated', 'hardworking', 'friendly'):
        data['str_paragraph'] = paragraph_str[data['strength']]
    db.insert(data['firstName'], data)
    return jsonify({"status": "form received"})


@app.route('/client', methods=['GET'])
def getallclients():
    clientlist = db.get_all_client()
    newlist = []
    for item in clientlist:
        newlist.append({
            'Name': item['firstName'],
            'Tagline': item['tagline'],
            'AssistanceDesc': item['assistance'],
            'Interests': item['industries']
        })
    return jsonify(clientlist)

@app.route('/list/client', methods=['GET'])
def getemplclient():
    clientlist = db.get_all_client()
    newlist = []
    for item in clientlist:
        newlist.append({
            'age': item['age'],
            'address':item['address'],
            'name': item['firstName'] + ' ' + item['familyName'],
            'id': item['firstName'],
            'interest': item['industries']
        })
    return jsonify(newlist)

@app.route('/resume/<firstname>', methods=['GET'])
def getresume(firstname):
    result = db.get(firstname)
    return jsonify(result)

# address: "Bishan"
# age: "23"
# assistance: "test"
# experience: "yes"
# familyName: "Tan"
# firstName: "David"
# gender: "Male"
# industries: "retail"
# nric: "fdsfsd"
# strength: "motivated"
# tagline: "ssfdkj"
# timeAvailability: "weekdays"



# def info_for_employer(result):
#     first_name = result["firstName"]
#     tag_line = result["tagline"]
#     assistance_Desc = result["assistance"]
#     interests = result["industries"]
#     strengths = result["strength"]
#     experience = result["experience"]
#     time_avail = result["timeAvailability"]
#     careerCoach = result["careerCoach"]
#     employer_dict = {"firstName" : first_name, "tagLine" : tag_line, "assistanceDesc" : assistance_Desc,
#                         "interests" : interests, "strengths" : strengths, "experience" : experience, 
#                         "time_avail" : time_avail, "careerCoach" : careerCoach}
    
#     return employer_dict



# {
# age: "25"
# address
# # assistance: "walking assistance needed."
# # careerCoach: "Jenny"
# # email: "Bishan"
# familyName: "Tan"
# firstName: "David"
# # gender: "Male"
# industries: "retail"
# nric: "G3242423523P"
# strength: "communication"
# tagline: "Work hard, play harder."
# timeAvailability: "weekdays"
# experience: "Worked at mcdonalds for 2 years"
# }