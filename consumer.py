"""
This script consumes data from the reddit api and returns that 
deserialized data
"""

import praw
from models import Forum, Post

class Consumer:
    # parameters
    QTY = 100  # Number of posts to pull from api
    COMMENT_THRESHOLD = 1000  # Target number of comments
    TOP_QTY = 10  # Number for topX collections

    def __init__(self):
        # Initialize python reddit api wrapper for r/popular subreddit
        self.reddit = praw.Reddit()
        self.popular = self.reddit.subreddit('popular')

        # Get top 100 hot submissions
        self.hot_submissions = list(self.popular.hot(limit=self.QTY))

    def get_oc_submissions(self):
        """
        Utility method returns a list of orginal content Posts from hot 
        submissions.
        """
        oc_submissions = []
        for submission in self.hot_submissions:
            if submission.is_original_content:
                # Translate Submission into a post and append to list
                new_post = Post(
                    title=submission.title, 
                    url=submission.permalink,
                    upvotes=submission.score, 
                    comment_count=submission.num_comments)
                oc_submissions.append(new_post)
        
        # Return oc list
        return oc_submissions

    def get_hi_comment_submissions(self):
        """
        Utility method returns a list of Posts with high comment counts.
        """
        hi_comment_submissions = []
        for submission in self.hot_submissions:
            if submission.num_comments > self.COMMENT_THRESHOLD:
                # Translate Submission into a Post and append to list
                new_post = Post(
                    title=submission.title, 
                    url=submission.permalink,
                    upvotes=submission.score, 
                    comment_count=submission.num_comments)
                hi_comment_submissions.append(new_post)

        # Return list of Posts with high comment counts
        return hi_comment_submissions

    def get_upvoted_submissions(self):
        """
        Utility method returns a list of top 10 upvoted Submissions in descending 
        order.
        """
        # Get upvoted submissions descending
        upvoted_submissions = self.hot_submissions[:] # create a shallow copy of list
        # Sort hot submissions by upvote score
        upvoted_submissions.sort(
            key=lambda sub: getattr(sub, 'score'), 
            reverse=True)
        # Get top10 list
        top_upvoted_submissions = []
        for submission in upvoted_submissions[0:self.TOP_QTY]:
            # Translate Submission into a Post and append to list
            new_post = Post(
                    title=submission.title, 
                    url=submission.permalink,
                    upvotes=submission.score, 
                    comment_count=submission.num_comments)
            top_upvoted_submissions.append(new_post)

        # Return a list of top 10 Submissions
        return top_upvoted_submissions

    def get_unique_subreddits(self):
        """
        Utility method returns a list of unique Forums aka subreddits 
        in top 100 'hot' Submissions of r/popular.
        """
        unique_subreddits = []
        seen_subreddits = []
        for submission in self.hot_submissions:
            if submission.subreddit not in seen_subreddits:
                # List subreddit as seen
                seen_subreddits.append(submission.subreddit)
                # Translate subreddit into Forum and append to list
                new_forum = Forum(
                    title=submission.subreddit.display_name, 
                    url=submission.subreddit.id,
                    description=submission.subreddit.public_description)
                unique_subreddits.append(new_forum)

        # Return list of unique Forums (subreddits)
        return unique_subreddits

    def get_recurring_subreddits(self):
        """
        Utility method returns a list of recurring Forums aka subreddits 
        in top 100 'hot' Submissions of r/popular
        """
        # Get recurring subreddits
        seen_subreddits = {}  # dictionary for seen subreddits
        recurring_subreddits = []
        for submission in self.hot_submissions:
            try:
                # This subredit has already been seen at least once
                seen_subreddits[submission.subreddit] += 1 # increment count

                if seen_subreddits[submission.subreddit] == 2:
                    # First time subreddit has been seen more than once
                    new_forum = Forum(
                        title=submission.subreddit.display_name, 
                        url=submission.subreddit.id,
                        description=submission.subreddit.public_description)
                    # Add to list
                    recurring_subreddits.append(new_forum)

            except KeyError:
                # First time seeing this subreddit
                seen_subreddits[submission.subreddit] = 1

        # Return list of recurring Forums (subreddits)
        return recurring_subreddits
"""
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
"""
"""
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
# new_multireddit = reddit.multireddit.create(display_name='testing1236', 
#    subreddits=recurring_subreddits)


"""
"""
# print summaries
print(f'Number of OC submission: {len(oc_submissions)}')
print(f'Number of highly commented submissions: {len(hi_comment_submissions)}')
print(f'Number of top 10 hot submissions: {len(top10_upvoted_submissions)}')
for test in top10_upvoted_submissions:
    print(test.score)
print(f'Number of unique subreddits in hot submissions: {len(unique_subreddits)}')
"""
# print(f'Number of recurring subreddits in hot submissions: {len(recurring_subreddits)}')
# print(new_multireddit)

"""
## Create a list of Posts
test_posts = []
for post in top10_upvoted_submissions:
    test_posts.append(Post(title=post.title, url=post.permalink, upvotes=post.score, comment_count=post.num_comments))

print('test')
for test_post in test_posts:
    print(f'title: {test_post.title} \nurl: {test_post.url} \nupvotes: {test_post.upvotes} \ncomments: {test_post.comment_count}')
"""