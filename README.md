2020-ca377-master-eatatdcu

Master repository for Fundamentals of Programming III (CA377)

## Synopsis

The aims of this project is to help any possible customer to find a restaurant at DCU, among all campus availables. Furthermore, by providing a web site the most friendly possible for the user.


## Installation

First of all to install the following application, you need to have python3.6 installed on your laptop and pip too.
Furthermore, you also need to install django 2.2.4 and the Requests library.
To install all those library you just need to execute the following command line:
- pip install django==2.2.4
- pip install requests
Then you need to clone the repository of this project.
And to run the application execute the following command line, in the **src/** directory:
- python3.6 manage.py runserver

If all go well, you probably will see the following message come :
"Watching for file changes with StatReloader
Performing system checks...

System check identified no issues (0 silenced).
December 13, 2019 - 16:36:48
Django version 2.2.5, using settings 'ca377.settings'
Starting development server at http://127.0.0.1:8000/
Quit the server with CONTROL-C."

So you just need to connect to the following addresse to see the web application : http://127.0.0.1:8000/

## Deploy to the cloud Pythonanywhere

If you want to deploy the project to an web host (pythonanywhere).
You must first create an account on pythonanywhere.
Go on the console tab and create a console bash.
Then install the requiered library, just execute the following command lines:
- mkvirtualenv --python=/usr/bin/python3.6 eatatdcu-virtualenv
- pip install django==2.2.4
- pip install requests

Then clone the repository

Create the web application, from the web tab by clicking "Add a new web app"
Choose the Manual configuration and select 3.6 as the Python version

Edit the source code and working directory values - /home/yourname/ca377/src/

Edit the WSGI configuration file. Remove everything except the Django code and set the path and os.environ['DJANGO_SETTING_MODULE'] values:
put the path to:
path = '/home/yourname/ca377/src/'

And finally run the command lines:
- python manage.py makemigrations eatatdcu
- python manage.py migrate 
- python manage.py shell >>>import load_db_data

To migrate the database.
And reaload the web app.




<!-- Provide code examples and explanations of how to get the project. -->


## Tests

To accompany this project, some Unit Test have been setting up.
To be able to run this tests cases, you must be in the **src/** directory.
Then you just need to execute the following command on the terminal :
- python3.6 manage.py test eatatdcu

This will run 11 tests cases.


## License

Sufyan Kerboua