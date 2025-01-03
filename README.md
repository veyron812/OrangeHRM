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
