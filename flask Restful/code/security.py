from user import User

# users = [
#     {
#         'id': 1,
#         'username': 'bob',
#         'password': 'asdf'
#     }
# ]

users = [
    User(1, 'bob', 'asdf')
]

# username_mapping = {'bob': {
#         'id': 1,
#         'username': 'bob',
#         'password': 'asdf'
#     }
# }
username_mapping = {u.username: u for u in users}

# userid_mapping = {1: {
#         'id': 1,
#         'username': 'bob',
#         'password': 'asdf'
#     }
# }
userid_mapping = {u.id: u for u in users}


def authenticate(username, password):
    user = username_mapping.get(username, None)
    user.password = ''.join(user.password)
    print(str(user.password))
    if user and user.password == password:
        return user
    else:
        return "kem Cho"


def identity(payload):  #jwt defined function
    user_id = payload['identity']
    return userid_mapping.get(tuple(user_id), None)
