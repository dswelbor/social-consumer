"""
This is a simple script to consume the (reddit) API, build the appropriate 
collections, and export the data in a human readable format.
"""

from consumer import Consumer
from models import Forum, Post

# Instantiate a Consumer object to consume data from reddit api
social_consumer = Consumer()

# Get lists of posts
oc_posts = social_consumer.get_oc_submissions()
hi_comment_posts = social_consumer.get_hi_comment_submissions()
upvoted_posts = social_consumer.get_upvoted_submissions()
unique_forums = social_consumer.get_unique_subreddits()
recurring_forums = social_consumer.get_recurring_subreddits()
# Create multireddit of recurring subreddits
social_consumer.create_multireddit()

# Print collection lengths
print(len(oc_posts))
print(len(hi_comment_posts))
print(len(upvoted_posts))
print (len(unique_forums))
print (len(recurring_forums))