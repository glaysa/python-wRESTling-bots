from flask_restful import abort


def abort_if_not_exists(obj_id: int, obj_list: iter, abort_message: str):
    if len(obj_list) < 0:
        abort(404, message="List is currently empty")
    if obj_id not in obj_list:
        abort(404, message=abort_message)


def abort_if_exists(obj_id: int, obj_list: iter, abort_message: str):
    if len(obj_list) < 0:
        abort(404, message="List is currently empty")
    if obj_id in obj_list:
        abort(409, message=abort_message)
