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
From commandline, run: `sudo pip3 install virtualenv`

### Create virtual environment and install dependancies
To create a virtual environment for python and install app dependancies, do the following:
1. Go to `/home/<user>` directory (or other preferred location for virtual environments)
2. Create a virtualenv `virtualenv -p python3 venv`
3. Activate virtualenv `source venv/bin/activate`
4. Go to repository root directory.
5. Install requirements `pip3 install -r requirements.txt`

## Configure API key
Copy `praw_sample.ini` to a new `praw.ini`, file in the repository root 
directory. In the `praw.ini` fill in relevant reddit api key and 
other sensitive data. DO NOT UPLOAD `praw.ini` to github or add it to 
any commits where it can be accessed from the commit history.
Specifically, you will need to change: <br>
- client_id
- client_secret


## Run SocialConsumer
Using an activated virtualenv instance, from the repository root directory execute: <br>
`python3 run.py`
<br>
One possible example output could be: <br>
```bash
Number of Original Content Posts 3
Number of Posts with High Comment Counts: 27
Number of top 10 most upvoted posts (descending): 10
        Title: A doctor at a high risk hospital is living away fr
        Upvotes: 96626
        Title: LPT: First rule of family gatherings, always bring
        Upvotes: 92835
        Title: Spinnin’
        Upvotes: 81553
        Title: Wife wanted a cat. I said no, so we compromised an
        Upvotes: 79805
        Title: Elsa is pretty athletic for a person that was lock
        Upvotes: 77456
        Title: Data shows Amazon raised prices during pandemic al
        Upvotes: 71659
        Title: This man is the original John wick
        Upvotes: 68970
        Title: He really tried
        Upvotes: 68267
        Title: TIL A married Secret Service agent had trouble ext
        Upvotes: 66258
        Title: 🔥 rainbow island, iran
        Upvotes: 65840
Number of "unique" subreddits in r/popular: 91
Number of recurring subreddits in r/popular: 9
Multireddit: /user/testdev/m/top100recurring
```