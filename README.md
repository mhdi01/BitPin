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
  python manage.py migrate
```
2. Then run the project
  ```bash
  python manage.py runserver
  ```


## Load Initial Data
Load Data needed for different table by these commands:
``bash
python manage.py load_users
python manage.py load_contents
python manage.py load_ratings


## APIs
# Login API

. Endpoint : /auth/login/

. Method : POST

. Request Body:

```bash
{
  "username": test,
  "password": test
}
```

# Create/Update Rating API

. Endpoint: /api/ratings/

. Headers : {'Authorization': 'Bearer Token'}

. Method: POST

. Request Body:

```bash
{
  "content_id": 1,
  "rating": 4.5
}

```

# Get Contents API

. Endpoint : /api/contents/list/

. Method : GET


## Suspicious Rating Detection
To prevent manipulation of content ratings by coordinated groups, a task is run to detect suspicious rating activities. This task checks for patterns such as a sudden influx of ratings within a short time frame and a significant deviation from the average rating.

# Criteria for Suspicious Ratings
1. High Volume of Ratings: The number of ratings within a specified time window exceeds a threshold.
2. Low/High Ratings: The ratings are significantly lower or higher than the content's average rating.
3. Rating Difference: The difference between the average rating and the ratings given in the time window exceeds a threshold.

# Implementation
There is a celery task named  <detect_suspicious_activity> , This task will be called whenever a rating is saved in the database. there are three important criteria for us here:
1. Time Window
2. Number of Rating
3. Average of the rating
All of them are considered in the <detect_suspicious_activity> Task. we have Different Threshold for high and low rating and even for number of ratings. These Threshold might be temporary and we might choose different threshold for each content when we have collected enought Data in our database.

When number of ratings in the 1 hour Time windows is passed from the Threshold which is 100 , We need to check more conditions.
we will check recent rating more than High Rate Threshold and less than Low Rate Threshold , we Get the number of these ratings and Get The Percentage of their apperanace.
if the percentage is more than SUSPICIOUS_RATING_PERCENTAGE And The Average Rating that are recently added has more than 1.5 average rating from the Actual Rating we have a suspicious Situation.
It Means that the number of rating was increasing suddenly , The Average Rating was far away from the actual rating and we update a field named is_suspicious for these kind of rating and we do not consider them as valid rating.

# Reason
I Tried to user behavioral analysis in this task. I focused on the data and criteria that we could have, and i found each of them important in this task. So all of the needed criteria are used with different threshold to make a better analysis about the users beahvior for rating. To complete these task we need to have more data for each content , then we can add some expectation about rating/hour and average_rating .
so with these expectation we can analize users behavior more accurate.


## Running Tests
To run test Run this command:
```bash
python manage.py test
