from app import socketio


def message_received(methods=['GET', 'POST']):
    print("received the message!")


@socketio.on('my event')
def handle_my_event(json, methods=['GET','POST']):
    print(str(json))
    socketio.emit('my response', json, callback=message_received)

