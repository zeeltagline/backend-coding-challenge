# Backend Coding Challenge
## Requirements

1. Python 3.8+
2. FastAPI
3. SQLAlchemy
4. SQLite

## Setup

1. Clone the project from github:
   `git clone git@github.com:zeeltagline/backend-coding-challenge.git`

1. Go to the project directory: `cd backend-coding-challenge`

1. Create a virtual environment (If virtualenv is not installed, "pip3 install virtualenv"): 
   `python3 -m venv venv`

1. Activate the venv:
  `source venv/bin/activate`

1. Install dependencies:
  `pip install -r requirements.txt`

1. Migrate to the database:
  `alembic upgrade head`

1. To import the data into the database, run the following script:
  `python dummy_data.py`

1. Run the app:
  `uvicorn main:app --reload`

1. Navigate to the following URL to view the API documentation:
 `http://localhost:8000/docs`



## Alembic DB Migrations
Alembic is used for generating migrations for the database for the SQL Alchemy.

### Create a migration
You can the change the message `create user table` in the below command.

### Create an manual migration
`alembic revision -m "create user table"`

### Create an autogenerate migration
`alembic revision --autogenerate -m [message]`


### Running a Migration
`alembic upgrade head`

### Downgrade last migration
`alembic downgrade -1`

### Downgrade migration from the beginning
`alembic downgrade base`


