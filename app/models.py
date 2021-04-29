from .import db
from flask_login import UserMixin,current_user
from werkzeug.security import generate_password_hash,check_password_hash
from datetime import datetime
from . import login_manager

@login_manager.user_loader
def load_user(user_id):
  return User.query.get(int(user_id))

class User(UserMixin,db.Model):
  __tablename__='users'

  id = db.Column(db.Integer,primary_key=True)
  username=db.Column(db.String(255),index=True)
  email=db.Column(db.String(255),unique=True)
  bio=db.Column(db.String(255))
  password_hash=db.Column(db.String(255))
  profile_pic_path = db.Column(db.String(255))
  comments=db.relationship("Comment",backref='user',lazy='dynamic')
  blogs=db.relationship("Blog",backref='user',lazy='dynamic')

  @property
  def password(self):
    raise AttributeError("cannot read password")

  @password.setter
  def password(self,password):
    self.password_hash=generate_password_hash(password)

  def password_verification(self,password):
    return check_password_hash(self.password_hash,password)

  def save_user(self):
    db.session.add(self)
    db.session.commit()

  def delete_user(self):
    db.session.delete(self)
    db.session.commit()

  def __repr__(self):
    return f"User {self.username}"

class Comment(db.Model):
  __tablename__='comments'

  id=db.Column(db.Integer,primary_key=True)
  contents=db.Column(db.String(255))
  posted_on=db.Column(db.DateTime,default=datetime.utcnow)
  user_id=db.Column(db.Integer,db.ForeignKey("users.id"))
  blogs=db.relationship("Blog",backref='comment',lazy='dynamic')

  def save_comments(self):
    db.session.add(self)
    db.session.commit()

  def delete_comment(self):
    db.session.delete(self)
    db.session.commit()

  @classmethod
  def get_comments(cls,id):
    comments=Comment.query.all(id=id)
    return comments

  def __repr__(self):
    return f"Comment {self.contents}"

class Blog(db.Model):
  __tablename__='blogs'

  id=db.Column(db.Integer,primary_key=True)
  contents=db.Column(db.String(255))
  posted_on=db.Column(db.DateTime,default=datetime.utcnow)
  user_id=db.column(db.Integer,db.ForeignKey("users.id"))
  comment_id=db.Column(db.Integer,db.ForeignKey("comments.id"))

  def save_blogs(self):
    db.session.add(self)
    db.session.commit()

  def delete_blogs(self):
    db.session.delete(self)
    db.session.commit()

  @classmethod
  def get_blogs(cls,id):
    blogs=Blog.query.filter_by(id=id).first()
    return blogs

  def __repr__(self):
    return f"Blog {self.contents}"