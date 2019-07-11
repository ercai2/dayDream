from datetime import datetime

from daydream import db


# 用户表
class User(db.Model):
	id = db.Column(db.Integer, primary_key=True)
	nickname = db.Column(db.String(12))
	messages = db.relationship('Message', back_populates='user')

# 星愿表
class Message(db.Model):
	id = db.Column(db.Integer, primary_key=True)
	body = db.Column(db.String(50))
	timestamp = db.Column(db.DateTime, default=datetime.now, index=True)
	nick_id = db.Column(db.Integer, db.ForeignKey('user.id'))
	user = db.relationship('User', back_populates='messages')