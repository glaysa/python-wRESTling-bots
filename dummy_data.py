users = {
    1: {
        "name": "alex",
        "personality": "grumpy"
    },
    2: {
        "name": "helena",
        "personality": "annoying"
    },
    3: {
        "name": "edward",
        "personality": "sweet"
    },
    4: {
        "name": "carlos",
        "personality": "shy"
    },
    5: {
         "name": "anna",
         "personality": "energetic"
    },
}

messages = {
    1: {
        "sender": users[1],
        "content": {
            "message": "Let's play",
            "actions": "play"
        }
    },
    2: {
        "sender": users[2],
        "content": {
            "message": "Let's swim",
            "actions": "swim"
        }
    },
    3: {
        "sender": users[3],
        "content": {
            "message": "Let's dance",
            "actions": "dance"
        }
    },
    4: {
        "sender": users[4],
        "content": {
            "message": "Let's cook",
            "actions": "cook"
        }
    },
    5: {
        "sender": users[5],
        "content": {
            "message": "Let's fight",
            "actions": "fight"
        }
    }
}

rooms = {
    1: {
        "name": "room 1",
        "users": {
            1: users[1],
            2: users[2]
        },
        "messages": [messages[1], messages[2]]
    },
    2: {
        "name": "room 2",
        "users": {
            3: users[3],
            4: users[4]
        },
        "messages": [messages[1]]
    },
    3: {
        "name": "room 3",
        "users": {5: users[5]},
        "messages": [messages[5]]
    },
    4: {
        "name": "room 4",
        "users": {4: users[4]},
        "messages": [messages[4]]
    },
    5: {
        "name": "room 5",
        "users": {},
        "messages": {}
    },
}
