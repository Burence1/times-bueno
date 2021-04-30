from .forms import AddBlog,AddComment,AddSubscriber,UpdateProfile
from flask import url_for,request,redirect,render_template,abort,flash
from . import main
from ..models import User,Blog,Comment,Subscribe
from flask_login import current_user,login_required
from .. import db,photos


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
    filename=photos.save(form.photo.data)
    image_pic_path = f'photos/{filename}'
    contents=form.contents.data
    user=current_user
    blog=Blog(title=title,contents=contents,user=user,image_pic_path=image_pic_path)
    blog.save_blogs()

    flash("Blog successfully saved")
    return redirect(url_for("main.index"))

  title="Add your blog"
  return render_template('new_blog.html',title=title,form=form)

@main.route('/new_comment',methods=["GET","POST"])
def new_comment():
  form=AddComment()
  if form.validate_on_submit():
    contents=form.contents.data
    user=current_user
    comment=Comment(contents=contents,user=user)
    comment.save_comments()

    flash("Comment posted")
    return redirect(url_for('main.new_comment'))

  return render_template('new_comment.html',form=form)

@main.route('/user_blogs/<string:username>',methods=["GET","POST"])
def user_blogs(username):
  user=User.query.filter_by(username=username).first()
  blog=Blog.query.filter_by(user=user).order_by(Blog.posted_on.desc()).all()
  return render_template("profile.html",blog=blog,user=user)

@main.route('/del_comment/<blog_id>/<comment_id>',methods=["POST"])
@login_required
def delete_comment(blog_id,comment_id):
  blog=Blog.get_blogs(blog_id)
  comment=Comment.get_comment(comment_id)
  if blog.user != current_user:
    abort(404)
  blog.delete_comment()

  flash("comment deleted")
  return redirect(url_for('main.comment'))

@main.route('/del_blog/<blog_id>',methods=["POST","GET"])
@login_required
def delete_blog(blog_id):
  blog=Blog.get_blogs(blog_id)
  if blog.user != current_user:
    abort(404)
  blog.delete_blogs()
  
  flash("blog deleted")
  return redirect(url_for('main.index'))

@main.route('/update_blog/<blog_id>',methods=["GET","POST"])
@login_required
def update_blog(blog_id):
  blog=Blog.query.get_blogs(blog_id)
  if blog.user != current_user:
    abort(404)
  form=AddBlog()
  if form.validate_on_submit():
    title = form.title.data
    filename = photos.save(form.photo.data)
    image_pic_path = photos.url(filename)
    contents = form.contents.data
    user = current_user
    db.session.commit()
    flash("Blog Updated")
    return redirect(url_for('main.index',blog_id=blog_id))
  elif request.method == 'GET':
    form.title.data=blog.title
    form.contents.data=blog.contents
    title="Update blog"
    return render_template('new_blog',title=title,form=form)


@main.route('/user/<uname>')
def profile(uname):
    user = User.query.filter_by(username=uname).first()

    if user is None:
        abort(404)

    return render_template("profile/profile.html", user=user)


@main.route('/user/<uname>/update/pic', methods=['POST'])
@login_required
def update_pic(uname):
    user = User.query.filter_by(username=uname).first()
    if 'photo' in request.files:
        filename = photos.save(request.files['photo'])
        path = f'photos/{filename}'
        user.profile_pic_path = path
        db.session.commit()
    return redirect(url_for('main.profile', uname=uname))


@main.route('/user/<uname>/update', methods=['GET', 'POST'])
@login_required
def update_profile(uname):
    user = User.query.filter_by(username=uname).first()
    if user is None:
        abort(404)

    form = UpdateProfile()

    if form.validate_on_submit():
        user.bio = form.bio.data

        db.session.add(user)
        db.session.commit()

        return redirect(url_for('.profile', uname=user.username))

    return render_template('profile/update.html', form=form)


@main.route('/blogs/<blog_id>', methods=['GET', 'POST'])
@login_required
def blogs(blog_id):
    blog = Blog.get_blogs(blog_id)
    if blog is None:
        abort(404)
    all_comments = Comment.get_comments(blog.id)
    comment_form = AddComment()
    if comment_form.validate_on_submit():
        comment = Comment(contents=comment_form.contents.data,user=current_user, blog_id=blog_id)
        comment.save_comments()

        flash('Your comment has been added!', 'success')
        return redirect(url_for('main.blogs', blog_id=blog.id))
    return render_template('blog.html', blog=blog, comments=all_comments, comment_form=comment_form)