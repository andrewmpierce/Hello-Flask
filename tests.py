import unittest
from hello_flask import hello_world
from models import User, Tweet

class TestModels(unittest.TestCase):

    def test_user(self):
        user = User("Andrew", "andrew@andrew.com")
        self.assertEqual(user.username, "Andrew")
        self.assertEqual(user.email, "andrew@andrew.com")

    def test_tweet(self):
        user = User("Andrew", "andrew@andrew.com")
        tweet = Tweet("This is a tweet", user)
        self.assertEqual(tweet.text, "This is a tweet")
        self.assertEqual(tweet.author, user)

class TestViews(unittest.TestCase):
    





if __name__ == "__main__":
     unittest.main()
