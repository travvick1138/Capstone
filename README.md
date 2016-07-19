# Proposal: Indie Comic Book Reader

The **ICBR** is a comic book viewer in a web app.

## Installation

Clone this repo and cd into it

    git clone https://github.com/travvick1138/Capstone.git

then

    cd Capstone

### Create a virtual myenv and activate it:

    virtualenv myenv

then

    MAC - source env/bin/activate or
    Windows - .\myvenv\Scripts\activate or
    Windows w/Powershell - .\myvenv\Scripts\activate.ps1

you should see (myenv) show up in front of your prompt (ex: `(myenv) Jasmine@Home $`)

### Make sure it's running python3

    virtualenv -p python3 myenv

### install django

    pip3 install django

### make sure you're in the same directory as manage.py and do

    python manage.py runserver

follow its instructions and make sure you see the right message in your browser.

## Requirements for Picopt

### install Pillow 3.3.0

    pip3 install Pillow

### install rarfile 2.8

    pip3 install rarfileMozjpeg
