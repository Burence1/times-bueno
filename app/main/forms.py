from wtforms import TextAreaField,StringField,SubmitField
from .. models import Blog,User,Comment,Subscribe
from wtforms.validators import Required
from flask_wtf import FlaskForm
from flask_login import current_user

class AddBlog(FlaskForm):
  title=TextAreaField("Blog Title",validators=[Required()])
  contents=TextAreaField("Write your blog",validators=[Required()])
  submit=SubmitField("Upload Blog")

class AddComment(FlaskForm):
  contents=TextAreaField("Write a comment",validators=[Required()])
  submit=SubmitField("Post comment")

class AddSubscriber(FlaskForm):
  name=StringField("Enter your name",validators=[Required()])
  email=StringField("Enter your email",validators=[Required()])
  submit=SubmitField("Subscribe")