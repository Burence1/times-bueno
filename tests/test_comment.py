import unittest
from app.models import Blog, User, Comment
from app import db


class CommentModelTest(unittest.TestCase):
    def setUp(self):
        self.new_comment = Comment(contents='contents')
        db.session.add(self.new_comment)
        db.session.commit()

    def tearDown(self):
        Comment.query.delete()
        Blog.query.delete()
        User.query.delete()
        db.session.commit()

    def test_save_comment(self):
        self.new_comment.save_comments()
        self.assertTrue(len(Comment.query.all()) > 0)

    def test_check_instance_variables(self):
        self.assertEquals(self.new_comment.contents, 'contents')

    def test_get_comment_by_id(self):
        self.new_comment.save_comments()
        comment = Comment.get_comments(1)
        self.assertEquals(self.new_comment.contents, 'contents')