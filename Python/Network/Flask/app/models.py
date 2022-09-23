from flask_sqlalchemy import SQLAlchemy
from datetime import datetime
from main import db


class Post(db.Model):
    __tablename__ = 'posts'
    id = db.Column(db.Integer(), primary_key=True)
    title = db.Column(db.String(255), nullable=False)
    slug = db.Column(db.String(255), nullable=False)
    author = db.Column(db.Integer, db.ForeignKey('user.id'))
    content = db.Column(db.Text(), nullable=False)
    created_on = db.Column(db.DateTime(), default=datetime.utcnow)
    updated_on = db.Column(db.DateTime(), default=datetime.utcnow, onupdate=datetime.utcnow)

    def __repr__(self):
        return f"id: {self.id}, title: {self.title[:10]}, slug: {self.slug}, content: {self.content}, " \
               f"created_on: {self.created_on}"


class User(db.Model):
    #__tablename__ = 'users'
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String, unique=True, nullable=False)
    email = db.Column(db.String, unique=True, nullable=False)
    number = db.Column(db.String(255))

    def __repr__(self):
        return f"user: {self.username}, email: {self.email}"


if __name__ == "__main__":
    db.create_all()
    #db.session.add(User(username="Egor", email="atomic14@mail.ru"))
    db.session.add(Post(title='Rise', slug='Nice', content='I love rise', author=1))
    db.session.commit()

    users = User.query.all()
    print(users)
    posts = Post.query.all()
    print(posts)
