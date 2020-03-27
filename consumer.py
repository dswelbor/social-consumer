"""
This script consumes data from the reddit api and returns that 
deserialized data
"""

import praw

# parameters
submission_qty = 100  # Number of posts to pull from api
comments_threshold = 1000  # Target number of comments

# Initialize python reddit api wrapper for r/popular subreddit
reddit = praw.Reddit()
popular = reddit.subreddit('popular')

# Get top 100 hot submissions
hot_submissions = popular.hot(limit=submission_qty)
# Populate list of OC content
oc_submissions = []  # hot_submissions.filters.add(is_original_content=True)
for submission in hot_submissions:
    if submission.is_original_content:
        oc_submissions.append(submission)

# Get highly comment submissions
hot_submissions = popular.hot(limit=submission_qty)
hi_comment_submissions = []
for submission in hot_submissions:
    print(submission.num_comments)
    if submission.num_comments > comments_threshold:
        hi_comment_submissions.append(submission)

print(f'Number of OC submission: {len(oc_submissions)}')
print(f'Number of highly commented submissions: {len(hi_comment_submissions)}')
