from typing import List

from data.models import User, Chatroom as Room

# test users
user1 = User(username="Alex", personality="grumpy")
user2 = User(username="Helena", personality="annoying")
user3 = User(username="Edward", personality="sweet")
user4 = User(username="Anna", personality="energetic")

room1 = Room(name="Grumpy Room", creator=user1, users=[user1])
room2 = Room(name="Annoying Room", creator=user2, users=[user2])
room3 = Room(name="Sweet Room", creator=user3, users=[user3])
room4 = Room(name="Energetic Room", creator=user4, users=[user4])

user_list: List[User] = [user1, user2, user3, user4]
room_list: List[Room] = [room1, room2, room3, room4]

