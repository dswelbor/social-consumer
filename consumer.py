"""
This module defines and implements class(es) to provide functionality for 
consuming the reddit api.
"""

import praw
from models import Forum, Post

class Consumer:
    """A class to implement api consumption functionality"""
    # parameters
    QTY = 100  # Number of posts to pull from api
    COMMENT_THRESHOLD = 1000  # Target number of comments
    TOP_QTY = 10  # Number for topX collections
    MULTIREDDIT_NAME = 'top100recurring'

    def __init__(self):
        """Simple constructor with defaults from praw config"""
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
                        description=submission.subreddit.public_description)
                    # Add to list
                    recurring_subreddits.append(new_forum)

            except KeyError:
                # First time seeing this subreddit
                seen_subreddits[submission.subreddit] = 1

        # Return list of recurring Forums (subreddits)
        return recurring_subreddits

    def create_multireddit(self):
        """This method creates a multi-reddit from a list of recurring subreddits"""
        # Get recurring subreddits
        seen_subreddits = {}  # dictionary for seen subreddits
        recurring_subreddits = []
        for submission in self.hot_submissions:
            try:
                # This subredit has already been seen at least once
                seen_subreddits[submission.subreddit] += 1 # increment count

                if seen_subreddits[submission.subreddit] == 2:
                    # First time subreddit has been seen more than once
                    recurring_subreddits.append(submission.subreddit)

            except KeyError:
                # First time seeing this subreddit
                seen_subreddits[submission.subreddit] = 1
        # Create a multireddit with recurring subreddits
        new_multireddit = self.reddit.multireddit.create(display_name=self.MULTIREDDIT_NAME, 
           subreddits=recurring_subreddits)
        
        return str(new_multireddit)
