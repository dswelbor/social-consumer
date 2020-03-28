"""
This script consumes data from the reddit api and returns that 
deserialized data
"""

import praw

# parameters
SUBMISSION_QTY = 100  # Number of posts to pull from api
COMMENT_THRESHOLD = 1000  # Target number of comments

# Initialize python reddit api wrapper for r/popular subreddit
reddit = praw.Reddit()
popular = reddit.subreddit('popular')
# Get top 100 hot submissions
hot_submissions = list(popular.hot(limit=SUBMISSION_QTY))

# Populate list of OC content
oc_submissions = []
for submission in hot_submissions:
    if submission.is_original_content:
        oc_submissions.append(submission)

# Get highly commented submissions
hi_comment_submissions = []
for submission in hot_submissions:
    if submission.num_comments > COMMENT_THRESHOLD:
        hi_comment_submissions.append(submission)

# Get upvoted submissions descending
upvoted_submissions = hot_submissions[:] # create a shallow copy of list
# Sort hot submissions by upvote score
upvoted_submissions.sort(key=lambda sub: getattr(sub, 'score'), reverse=True)
top10_upvoted_submissions = upvoted_submissions[0:10] # Get top10 list

# Get unique subreddits
unique_subreddits = []
for submission in hot_submissions:
    # print(submission.subreddit)
    if submission.subreddit not in unique_subreddits:
        unique_subreddits.append(submission.subreddit)

# Get recurring subreddits
seen_subreddits = {}  # dictionary for seen subreddits
recurring_subreddits = []
for submission in hot_submissions:
    try:
        # This subredit has already been seen at least once
        seen_subreddits[submission.subreddit] += 1 # increment count

        if seen_subreddits[submission.subreddit] == 2:
            # First time subreddit has been seen more than once
            recurring_subreddits.append(submission.subreddit) # add to list

    except KeyError:
        # First time seeing this subreddit
        seen_subreddits[submission.subreddit] = 1

# Create a multireddit with recurring subreddits
new_multireddit = reddit.multireddit.create(display_name='testing1236', 
    subreddits=recurring_subreddits)




# print summaries
print(f'Number of OC submission: {len(oc_submissions)}')
print(f'Number of highly commented submissions: {len(hi_comment_submissions)}')
print(f'Number of top 10 hot submissions: {len(top10_upvoted_submissions)}')
for test in top10_upvoted_submissions:
    print(test.score)
print(f'Number of unique subreddits in hot submissions: {len(unique_subreddits)}')
print(f'Number of recurring subreddits in hot submissions: {len(recurring_subreddits)}')
print(new_multireddit)