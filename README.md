# trello-api
Hybrid testing framework using Trello API for testing API and UI

# Install dependencies
Install the depended packages in requirements.txt using 
```
pipenv install -r requirements.txt

```

And execute
```
export PYTHONPATH="${PYTHONPATH}:/Path/to/yout/project"

```
# Project Structure

Here you can find a short description of main directories and it's content

* api-tests - Set of tests for API(trello_tests.py) and UI(test_ui.py) level
* pageObjects - There are sets of method for each page/view  
* utils - this directory contains files responsible for utilities making easir some operations inside the framework

# Run test cases

In order to run test cases, use the command below:

```
py.test api-tests/trello_tests.py api-tests/test_ui.py

```
