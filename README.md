# SocialConsumer
This is a small lightweight utility app that consumes aggregated social news data from an API 
and performs light data processing. Specifically, this app interfaces with the redit api. https://www.reddit.com/wiki/api

## Getting Started

### Clone the Repository
`git clone https://github.com/dswelbor/social-consumer.git`

### Install Python 3 (as needed)
This app is written in python3 and will need a python interpretter. More information can be found at https://www.python.org/downloads/

### Install pip (as needed)
Debian/Ubuntu Linux: 
`sudo apt-get install python3-pip` <br>
More detailed instructions are available at: 
https://pip.pypa.io/en/stable/installing/

### Install VirtualEnv (as needed)
A virtual environment for python app is preferred. More information about virtualenv can be found at https://virtualenv.pypa.io/en/latest/installation.html <br>
From commandline (linux), run: `sudo pip3 install virtualenv` <br>
or <br>
From commandpromt (windows administrator mode), run `pip3 install virtualenv`

### Create virtual environment and install dependancies
To create a virtual environment for python and install app dependancies, do the following:
1. Go to `/home/<user>` directory (or other preferred location for virtual environments)
2. Create a virtualenv `virtualenv -p python3 venv`
3. Activate virtualenv `source venv/bin/activate` (or `source venv/Scripts/activate` on windows)
4. Go to repository root directory.
5. Install requirements `pip3 install -r requirements.txt`

## Configure OAuth for Reddit
Follow the steps below to configure SocialConsumer with the appropriate credentials. Note: If you do not have an api key already, visit: https://www.reddit.com/prefs/apps
1. Copy `praw_sample.ini` to a new `praw.ini`, file in the repository root 
directory.
2. In the `praw.ini` fill in relevant reddit api key and 
other sensitive data. DO NOT UPLOAD `praw.ini` to github or add it to 
any commits where it can be accessed from the commit history.

   Specifically, you will need to change: <br>
   - client_id
   - client_secret
   - username
   - password

    DO NOT UPLOAD `praw.ini` to github or add it to 
any commits where it can be accessed from the commit history.


## Running SocialConsumer
First follow the steps above to configure the app for OAuth with the reddit API. Using an activated virtualenv instance, from the repository root directory execute: <br>
`python3 run.py`
<br>
One possible example output could be: <br>
```
Aggregating 'original content' posts...
Aggregating 'high comment count' posts...
Aggregating 'most upvoted' posts...
Aggregating 'unique' subreddits...
Aggregating 'recurring' subreddits...
Creating multireddit with recurring subreddits...

Number of Original Content Posts 3
Number of Posts with High Comment Counts: 38
Number of top 10 most upvoted posts (descending): 10
        Title: LPT: First rule of family gatherings, always bring
        Upvotes: 113739
        Title: A doctor at a high risk hospital is living away fr
        Upvotes: 108782
        Title: Poor dads
        Upvotes: 103172
        Title: Spinnin’
        Upvotes: 91465
        Title: In my super small indiana town
        Upvotes: 87154
        Title: My neighbour Joe returning home from hospital, now
        Upvotes: 80863
        Title: Checkmate
        Upvotes: 75748
        Title: WHO accused of 'carrying China's water' after offi
        Upvotes: 69418
        Title: Whoops.
        Upvotes: 68639
        Title: My quarantine birthday is going well.
        Upvotes: 64208
Number of "unique" subreddits in r/popular: 92
Number of recurring subreddits in r/popular: 8
Multireddit: /user/testdev/m/top100recurring

Processed data exported to 'output.json'
```

## Export Data
SocialConsumer aggregates data from the reddits r/popular subreddit and performs light data processing. The output listing can be accessing by default from the repository root directory in `output.json`. A sample output list file is provided `output_sample.json`
