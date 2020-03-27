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
hot_submissions = list(popular.hot(limit=submission_qty))

# Populate list of OC content
oc_submissions = []
for submission in hot_submissions:
    if submission.is_original_content:
        oc_submissions.append(submission)

# Get highly commented submissions
hi_comment_submissions = []
for submission in hot_submissions:
    if submission.num_comments > comments_threshold:
        hi_comment_submissions.append(submission)

# Get upvoted submissions descending
upvoted_submissions = hot_submissions[:] # create a shallow copy of list
# Sort hot submissions by upvote score
upvoted_submissions.sort(key=lambda sub: getattr(sub, 'score'), reverse=True )
top10_upvoted_submissions = upvoted_submissions[0:10] # Get top10 list

# Get unique subreddits
unique_subreddits = []
for submission in hot_submissions:
    # print(submission.subreddit)
    if submission.subreddit not in unique_subreddits:
        unique_subreddits.append(submission.subreddit)




# print summaries
print(f'Number of OC submission: {len(oc_submissions)}')
print(f'Number of highly commented submissions: {len(hi_comment_submissions)}')
print(f'Number of top 10 hot submissions: {len(top10_upvoted_submissions)}')
for test in top10_upvoted_submissions:
    print(test.score)
print(f'Number of unique subreddits in hot submissions: {len(unique_subreddits)}')
for sub in unique_subreddits:
    print(sub)
    