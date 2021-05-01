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
  username=db.Column(db.String(50),index=True)
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
  blog_id=db.Column(db.Integer,db.ForeignKey("blogs.id"))

  def save_comments(self):
    db.session.add(self)
    db.session.commit()

  def delete_comment(self):
    db.session.delete(self)
    db.session.commit()

  @classmethod
  def get_comments(cls,id):
    comments=Comment.query.filter_by(blog_id=id).order_by(Comment.posted_on.desc())
    return comments
  
  @classmethod
  def get_comment(cls,id):
    comment=Comment.query.filter_by(id=id).first()
    return comment

  def __repr__(self):
    return f"Comment {self.contents}"

class Blog(db.Model):
  __tablename__='blogs'

  id=db.Column(db.Integer,primary_key=True)
  title=db.Column(db.String(150))
  image_pic_path = db.Column(db.String(255))
  contents=db.Column(db.String())
  posted_on=db.Column(db.DateTime,default=datetime.utcnow)
  user_id=db.Column(db.Integer,db.ForeignKey("users.id"))
  comments=db.relationship("Comment",backref='blog',lazy='dynamic')

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
  
  @classmethod
  def all_blogs(cls):
    blogs=Blog.query.all()
    return blogs
  @classmethod
  def get_user_blogs(cls,id):
    blogs=Blog.query.filter_by(user_id=id).all()
    return blogs

  def __repr__(self):
    return f"Blog {self.title}:{self.contents}"

class Subscribe(db.Model):
  __tablename__='subscribes'

  id =db.Column(db.Integer,primary_key=True)
  email=db.Column(db.String(255),unique=True)

  def save_subscriber(self):
    db.session.add(self)
    db.session.commit()

  def delete_subscriber(self):
    db.session.delete(self)
    db.session.commit()

  def __repr__(self):
    return f"Subscribe {self.email}"


class Quote:
  '''
  Quote class that defines quotes instances
  '''
  def __init__(self,id,author,quote):

    self.id=id
    self.author=author
    self.quote=quote