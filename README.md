---
page_type: sample
description: "Application to summarize text from the scanned document."
languages:
- python
products:
- azure
- azure-app-service
---

# Application

Application to summarize text from the scanned document.
This is Python 3 Flask application with Angular front-end.

## Installing
### Prerequisites

Python 3  installed standalone or as a part of [Conda](https://www.anaconda.com/products/individual).

### Dependencies installation

Create your virtual Python environment (using conda or venv). Switch to your new environment.
Run from the project root folder:
```
pip install -r requirements.txt
```

## Running
### Local machine

To run locally on Linux machine:
```
export FLASK_APP=application.py
flask run
```

To run locally on Windows machine:
```
set FLASK_APP=application.py
flask run
```

# References

For more information, please see the [Python on App Service quickstart](https://docs.microsoft.com/azure/app-service/containers/quickstart-python).


