# project/tests/test_user.model.py

# project/tests/test_user_model.py


from sqlalchemy.exc import IntegrityError

from project import db
from project.api.models import User
from project.tests.base import BaseTestCase
from project.tests.utils import add_user

class TestUserModel(BaseTestCase):

    def test_add_user(self):
        user = add_user('justatest', 'test@test.com', 'test') # added pass
        self.assertTrue(user.id)
        self.assertEqual(user.username, 'justatest')
        self.assertEqual(user.email, 'test@test.com')
        self.assertTrue(user.password)
        self.assertTrue(user.active)
        self.assertTrue(user.created_at)
        
    # Continuing on... Part 3 Lession 4
    def test_encode_auth_token(self):
        user = add_user('justatest', 'test@test.com', 'test')       
        auth_token = user.encode_auth_token(user.id)                # added password...continuing onward
        print(auth_token)                                           # auth
        self.assertTrue(isinstance(auth_token, bytes))
        
    def test_decode_auth_token(self):
        user = add_user('justatest', 'test@test.com', 'test')
        auth_token = user.encode_auth_token(user.id)
        self.assertTrue(isinstance(auth_token, bytes))
        self.assertTrue(User.decode_auth_token(auth_token), user.id)

    def test_add_user_duplicate_username(self):
        add_user('justatest', 'test@test.com', 'test') # added pass
        duplicate_user = User(
            username='justatest',
            email='test@test2.com',                     # added pass
            password='test'
        )
        db.session.add(duplicate_user)
        self.assertRaises(IntegrityError, db.session.commit)

    def test_add_user_duplicate_email(self):
        add_user('justatest', 'test@test.com', 'test')   # added pass
        duplicate_user = User(
            username='justatest2',
            email='test@test.com',
            password='test'                              # added pass
        )
        db.session.add(duplicate_user)
        self.assertRaises(IntegrityError, db.session.commit)
        
    def test_passwords_are_random(self):
        user_one = add_user('justatest', 'test@test.com', 'test')   # added pass
        user_two = add_user('justatest2', 'test@test2.com', 'test') # added pass
        self.assertNotEqual(user_one.password, user_two.password)
        
        
    