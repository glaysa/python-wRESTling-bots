from app import login_manager
from api_views import user_list


def get_user(username):
    user_to_return = None
    for user in user_list:
        if user.username == username:
            user_to_return = user
    return user_to_return


@login_manager.user_loader
def load_user(username):
    return get_user(username)


