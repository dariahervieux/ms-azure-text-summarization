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

Installed software:
* Python 3 - standalone or as a part of [Conda](https://www.anaconda.com/products/individual).
* Node.js
* Angular Cli

### Dependencies installation

Create your virtual Python environment (using conda or venv). Switch to your new environment.
Run from the project root folder:
```
pip install -r requirements.txt
```

### Configuration

#### Computer Vision API configuration

Create environment variables:
* COMPUTER_VISION_SUBSCRIPTION_KEY - your computer vision subscription key,
* COMPUTER_VISION_ENDPOINT - url of your computer vision resource

## Building

Build is made by Angular Cli.
To build the project on Windows machine

```
cd front-end
npm run-script buildWin
```

`buildWin` will create `dist folder in the project root `containing Flask and Angular front-end applications.

## Running
### Local machine

To run locally on Linux machine:
```
cd dist
export FLASK_APP=application.py
flask run
```

To run locally on Windows machine:
```
cd dist
set FLASK_APP=application.py
flask run
```

# Deploying on Azure
To deploy/update you application run
```
cd dist
az webapp up --name <your WebApp name>
```

# References

* [Python on App Service quickstart](https://docs.microsoft.com/azure/app-service/containers/quickstart-python).
* https://docs.microsoft.com/en-us/azure/cognitive-services/Computer-vision/quickstarts-sdk/client-library?pivots=programming-language-python


