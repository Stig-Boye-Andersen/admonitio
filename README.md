# reminder

## Setup a virtual environment for your Python

https://realpython.com/python-virtual-environments-a-primer/

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

