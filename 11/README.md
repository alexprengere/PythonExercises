## Exercise 11

### Problem

This time, we want to build a simple web application. Let's suppose we have a list of races in a CSV file:

```
$ cat races.csv
2015,Marathon Nice Cannes,42km,03:55:12
2015,Trail des Alpes Maritimes,25km,04:51:10
2015,Courir pour une fleur,10km,00:56:42
2016,Trail de Caussols,33km,04:25:21
2016,Marathon Nice Cannes,42km,03:50:14
```

Now we want to build an application which will display those races in a nice web page. Later on, we could
improve this to add search feature for example.

We will use the [Flask](http://flask.pocoo.org/) Python library for this. To install it in a isolated environment, follow these instructions (if an error occurs, read the help section at the bottom):

```bash
virtualenv .env
source .env/bin/activate
pip install -r requirements.txt
```

In the `start` directory is the backbone of a very simple Flask application, you can use it as a starting point.
```
start
├── app.py
├── static
│   ├── main.js
│   └── style.css
└── templates
    └── index.html
```

You can already launch the webapp with:

```bash
python start/app.py races.csv
```

Now let's improve it!

### Help

`pip` is the Python package manager. If it is not installed on your machine, you can install it with:

```
# easy_install should be on your machine, if not, you need
# to install python-setuptools with your package manager
easy_install --user pip
```

`virtualenv` is a tool helping you work in isolated environments. With this, when you install a new package, you will only see it in your virtual environment, allowing you to cleanly separate the dependencies of your projects.
Install it like any other package with:

```
pip install --user virtualenv
```
