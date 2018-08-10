import os
import json

from urllib.parse import urlencode
from urllib.request import Request, urlopen

from flask import Flask, request

app = Flask(__name__)

"""
Things to add
 - Something 
"""

@app.route('/', methods=['POST'])
def webhook():
    data = request.get_json()

    if data['name'] != "Easton":
        if data['name'] == 'Colin Walton':
            if "left nut" in data['text']:
                msg = "Suck my right nut"
                send_message(msg)
            elif data['created_at']%8 == 0:
                msg = 'Shut up Colin'
                send_message(msg)

        if "Hi Easton" in data['text']:
            if data['name'] == "Christian Walton" or data['name'] == "Colin Walton" or data['name'] == 'Dane':
                msg = "Wadddup uncle"
                send_message(msg)
            elif data['name'] == "Jennifer Webb Walton":
                msg = "Hi Grandmaaaa!!"
                send_message(msg)
            elif data['name'] == "Steven Walton":
                msg = "Hey Gramps!"
                send_message(msg)
            elif data['name'] == "Devin Walton":
                msg = "Hi Mom :)"
                send_message(msg)
            elif data['name'] == "Itz Ya Boi T Chainz":
                msg = "Sup Papa Post"
                send_message(msg)
        elif "Easton" in data['text']:
            if data['created at']%4 == 0:
                msg = "Yea but can we just take a second to appreciate I'm cute as shit"
                send_message(msg)

        if "droppin" in data['text'] or "dropping" in data['text']:
            msg = "I only drop Tilted Titties because Papa Post and Mum didn't raise no bitch"
            send_message(msg)

        if "surf" in data['text']:
            url = 'http://magicseaweed.com/api/2d93b2d0c882f2ff100591c9812ab5/forecast/?spot_id=2643'

            json = urlopen(url).read().decode()
            msgJson = json.get_json()
            msg = msgJson['swell']['maxBreakingHeight']
            send_message(msg)

    return "ok", 200


def send_message(msg):
    url = 'https://api.groupme.com/v3/bots/post'

    data = {
        'bot_id' : os.getenv('GROUPME_BOT_ID'),
        'text'   : msg,
    }

    request = Request(url, urlencode(data).encode())
    json = urlopen(request).read().decode()