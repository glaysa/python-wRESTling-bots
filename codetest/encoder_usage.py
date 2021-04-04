from models.user import User
from models.message import Message, Content
from models.chatroom import Chatroom
import json
from models.json_serializer import ModelEncoder

print("###############MSG###################")

msg1 = Message(sender="alex", content=Content(message="Let's swim", action="swim"), msg_type="CHAT")
json_msg1 = json.dumps(msg1, cls=ModelEncoder, indent=4)
print(json_msg1)

msg2 = Message(sender="helena", content=Content(message="Let's play", action="play"), msg_type="CHAT")
json_msg2 = json.dumps(msg2,cls=ModelEncoder, indent=4)
print(json_msg2)

print("###############User###################")

usr1 = User(username="alex", personality="grumpy")
json_usr1 = json.dumps(usr1, cls=ModelEncoder, indent=4)
print(json_usr1)

usr2 = User(username="helena", personality="annoying")
json_usr2 = json.dumps(usr2, cls=ModelEncoder, indent=4)
print(json_usr2)

print("###############Room###################")

room1 = Chatroom(name="Room 1", users=[usr1, usr2], messages=[msg1, msg2])
json_room1 = json.dumps(room1, cls=ModelEncoder, indent=4)
print(json_room1)
room2 = Chatroom(name="Room 5")
json_room2 = json.dumps(room2, cls=ModelEncoder, indent=4)
print(json_room2)



