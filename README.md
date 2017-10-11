
This is my first attempt at using Django (not the movie). With this small Python/Django web application wou can manage a simple app store. A list page and a detail page are provided. 

## Requirements

To develop the application I used Python 3.6.3 and Django 1.11.6. I haven't tested it with lower versions.

## Installation

Copy the project folder to your system, then from inside the folder run the script: `python manage.py runserver`

## Get Started

After you've started the development server. Navigate to `http://localhost:8000/appStore`.

## Description

The app uses _SQLite_ and provides only one model with the following fields: *(name, description, platform, created_at)*.

The following pages/urls are available:

* **appStore/** Show a list of all the available apps
* **appStore/{id}/** Detail page for the app with id={id}
* **appstore/app/add/** Create a new app
* **/appStore/app/{id}/** Edit detail page for the app with id={id}
* **/appStore/app/{id}/delete** Delete confirmation page for the app with id={id}

Buttons and links are provided to navigate from one page to another and back.

## Tests

Some tests are available in the `tests` folder. To run them use the command
`python manage.py test appStore/tests`
