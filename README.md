# FormBot

## Context
A bot to fill out forms. Made as a model to automate the process of submitting information to [freelancewebdevelopers](https://femalefreelancewebdevelopers.com).

## Installation
_Note: I am using poetry as a package manager, also GitHub's command-line tools._

* Clone the repository
	- `cd ~ && gh repo clone j-a-c-k-goes/FormBot && cd FormBot`
	- alternatively: download the .zip, use https clone method

* Activate Virtual environment ( you should already be in root directory )
	- `poetry shell`
	- alternatively: `python3 -m venv <formbotvenv> && source <formbotvenv>/bin/activate`

* Install packages and update.
	- `poetry install && poetry update`
	- alternatively: `pip install -r requirements.txt`

* Run the script
	- `python3 -i app.py`

## FormBot Works Like
* Connects to a website.
* Determines form elements.
* Prepares needed data.
* Fills out form with data.
* Archives the page source.

## Future Work
* Using asynchronous calls.
* Command-line arguments made passable.
* Pulling from a data set to run the bot on a loop cycle.

## Sources and Resources
[ femalefreelancedevelopers ](https://femalefreelancedevelopers.com/)

[ screeninfo ](https://github.com/rr-/screeninfo)

[ creating a virtual environment ](https://docs.python.org/3/tutorial/venv.html)

[ selenium documentation ](https://www.selenium.dev/documentation/)
