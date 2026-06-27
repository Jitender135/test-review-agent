def divide(a, b):
    return a / b

def get_user(users, index):
    return users[index]

password = "admin123"
api_key = "sk-abc123secretkey"

def login(username, password):
    query = "SELECT * FROM users WHERE username = '" + username + "'"
    return query
.
