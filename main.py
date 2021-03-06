from api import API
from waits import Waits
from map import Map
from enum import Enum
from flask import Flask,request
import json

app = Flask(__name__)

class State(Enum):
    READY=0
    LOCA=1
    SYMP=2
    ALRT=3

class Main():

    one = 0
    two = 0
    three = 0
    counter = 0

    def __init__(self):
        self.api = API()
        self.data = []
        self.myID = self.api.findUserID()
        self.counter=0
        self.activeUser="Selena"
        for chat in self.api.parseChats():
            temp = []
            temp.append(chat['id'])
            temp.append(State.READY)
            self.data.append(temp)
        print(self.data)
        #self.readAllMessages()

    def readAllMessages(self):
        for chat in self.data:
            id=chat[0]
            self.mainControl()
            #for message in self.api.readMessage(id):
                #print(message['sender']['id']+": "+message['message'])
                #if chat[1]==State.READY:
                    #self.api.sendMessage(id,self.api.writePromptString())
                    #mainControl()
#'''if '1' in message['message']:
#                    chat[1]=State.LOCA
#                elif '2' in message['message']:
#                    chat[1]=State.SYMP
#                    #self.api.sendMessage(chat[0],"Sure, I can help with that. What symptoms do you have?")
#                elif '3' in message['message']:
#                    chat[1]=State.ALRT'''


    def incrementCounter(self):
        id=self.api.findChatByMemberName(self.activeUser)
        print(self.api.readMessage(id)[0]['sender']['id'])
        if(self.api.readMessage(id)[0]['sender']['id']!=self.myID):
            self.mainControl()
            self.counter+=1

    def mainControl(self):
        id=self.api.findChatByMemberName(self.activeUser)
        print(self.counter)
        if self.counter == 0:
            self.api.sendMessage(id,"Hello, I am Moose M.D, a friendly healthcare chatbot. Would you like me to (1) Search nearby healthcare services, (2) match your symptoms, (3) help regulate your medication?")
        elif self.counter == 1:
            self.api.sendMessage(id,"Sure, I can help you with that. What are your symptoms?")
        elif self.counter == 2:
            self.api.sendMessage(id,"I understand that you are experiencing cough, fever, and nausea. Am I correct?")
        elif self.counter == 3:
            self.api.sendMessage(id,"Here are some possible matches: Flu = high Hepatitis A = moderate Measles = low Would you like help with anything else?")
        elif self.counter == 4:
            self.api.sendMessage(id,"Hello, what would you like help with?")
        elif self.counter == 5:
            self.api.sendMessage(id,"Sure. What medication(s) are you taking?")
        elif self.counter == 6:
            self.api.sendMessage(id,"What days of the week do you need to take insulin?")
        elif self.counter == 7:
            self.api.sendMessage(id,"What time of day would you like a reminder text?")
        elif self.counter == 8:
            self.api.sendMessage(id,"Ok, your next reminder is set for today at 7:00pm. Would you like help with anything else?")
        elif self.counter == 9:
            self.api.sendMessage(id,"Hello, what would you like help with?")
        elif self.counter == 10:
            self.api.sendMessage(id,"Of course. What is your postal code?")
        elif self.counter == 11:
            self.api.sendMessage(id,"Here are the nearest healthcare centres and their availability: St. Michaels Hospital: 30 mins wait time The Hospital for Sick Children: 15 mins wait time The Rehab and Wellbeing Centre at Mount Sinai Hospital: 25 mins wait time Would you like help with anything else?")
        elif self.counter == 12:
            self.counter == 0
        else:
            self.counter += 1 #wait for user to send another message.

b = Main()

@app.route('/',methods=['POST'])
def post_json():
    data=request.form
    b.incrementCounter()
    print(data)
    return data

Flask.run(app,host="167.99.186.154")
