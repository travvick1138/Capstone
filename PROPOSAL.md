# Proposal: Indie Comic Book Reader

The **ICBR** is a comic book viewer in a web app.

It allows any artist to build a **.CBZ** file of **source** images and view them as a **comic** in a browser to give the user the experience of reading a comic book while on a website.


## Specific Functionality

### Main Page
#### Description of concept
Full page image preferably indie Comic art or of an artist space with a description, links to an example experience, and login or register set up.

#### Login
When you load the domain you will be prompted to login or sign up using django User extended configuration and authentication.
Authentication will require email verification and captcha.
Group configuration for permission and content
Agreement to terms and conditions

#### User content and options
Once logged in the user will have the ability to upload .cbr, .cbz and image files to create viewable comics.
They will see a list of content they have saved on the server for viewing thru the reader.

#### Upload files
Once logged in as a trusted user can upload files to the server to create a .cbz or to view in the Comic Reader
Add a warning about copyrighted material not owned by the user will be removed from the server.  see terms and conditions.

### Comic Reader
Will be a full page viewer that will pop up when you select a file.

## Data Model
### source
Is one of the follow file types to be viewed in the comic reader from the database by user.
Each source will have the following properties:
 * Unique ID
 * file name and extension
 * upload created date
 * modified date
 * public/private
 * content rater NSFW

#### File Types
* Upload File Types
    * Viewer File Types
        * .cbr
        * .cbz
        * .cbt
    * Transformable input File Types
        * .png
        * .jpg, .jpeg
    * Transformed output File Types
        * .cbz

### Viewable Comic
Viewable comics will be viewed in a .cbr .cbz .cbt format

## Technical Components
Indie comic reader based on:
https://github.com/giacomos/collective.comicbookreader

Creating Reader files using:
https://pypi.python.org/pypi/picopt/1.3.1 to take grouped image .png, .jpg, or .jpeg files into .cbz

Front-end will be HTML5, CSS, JavaScript

## Schedule
* high level workflow for database to viewer - easy - 1 day
* deconstruction to break down each problem - easy - 1 day
* django database build - medium - 4 days
* django user configuration and authentication - easy - 2 days
* python file conversion integrations - medium - 4 days
* python comicbookreader intergration - medium - 5 days
* viewable gallery front-end - medium - 3 days
* indiecomicbookreader front-end - medium -3 days
* Main page build - easy 2 days

## Additional content
* API to google drive for content
* API to dropbox for content
* User created content sharing
* Add Comic tagger for getting meta data for comic books https://pypi.python.org/pypi/comictagger/1.1.15-beta or use https://pypi.python.org/pypi/libgenapi/1.2.0
