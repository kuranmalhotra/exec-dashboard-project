# Exec Dashboard Project [![Build Status](https://travis-ci.com/kmalhotra13/exec-dashboard-project.svg?branch=master)](https://travis-ci.com/kmalhotra13/exec-dashboard-project)

<i><h3>Created by Kuran P. Malhotra</h3></i>

## Introduction

This project's goal is to provide information on a chosen data file and help visualize it. Later iterations will allow for it to incorporate multiple months' worth of data.

## Technical Prerequisites

<b>Software Requirements</b>
- Git
- Anaconda 3.7
- Python 3.7
- Pip
- Packages listed in `/requirements.txt`

## Installation

In order to set up this applet, please download install the source code:

```sh
git clone git@github.com:kmalhotra/exec-dashboard-project
cd exec-dashboard-project/
```

Install the package dependencies:

```sh
pip install -r requirements.txt
```

## Usage

To use the application, just run the script using the following command:

```sh
python app/monthly_sales.py
```


From there, you will be prompted to select a datasheet via a pop-up window. The system will generate a report and graph based on that data.

## Testing

From within the virtual environment, install the `pytest` package (first time only):

```sh
pip install pytest
```

Run tests:

```sh
pytest
```