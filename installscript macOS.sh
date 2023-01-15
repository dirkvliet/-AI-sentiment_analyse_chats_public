#!/bin/bash

# Install git
xcode-select --install

# Install Python 3.10.6
curl https://www.python.org/ftp/python/3.10.6/python-3.10.6-macosx10.9.pkg -o python-3.10.6-macosx10.9.pkg
sudo installer -pkg python-3.10.6-macosx10.9.pkg -target /

# Set Python path
echo 'export PATH="/Library/Frameworks/Python.framework/Versions/3.10/bin:$PATH"' >> ~/.bash_profile
source ~/.bash_profile

# Install pip
curl https://bootstrap.pypa.io/get-pip.py -o get-pip.py
python3 get-pip.py

# Clone git repository
git clone https://github.com/dirkvliet/AI-sentiment_analyse_chats.git

# Navigate to the cloned directory
cd AI-sentiment_analyse_chats

# Install requirements
pip3 install -r requirements.txt

# Launch python script
python3 run.py

# Open browser
open http://localhost:5000
Please note that before running this script, you should make sure that you are running it with a user that has administrative rights, also you should check if the required dependencies are installed on the system.




