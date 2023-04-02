# Python Examples for API Interactions

Here some basic python examples that you can leverage on how to interact with U.S. Bank's apis.

To see the full list of APIs available, you can read the documentation [here](https://hacktotrack-innovation.usbank.com/).

## Set Up

If you're using **PyCharm**, make sure that you have a virtual environment so that we can install
python packages specific to your project.

If you're using another tool like **Visual Studio Code**, make sure that you create a virtual
environment for your project.

Once you have your project open, make sure you install the following libraries using `pip`:

* requests
* python-dotenv

You can also install both of these running the command `pip install -r requirements.txt` (assuming you're using this project).

## Developer Notes

To see if your code is using industry standard naming conventions, you can run
`pylint *.py */*.py` to run the linter and have the code rated.

## Build Library Locally

To build this library locally you can run the command `python -m build` to generate a **.whl** file in the **dist/** folder.

If you want to use this library for your local python project, you can install it via pip by running
`pip install --index-url https://test.pypi.org/simple/ --no-deps mctc-hackathon-robot297`.
