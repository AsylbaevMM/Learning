import unittest

from seminar3.user import User
from seminar3.user_repository import UserRepository


class UserTest(unittest.TestCase):
    def test_user_logout_test(self):
        repository = UserRepository()
        repository.add_user(User("user1", "user1pass", False))
        repository.add_user(User("user2", "user2pass", False))
        repository.add_user(User("user3", "user3pass", False))
        repository.add_user(User("admin1", "admin1pass", True))
        repository.add_user(User("admin2", "admin2pass", True))
        repository.all_users_logout()
        for elem in repository.data:
            self.assertTrue(elem.admin)