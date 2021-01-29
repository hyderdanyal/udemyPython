from models.user import UserModel

def authenticate(username, password):
    #user = username_mapping.get(username, None)
    user = UserModel.find_by_username(username)
    user.password = ''.join(user.password)
    if user and user.password == password:
        return user


def identity(payload):  #jwt defined function
    user_id = payload['identity']
    return UserModel.find_by_id(user_id)
