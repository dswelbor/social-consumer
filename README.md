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



