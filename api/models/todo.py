from api.database import db
from datetime import datetime

class Todo(db.Model):
    __table_name__ = 'todos'

    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    title = db.Column(db.String(100), nullable=False)
    content = db.Column(db.Text, nullable=False)
    createdAt = db.Column(db.DateTime, nullable=False, default=datetime.now)
    updatedAt = db.Column(db.DateTime, nullable=False, default=datetime.now)
    finish = db.Column(db.Boolean ,nullable=False, default=False )
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'))
    user = db.relationship('User', backref='user')

    def update(self, title, content,finish):
        if title:
            self.title = title
        if content:
            self.content = content
        if finish:
            self.finish = finish
        self.updatedAt = datetime.now()
        return self

    def __repr__(self):
        return f"<Todo('{self.id}', '{self.title}', '{self.content}')>"

    def serialize(self):
        return {
            'id': self.id,
            'user': self.user_id,
            'title': self.title,
            'content': self.content,
            'finish':self.finish,
            'createdAt': self.createdAt.strftime('%y-%m-%d %H:%M'),
            'updatedAt': self.updatedAt.strftime('%y-%m-%d %H:%M')
        }