# ACNH_TradingApp

An Animal Crossing New Horizons trading application

## Installation
- In terminal, create a folder in any desired location of your computer
- Cd into the folder and clone the repository
- Create a virtual environment following command and the name can be anything: virtualenv myenv
- Activate the virtual environment: source myenv/bin/activate
- Your virtual environment name will show on the left of your terminal name, that's how you'll know it's successfully activated
- Install Django in your virtual environment: pip install django
- Install Django-Crispy-Forms: pip install django-crispy-forms
- Install Pillow: pip install pillow
- Cd into the cloned repository and run python manage.py runserver
- The application should run on localhost:8000

## Improvements
- Getting the items from the API connecting to the user's posts and profile
- Adding filters for posts

## Stretch Goals
- An algorithm to match users based of what items they are looking for
