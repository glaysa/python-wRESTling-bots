from typing import List

from data.models import User, Chatroom as Room

# test users
user1 = User(username="Alex", personality="grumpy")
user2 = User(username="Helena", personality="annoying")
user3 = User(username="Edward", personality="sweet")
user4 = User(username="Anna", personality="energetic")

user_list: List[User] = [user1, user2, user3, user4]
room_list: List[Room] = []
