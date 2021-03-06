
from db import db


class UserModel(db.Model):

    __tablename__ = 'users'

    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(80))
    password = db.Column(db.String(80))

    def __init__(self, username, password):
        self.username = username
        self.password = password

    def save_to_db(self):
        db.session.add(self)
        print(db.session)
        db.session.commit()
        print(db.session)

    @classmethod
    def find_by_username(cls, username):
        compare = cls.query.filter_by(username=username).first()
        return compare

    @classmethod
    def find_by_id(cls, _id):
        return cls.query.filter_by(id=_id).first()
