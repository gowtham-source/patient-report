import streamlit_authenticator as stauth

import database as db


# usernames = ["pparker", "rmiller", 'gowtham205']
# names = ["Peter Parker", "Rebecca Miller", 'gowtham']
# passwords = ["abc123", "def456", 'asdfs854']
# hashed_passwords = stauth.Hasher(passwords).generate()


# for (username, name, hash_password) in zip(usernames, names, hashed_passwords):
#     db.insert_user(username, name, hash_password)

# users = db.fetch_all_users()
# print(users)


def signup(name, username, password):
    usernames = [username]
    names = [name]
    passwords = [password]
    hashed_passwords = stauth.Hasher(passwords).generate()

    for (username, name, hash_password) in zip(usernames, names, hashed_passwords):
        db.insert_user(username, name, hash_password)


# signup('karthi', 'karthi11', 'aed256')
