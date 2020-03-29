"""
This is a simple script to consume the (reddit) API, build the appropriate 
collections, and export the data in a human readable format.
"""

import json
from consumer import Consumer
from utils import to_dict

# Define constants
OUTPUT_FILENAME = 'output.json'

# Instantiate a Consumer object to consume data from reddit api
social_consumer = Consumer()

# Get lists of posts
print('Aggregating \'original content\' posts...')
oc_posts = social_consumer.get_oc_submissions()

print('Aggregating \'high comment count\' posts...')
hi_comment_posts = social_consumer.get_hi_comment_submissions()

print('Aggregating \'most upvoted\' posts...')
upvoted_posts = social_consumer.get_upvoted_submissions()

print('Aggregating \'unique\' subreddits...')
unique_forums = social_consumer.get_unique_subreddits()

print('Aggregating \'recurring\' subreddits...')
recurring_forums = social_consumer.get_recurring_subreddits()

# Create multireddit of recurring subreddits
print('Creating multireddit with recurring subreddits...\n')
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
print(f'Multireddit: {multireddit_result}\n')

# Export data as json
data = {}
data['original_content_posts'] = to_dict(oc_posts)
data['high_comment_posts'] = to_dict(hi_comment_posts)
data['upvoted_posts'] = to_dict(upvoted_posts)
data['unique_reddits'] = to_dict(unique_forums)
data['recurring_reddits'] = to_dict(recurring_forums)
data['multireddit_created'] = multireddit_result
data_json = json.dumps(data, indent=4)
# Write json to file
try:
    with open(OUTPUT_FILENAME, "wt") as output:
        output.write(data_json)
        print(f'Processed data exported to \'{OUTPUT_FILENAME}\'')
except IOError:
    print('Could not write data to file')
    print(f'Data: \n{data_json}')