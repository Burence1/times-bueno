import unittest
from app.models import Blog
from app import db

class PitchModelTest(unittest.TestCase):
    def setUp(self):
        self.new_blog = Blog(title="title", contents="description", image_pic_path="photo_url")
        db.session.add(self.new_blog)
        db.session.commit()

    def tearDown(self):
        Blog.query.delete()
        db.session.commit()

    def test_save_blogs(self):
        self.new_blog.save_blogs()
        self.assertTrue(len(Blog.query.all()) > 0)

    def test_check_instance_variables(self):
        self.assertEquals(self.new_blog.title, 'title')
        self.assertEquals(self.new_blog.contents, 'description')
        self.assertEquals(self.new_blog.image_pic_path, 'photo_url')