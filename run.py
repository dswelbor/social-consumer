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
multireddit_result = social_consumer.create_multireddit()

# Print collection lengths
print(f'Number of Original Content Posts {len(oc_posts)}')
print(f'Number of Posts with High Comment Counts: {len(hi_comment_posts)}')
print(f'Number of top 10 most upvoted posts (descending): {len(upvoted_posts)}')
# print top most upvoted posts
for post in upvoted_posts:
    print(f'\tTitle: {post.title[:50]}')
    print(f'\tUpvotes: {post.upvotes}')
print(f'Number of "unique" subreddits in r/popular: {len(unique_forums)}')
print(f'Number of recurring subreddits in r/popular: {len(recurring_forums)}')
print(f'Multireddit: {multireddit_result}')