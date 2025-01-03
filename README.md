# Pytest Project

This is a Python project that uses `pytest` to perform automated testing.
This `README` provides instructions on how to run the tests locally.

## Prerequisites

Before running the tests, ensure that you have the following installed on your system:

- [Python 3.6+](https://www.python.org/downloads/)
- [pip](https://pip.pypa.io/en/stable/)

## Installation

1. Clone the repository to your local machine:

   git clone

3. Create virtual environment:

   This step would be slightly different for Mac/Windows/Linux
   
   For Windows:
   
    - python -m venv env  (to create virtual env)
    - env\Scripts\activate.bat  (to activate virtual env)

   For Mac:
   
    - python3 -m venv env  (to create virtual env)
    - source env/bin/activate  (to activate virtual env)
   

5. Install dependencies:

    pip install -r requirements.txt

6. To run Demo tests use command:

    pytest -s -v -m demo


## Repository comments

This repository was created to test Demo page with URL:  
https://opensource-demo.orangehrmlive.com/web/index.php/pim/viewEmployeeList

**Technical Stack**:
 - PyTest framework for automated tests
 - selenium - for web browser interactions
 - beautiful soup and pandas - for parsing UI tables
 - requests library - for API calls
 - sqlite3 - for simulating data base connection
 - python-dotenv  - for loading values from .env file as environmental variables
 - faker - for creating fake values (password)
 - webdriver-manager - for managing webdriver version
 - pytest-dependency - for managing tests dependencies

## Project structure
**Project uses PyTest fixtures with different scopes**: 
 - webdriver selection
 - database connection
 - API calls
 - password generation

**BasePage used for storing common UI actions which can be applied on any UI page**:
 - select dropdown
 - enter text
 - click button
 - wait for popup message, etc. 

## Important security information 
Be careful. This is a Demo project, not a production code.  
Only because of that .env file with credentials was pushed to repository.  
Never push .env file with credentials to repository in your production code!  
Store them in safe vault (LastPass, 1Password, etc.) and share only across trusted team members.  

## Known flakiness   
Function get_current_user is used to get full name of current user.  
Unfortunately, this value randomly changes.  
Sometimes even during one browser session. 
That makes tests flaky.  
That should be discussed with developers to create the best approach in tests.

## Code execution workflow
 - Create 2 users (1 - Admin, 2 - ESS), assert confirmation popup message was created
 - Search both users by username on the Admin page (assert Search works as expected)
 - Use Reset button in the Search, assert Search values are back to default, assert table shown with all users
 - Delete User (ESS), assert User no more presented in the UI table, assert User was deleted from the database with SQL query
 - Send GET API call for all users, assert number of users in the UI table and API response is the same

## API assumptions
Assumptions about API URLs were made in the project:  
base_url:  
https://opensource-demo.orangehrmlive.com    
GET API for all users:  
https://opensource-demo.orangehrmlive.com/users  
GET API for user (with specific ID):  
https://opensource-demo.orangehrmlive.com/user/1
