# Pytest Project

This is a Python project that uses `pytest` to perform automated testing.
This `README` provides instructions on how to run the tests locally.

## Prerequisites

Before running the tests, ensure that you have the following installed on your system:

- [Python 3.6+](https://www.python.org/downloads/)
- [pip](https://pip.pypa.io/en/stable/)

## Installation

1. Clone the repository to your local machine:

   git clone <repository-url>
   cd <repository-folder>

2. Create virtual environment:

    python -m venv venv

3. Install dependencies:

    pip install -r requirements.txt

4. To run Demo tests use command:

    pytest -s -v -m demo


## Repository comments

This repository was created to test Demo page with URL: 
  https://opensource-demo.orangehrmlive.com/web/index.php/pim/viewEmployeeList

**Technical Stack**:
 - PyTest framework for automated tests
 - Selenium - for web browser interactions
 - Beautiful Soup and Pandas - for parsing UI tables
 - requests library - for API calls
 - sqlite3 - for simulating data base connection
 - python-dotenv  - for loading values from .env file as environmental variables
 - Faker - for creating fake values (password)
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
