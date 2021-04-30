from wtforms import TextAreaField,StringField,SubmitField
from .. models import Blog,User,Comment,Subscribe
from wtforms.validators import Required
from flask_wtf import FlaskForm
from flask_wtf.file import FileAllowed,FileRequired,FileField
from flask_login import current_user
from ..import db,photos

class AddBlog(FlaskForm):
  title=TextAreaField("Blog Title",validators=[Required()])
  photo=FileField(validators=[FileAllowed(photos,'Image only!'),FileRequired('File ws empty')])
  contents=TextAreaField("Write your blog",validators=[Required()])
  submit=SubmitField("Upload Blog")

class AddComment(FlaskForm):
  contents=TextAreaField("Write a comment",validators=[Required()])
  submit=SubmitField("Post comment")

class AddSubscriber(FlaskForm):
  name=StringField("Enter your name",validators=[Required()])
  email=StringField("Enter your email",validators=[Required()])
  submit=SubmitField("Subscribe")