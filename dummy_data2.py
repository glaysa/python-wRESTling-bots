from models.user import User
from models.message import Message, Content
from models.chatroom import Chatroom

users = [
    User.to_dictionary(User(username="alex", personality="grumpy")),
    User.to_dictionary(User(username="helena", personality="annoying")),
    User.to_dictionary(User(username="edward", personality="sweet")),
    User.to_dictionary(User(username="carlos", personality="shy")),
    User.to_dictionary(User(username="anna", personality="energetic")),
]

messages = [
    Message.to_dictionary(Message(sender=users[0], content=Content(message="Let's play", action="play"), msg_type="CHAT")),
    Message.to_dictionary(Message(sender=users[1], content=Content(message="Let's swim", action="swim"), msg_type="CHAT")),
    Message.to_dictionary(Message(sender=users[2], content=Content(message="Let's dance", action="dance"), msg_type="CHAT")),
    Message.to_dictionary(Message(sender=users[3], content=Content(message="Let's cook", action="cook"), msg_type="CHAT")),
    Message.to_dictionary(Message(sender=users[4], content=Content(message="Let's fight", action="fight"), msg_type="CHAT")),
]

rooms = [
    Chatroom.to_dictionary(Chatroom(name="Room 1", users=[users[0], users[1]], messages=[messages[0], messages[1]])),
    Chatroom.to_dictionary(Chatroom(name="Room 2", users=[users[2], users[3]], messages=[messages[2], messages[3]])),
    Chatroom.to_dictionary(Chatroom(name="Room 3", users=[users[4]], messages=[messages[4]])),
    Chatroom.to_dictionary(Chatroom(name="Room 5")),
]

