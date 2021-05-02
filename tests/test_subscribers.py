import unittest
from app import db
from app.models import Subscribe

class SubscribeTest(unittest.TestCase):
    def setUp(self):
        self.new_subscriber = Subscribe(email="diana@gmail.com")
        db.session.add(self.new_subscriber)
        db.session.commit()

    def tearDown(self):
        Subscribe.query.delete()
        db.session.commit()

    def test_is_instance(self):
       self.assertTrue(isinstance(self.new_subscriber, Subscribe))

    def test_save_subscriber(self):
        self.new_subscriber.save_subscriber()
        self.assertTrue(len(Subscribe.query.all()) > 0)