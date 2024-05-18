# Content Rating Service

A Django-based service for rating content with features to detect and handle suspicious rating activities.

## Table of Contents

- [Installation](#installation)
- [Environment Setup](#environment-setup)
  - [Testing](#testing-environment)
  - [Production](#production-environment)
- [Running the Project](#running-the-project)
- [Load Initial Data](#load-initial-data)
- [APIs](#apis)
- [Suspicious Rating Detection](#suspicious-rating-detection)
- [Running Tests](#running-tests)

## Installation

1. Clone the repository:
   ```bash
   git clone https://github.com/mhdi01/BitPin.git
   cd bitpin
2. Create virtual environment
   ```bash
   python -m venv env
   source env/bin/activate
   pip install -r requirements.txt

## Load Initial Data
Load Data needed for different table by these commands:
``bash
python manage.py load_users
python manage.py load_contents
python manage.py load_ratings

## Environment Setup

 # Testing
 1. To set the environment = testing run this command
    ```bash
    export DJANGO_ENV=testing 

  Also the default DJANGO_ENV is testing

# Production
1. To set the environment = production run this command:
   ```bash
   export DJANGO_ENV=production 

2. Confiure postgresql in the /bitpin/settings/production.py as needed

## Running the Project
1. Make migrations and migrate them

  ```bash
  python manage.py makemigrations
  python manage.py migrate
```
2. Then run the project
  ```bash
  python manage.py runserver



