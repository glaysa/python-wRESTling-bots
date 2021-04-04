from models.user import User
from models.message import Message, Content
from models.chatroom import Chatroom
import json

# user = User(username="Nima", personality="Unknown")
# msg = Message(sender="Nima", content=Content(message="Hello!"), type="Chat")
# room = Chatroom(name="Room 1", users=[user, user, user], messages=[msg, msg])
# print(user.to_dictionary())
'''
jsonstrusr = "{" \
            "\"username\" : \"Nima\"," \
             "\"personality\" : \"Unknown\"" \
             "}"
#usr1 = User.json_to_room(json_str=jsonstrusr)
#print(usr1)

jsonmsg = "{" \
          "\"sender\" : \"Nima\"," \
          "\"content\" : {" \
          "\"message\" : \"Hello there\"," \
          "\"action\" : null," \
          "}," \
          "\"timestamp\" : null," \
          "\"type\" : \"CHAT\"," \
          "}"
msg = Message.json_to_msg(jsonmsg)
print(msg)

jsonroom = "{" \
           "\"name\" : \"room 1\"," \
           "\"users\" : [ ]," \
           "\"messages\" : [ ]" \
           "}"

'''
room_dict = {
    'id': 1,
    'name': "room 1",
    'users': [
        {
            'id': 1,
            'username': "Nima",
        },
        {
            'id': 2,
            'username': "Per Gynt"
        },
    ],
    'messages': [
        {
            'id': 1,
            'sender': "Per Gynt",
            'content': {
                'message': "Jeg er som en løkke!",
                'action': "er"
            },
            'timestamp': None,
            'type': "CHAT"
        },
        {
            'id': 2,
            'sender': "Nima",
            'content': {
                'message': "Det er du, kanskje",
                'action': "er"
            },
            'timestamp': None,
            'type': "CHAT"
        }
    ]
}

room_json = json.dumps(room_dict, indent=4)
print(room_json)

json_str = """
{
    "name": "room 1",
    "users": [
        {
            "id": 1,
            "username": "Nima"
        },
        {
            "id": 2,
            "username": "Per Gynt"
        }
    ],
    "messages": [
        {
            "id": 1,
            "sender": "Per Gynt",
            "content": {
                "message": "Jeg er som en l\u00f8kke!",
                "action": "er"
            },
            "timestamp": null,
            "type": "CHAT"
        },
        {
            "id": 2,
            "sender": "Nima",
            "content": {
                "message": "Det er du, kanskje",
                "action": "er"
            },
            "timestamp": null,
            "type": "CHAT"
        }
    ]
}
"""
# print(json_str)
obj = json.loads(json_str)
print(type(obj))

room1 = Chatroom.json_to_room(json_str)
print(room1)
