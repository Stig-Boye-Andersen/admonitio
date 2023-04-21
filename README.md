# Amonitio
The Amonitio project is focused on creating a system that can solve the problem outlined below.

## The problem
In my team we often face situations where we have to remember to complete certain tasks at a given time in the future. Often the tasks are complex and require a guide to complete. An example could be: "On the 2. of April 2027, update the 'xxx-client' Azure app registration client secret and related external C# services using that secret".

So far we've kept the reminder/notification functionality in one system and the documentation/guide in another system. It would be nice if they could be kept together?

To add to that my team is far from the only team with this requirement and therefore it would be equally nice if this system could be easily available to other teams in my organization.

## The solution

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

