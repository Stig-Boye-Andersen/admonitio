# Amonitio

## The idea
In my team we often face situations where we have to remember to complete certain tasks at a given time in the future. Often the tasks are complex and require a guide to complete.

So far we've kept the reminder/notification functionality in one system and the documentation/guide in another system. Wouldn't it be nice if those two things could be combined?

This is where GitHub comes to the rescue since it allows us to build a system where both the reminder and the guide is managed in the same system. To fulfill our requrements the system should be designed as follows:

The basic technical idea is base on Markdown documents and their Frontmatter feature. 


## Setup a virtual environment for your Python
At the core of the reminder workflow sits a Python componet that regularly goes through all the configured Markdown documents and checks whether they have a remind date set, that is close enough for someone to get a reminder about it.

I you're interested in working with that Python components following the steps below to setup your developments environment.

## Setup development environment
The development enviroment uses Python envents that are further described [here](https://realpython.com/python-virtual-environments-a-primer/)

Create virtual environment by running this
```cmd
python3 -m venv venv
```

Activate the virtual environment by running this 
```cmd
source venv/bin/activate
```

Now the virtual environment is active you can install external dependencies into it by running a statement like the following
```cmd
python -m pip install markdown
```

If you don't want to work in the Python environment any more run the following command:
```cmd
deactivate
```

