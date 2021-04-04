from models.user import User
from models.message import Message, Content
from models.chatroom import Chatroom
import json

users = [
    User(username="alex", personality="grumpy").to_dictionary(),
    User(username="helena", personality="annoying").to_dictionary(),
    User(username="edward", personality="sweet").to_dictionary(),
    User(username="carlos", personality="shy").to_dictionary(),
    User(username="anna", personality="energetic").to_dictionary(),
]

messages = [
    Message(sender=users[0], content=Content(message="Let's play", action="play"), type="CHAT"),
    Message(sender=users[1], content=Content(message="Let's swim", action="swim"), type="CHAT").to_dictionary(),
    Message(sender=users[2], content=Content(message="Let's dance", action="dance"), type="CHAT").to_dictionary(),
    Message(sender=users[3], content=Content(message="Let's cook", action="cook"), type="CHAT").to_dictionary(),
    Message(sender=users[4], content=Content(message="Let's fight", action="fight"), type="CHAT").to_dictionary(),
]

rooms = [
    Chatroom(name="Room 1", users=[users[0], users[1]], messages=[messages[0], messages[1]]).to_dictionary(),
    Chatroom(name="Room 2", users=[users[2], users[3]], messages=[messages[2], messages[3]]).to_dictionary(),
    Chatroom(name="Room 3", users=[users[4]], messages=[messages[4]]).to_dictionary(),
    Chatroom(name="Room 5").to_dictionary(),
]

