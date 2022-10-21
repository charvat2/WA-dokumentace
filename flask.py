from flask import Flask
from flask import request
from time import strftime
import datetime
import json


app = Flask(__name__)
date = datetime.datetime.now()
@app.route('/')
def index():
    return 'Vitejte na serveru SPSE Jecna'

@app.route('/zkouska')
def moje_zkouska():
    return 'Možná budou fungovat i háčky a čárky.'

@app.route('/datum')
def datum():
    return str(str(date.day)+ "." + str(date.month)+ ". " + str(date.year))

@app.route('/cas')
def cas():
    current_time = strftime("%H:%M:%S")
    return (current_time)

@app.route('/datumacas')
def datumacas():

    dt_string = strftime("%d.%m.%Y %H:%M:%S")
    return(dt_string)

@app.route('/ISO')
def ISO_8601():

    dt_string = strftime("%d%m%Y %H:%M:%S")
    return(dt_string)

@app.route('/chat', methods=['GET'])
def chat_serverget():
    zpravy = {
        "data" : [
            {"zprava1": "ahoj", "id" : 1},
            {"zprava2": "cau", "id": 2},
            {"zprava3": "cus", "id": 3},
            {"zprava4": "nazdar", "id": 4},

        ],

        "links": [
            {
                "type": "GET",
                "href": "/chat/zpravy/GET",
            }
        ]
    }
    return(zpravy)

@app.route('/chatget', methods=['GET'])
def chat_servergetid():
    zpravy = {
        "data" : [
            {"zprava1": "ahoj", "id" : 1},
            {"zprava2": "cau", "id": 2},
            {"zprava3": "cus", "id": 3},
            {"zprava4": "nazdar", "id": 4},

        ],

        "links": [
            {
                "type": "GET",
                "href": "/chat/zprava1/GET/1",

            }
        ]
    }
    return(zpravy[1])

@app.route('/chatdelete', methods=['DELETE'])
def chat_serverdelete():
    zpravy = {
        "data" : [
            {"zprava1": "ahoj", "id" : 1},
            {"zprava2": "cau", "id": 2},
            {"zprava3": "cus", "id": 3},
            {"zprava4": "nazdar", "id": 4},

        ],

        "links": [
            {
                "type": "DELETE",
                    "href": "/chat/zpravy/DELETE",

            }
        ]
    }

    zpravy.pop(1)
    return("smazal jsi druhou polozku z listu" + zpravy)

@app.route('/chatpost', methods=['POST'])
def chat_serverpost():
    zpravy = {
        "data" : [
            {"zprava1": "ahoj", "id" : 1},
            {"zprava2": "cau", "id": 2},
            {"zprava3": "cus", "id": 3},
            {"zprava4": "nazdar", "id": 4},

        ],

        "links": [
            {
                "type": "POST",
                "href": "/chat/zpravy/POST",

            }
        ]
    }
    zpravy.add("zdař bůh")
    return(zpravy)

@app.route('/chatput', methods=['PUT'])
def chat_serverput():
    zpravy = {
        "data" : [
            {"zprava1": "ahoj", "id" : 1},
            {"zprava2": "cau", "id": 2},
            {"zprava3": "cus", "id": 3},
            {"zprava4": "nazdar", "id": 4},

        ],

        "links": [
            {
                "type": "PUT",
                "href": "/chat/zpravy/PUT/1",
            }
        ]
    }
    zpravy.insert(1, "cussss")
    return(zpravy)

@app.route('/restapi/v1/user/<id>', methods=['GET'])
def user_show(username):
    return "Ahoj "+username

@app.route('/restapi/v2/user/<username>', methods=['DELETE'])
def user_delete(username):
    return "Uzivatel "+username+" byl smazan"

@app.route('/doc', methods=['GET'])
def doc():



    if __name__ == '__main__':
        app.run(host='0.0.0.0', port=80, debug=False)

