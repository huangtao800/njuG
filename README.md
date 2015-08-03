## Introduction
njuG is a simple social website built especially for LGBT students in universities located in the city of Nanjing, China. The current people in China are becoming much more friendly to homosexuality. However, due to the deep-rooted traditional culture, many of the homosexual people, especially the youth, who are well-educated, still find it very difficult to make their friends and families understand and accept their sexual orientation. 

I created this website with the hope of boosting the communication among gay students in universities, and pushing forward the public attention on this community. I wish my homosexual alumnus at Nanjing University will enjoy this website.

## Installation
1. pip install Django==1.8.3
2. pip install mysql-python
3. pip install django-allauth
4. pip install sorl-thumbnail
5. sudo apt-get install libjpeg-dev
6. pip install Pillow
7. Build a new database in your MySQL database
8. Edit njuGay/settings.py. Modify "DATABASES" secition, change the database name, user and password to the ones you created in step 7.
9. Edit njuGay/settings.py. Modify "EMAIL_HOST", "EMAIL_HOST_USER", "EMAIL_HOST_PASSWORD" and "EMAIL_PORT" to your preferred email service. The default configuration uses Gmail to send emails to users.

## Features
1. Sharing status, pictures, and blogs
2. Posting comments on status or blogs
2. Building personal profiles
3. Sending and receiving messages
4. Posting activities so that people could see and join them
