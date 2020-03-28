"""
This module provides datastructure models for imported data from the reddit
API
"""

class Post:
    """Class defines a model for social media posts"""
    def __init__(self, title, url, upvotes=0, comment_count=0):
        """Parameterized ctor with default values for upvotes and comments"""
        self.title = title
        self.url = url
        self.upvotes = upvotes
        self.comment_count = comment_count

class Forum:
    """Class defines a model for forums and subforums on social media"""
    def __init__(self, title, url, description=None):
        """Parameterized ctor for default values for description"""
        self.title = title
        self.url = url