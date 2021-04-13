from data.models import Message, Content, User
from data.json_deserializer import *
from dataclasses import asdict

sndr = User(username="Nima", personality="annoying")
cnt = Content(message="let's play football.", action="Play")
msg = Message(sender=sndr, content=cnt)

print(msg)

msg_dct = asdict(msg)
print(msg_dct)

msgs_asdict = {
    'message': msg_dct,
}
print(msgs_asdict['message']['content']['action'])
