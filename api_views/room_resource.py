from flask import request, redirect, url_for, render_template, session, flash
from flask_restful import Resource
from api_views import room_list
from data.json_serializer import asdict
from data.models import Chatroom as Room


# Shows a single room
class SingleRoom(Resource):

    def get(self, room_id: str = None):
        for room in room_list:
            if room.room_id == room_id:
                return asdict(room)
        return {"message": "Room not found"}, 404

    # Deletes a room
    def post(self, room_id: str = None):
        for room in room_list:
            if room.room_id == room_id:
                room_list.remove(room)
                flash(f"Room '{room.name}' has been deleted")
                return redirect(url_for('get_home'))
        return {"message": "Room not found"}, 404


# Shows a list of rooms
class RoomList(Resource):

    def get(self):
        return [asdict(room) for room in room_list]

    def post(self):
        if request.method == 'POST':
            room_name = request.form['room_name']
            creator = session['user']
            room = Room(name=room_name, creator=creator, users=[creator])
            room_list.append(room)
            status_msg = room_name
            return redirect(url_for('get_home', msg=status_msg))

        status_msg = "Cannot create room, please try again!"
        return render_template('home.html', msg=status_msg)
