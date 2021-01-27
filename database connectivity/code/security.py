from user import User


users = [
    User(1, 'bob', 'asdf')
]

# username_mapping = {u.username: u for u in users}
# userid_mapping = {u.id: u for u in users}


def authenticate(username, password):
    #user = username_mapping.get(username, None)
    user = User.find_by_username(username)
    user.password = ''.join(user.password)
    if user and user.password == password:
        return user
    else:
        return "kem Cho"


def identity(payload):  #jwt defined function
    user_id = payload['identity']
    return User.find_by_id(tuple(user_id))
