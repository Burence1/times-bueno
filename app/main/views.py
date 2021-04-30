from .forms import AddBlog,AddComment,AddSubscriber
from flask import url_for,request,redirect,render_template,abort,flash
from . import main
from ..models import User,Blog,Comment,Subscribe
from flask_login import current_user,login_required
from .. import db


@main.route('/')
def index():
  '''
  home/landing page
  '''
  blogs=Blog.query.all()
  recent=Blog.query.order_by(Blog.posted_on.desc()).all()

  title="Times Bueno"
  return render_template('index.html',blogs=blogs,recent=recent,title=title)