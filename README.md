# Backend Coding Challenge

At aspaara a squad of superheroes work on giving superpowers to planning teams.
Through our product dashboard we give insights into data – a true super-vision
superpower. Join forces with us and build a dashboard of the future!

![aspaara superhero](aspaara_superhero.png)

## Goal

Create a simple backend application that provide API that allows a planner to get insights
into client and planning information.

You will find the corresponding data(Fixture) that need to be imported into database from  `planning.json`, which
contains around 10k records.

## Requirements

Create proper database models that can fit to the schema

Within the application, it should be possible to
* provide api(s) to get the planning data
* api must be paginated
* api must provide provision to filter for as many columns as possible
* api must have search functionality to search for records
* api should provide sorting of data 


## Data Model

* ID: integer (unique, required)
* Original ID: string (unique, required)
* Talent ID: string (optional)
* Talent Name: string (optional)
* Talent Grade: string (optional)
* Booking Grade: string (optional)
* Operating Unit: string (required)
* Office City: string (optional)
* Office Postal Code: string (required)
* Job Manager Name: string (optional)
* Job Manager ID: string (optional)
* Total Hours: float (required)
* Start Date: datetime (required)
* End Date: datetime (required)
* Client Name: string (optional)
* Client ID: string (required)
* Industry: string (optional)
* Required Skills: array of key-value pair (optional)
* Optional Skills: array of key-value pair (optional)
* Is Unassigned: boolean

## Tech Stack

* Python 3.8+
* FastAPI
* SQLAlchemy


## Submission

* Please fork the project, commit and push your implementation and add
  `sundara.amancharla@aspaara.com` as a contributor.
* Please update the README with any additional details or steps that are
  requried to run your implementation.
* We understand that there is a limited amount of time, so it does not have to
  be perfect or 100% finished. Plan to spend no more than 2-3 hours on it.

For any additional questions on the task please feel free to email
`sundara.amancharla@aspaara.com`.
