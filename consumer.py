"""
This script consumes data from the reddit api and returns that 
deserialized data
"""

import praw

# parameters
submission_qty = 100  # Number of posts to pull from api
comments_qty = 1000  # Target number of comments

# Initialize python reddit api wrapper for r/popular subreddit
reddit = praw.Reddit()
popular = reddit.subreddit('popular')

# Get top 100 hot posts
hot_submissions = popular.hot(limit=submission_qty)
# Populate list of OC content
oc_submissions = []  # hot_submissions.filters.add(is_original_content=True)
for submission in hot_submissions:
    if submission.is_original_content:
        oc_submissions.append(submission)


print(len(oc_submissions))

