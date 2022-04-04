## Author


* [**Virginiah Periah**](https://github.com/virginiah894)

## Features
## Deployment
[Heroku](https://veerest.herokuapp.com/)

As a user of the web application you will be able to:

1. View photos posted by other users
2. Comment on other posts
3. Upvote Posts
4. Create their own posts
5. Delete posts



## Getting started
### Prerequisites
* python3.6
* virtual environment
* pip

### Cloning
* In your terminal:
        
        $ git clone https://github.com/virginiah894/News_Api
     

## Running the Application
* Install virtual environment using `$ python3 -m venv --without-pip virtual`
* Activate virtual environment using `$ source virtual/bin/activate`
* Download pip in our environment using `$ curl https://bootstrap.pypa.io/get-pip.py | python`
* Install all the dependencies from the requirements.txt file by running `python3 pip install -r requirements.txt`
* Create a database and edit the database configurations in `settings.py` to your own credentials.
* Make migrations

        $ python manage.py makemigrations app
        $ python3 manage.py migrate 

* To run the application, in your terminal:
* cd into crudapi,then run

        $ python3 manage.py runserver


## API endpoints
*  http://127.0.0.1:8000/api/
*  [Posts](http://127.0.0.1:8000/api/app/)
*  [Comments](http://127.0.0.1:8000/api/comments)
        
## Technologies Used
* Python3.10
* Django 4
* HTML 5
* Django bootstrap 
* Django Rest framework
* crispy forms


## Future Implementation
- Authentication System
- Limit delete of posts to only the posteer /admin


