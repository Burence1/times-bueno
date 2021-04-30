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

@main.route('/new_blog',methods=["GET","POST"])
def new_blog():
  '''
  function to add new blogs to the application
  '''
  form=AddBlog()
  if form.validate_on_submit():
    title=form.title.data
    contents=form.contents.data
    user=current_user
    blog=Blog(title=title,contents=contents,user=user)
    blog.save_blogs()

    flash("Blog successfully saved")
    return redirect(url_for("main.index"))

  title="Add your blog"
  return render_template('new_blog.html',title=title,form=form)