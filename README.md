# Amonitio
The Amonitio project is focused on creating a system that can solve the problem outlined below.

## The problem
In my team we often face situations where we have to remember to complete certain tasks at a given time in the future. Often the tasks are complex and require a guide to complete. An example could be: "On the 2. of April 2027, update the 'xxx-client' Azure app registration client secret and related external C# services using that secret".

So far we've kept the reminder functionality in one system and the guide in another system. It would be nice if they could be kept together.

To add to that my team is far from the only team with this requirement and therefore it would be equally nice if this system could be easily available to other teams in my organization.

## The solution
The following solution could solve the problem outlined above.

First to keep the reminder and the guide together the guide should be written in Markdown. Writing the guide in Markdown would allow us add a so called 'front matter' to the guide an thereby specify additional information related to the guide. That addition informaiton could be a reminder date and other relevant information. Below is a brief example of such a guide:

```markdown
---
reminder-date: 02.04.2027
---
# Update the xxx-client Azure app registration client secret

The xxx-client Azure app registration client secrets is updated by completing the following steps...
```
Having the guide and related meta data connetected such as a reminder date configured we only need a component that can regularly go through that meta data a check whether a reminder should be generated. That component could be a GitHub workflow setup to run once a day (schedule trigger).

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

