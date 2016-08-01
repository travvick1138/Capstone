# Proposal: Indie Comic Book Reader

The **ICBR** is a comic book viewer in a web app.  This reader is based on https://github.com/giacomos/collective.comicbookreader it is not an exact replica, but modern update with my twists, but the initial credit goes to giacomos

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
    pip3 install django-permission

### make sure you're in the same directory as manage.py and do

    python manage.py runserver

follow its instructions and make sure you see the right message in your browser.

## Requirements for Creating comic book files

### install Pillow 3.3.0

    pip3 install Pillow

### install python-resize-image

    pip3 install python-resize-image

### install rarfile 2.8

    pip3 install rarfile

### install zipfile

    pip3 install zipfile
