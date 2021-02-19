from passlib.hash import sha256_crypt

USERS = 'users'


class UserDb():
    def __init__(self, db):
        self.db = db

    def username_available(self, username):
        return self.db[USERS].find_one(username=username) is None

    def save(self, username, password):
        hash_password = sha256_crypt.encrypt(password)

        data = dict(username=username, password=hash_password)
        self.db[USERS].insert(data)

    def valid_password(self, username, password):
        current = self.db[USERS].find_one(username=username)
        return sha256_crypt.verify(password, current['password'])
