Python Project Template
-----------------------

This project aims to provide a template for new python project.
Goal is to keep a good file structure, that allows for easy packaging and building.

This project is useful for creating Python Eggs, and Debian packages (.deb) for both Python 2 and 3.

*Should be compatible with Python >=2.7 and >= 3.4.*


## How to initialize you project

1. Copy all files in the python bootstrap folder to your new repo (except maybe this md file).
2. Replace MYPROJECT by your project name in setup.py.
3. Rename the MYPROJECT folder and use this as your base application module.
4. Rename the bin/MYPROJECT script and use this as an executable if necessary.

## How to use this project as a template

If you don't fancy copying all the files to your repo, you can use these commands to create your project on github :

    git clone --depth 1 --origin source git@github.com:ronhanson/python-project-template.git <NEW_PROJECT_NAME>
    cd <NEW_PROJECT_NAME>
    git create <NEW_PROJECT_NAME>

You need [Hub](https://github.com/github/hub) installed for that.

## How to develop your project

Type the following command to initialize your development environment :

    sudo pip install fabric
    
    fab dev
    
This will initialize a virtual environment, and install your python requirements.

## How to package your project

See [HOWTO.md](HOWTO.md) file to see how to package your project in egg or deb.

## A note on Python requirements

In order to be able to use your own sub projects, python libraries, ..., you can use the requirement file with pip/git combo.

Adding this line to your requirements.txt file will add a git repo as a requirement :

    -e git+git@github.com:ronhanson/python-toolbox.git#egg=toolbox

This will clone the git repo into the "libs/" folder. And it will also add this path into your virtualenv PYTHONPATH.

This is pip editable mode. It is very useful to include projects of your own or not packaged ones.
Note the "#egg=toolbox" part. This sets the name of the package you are installing.

This also allows softwares like PyCharm not to yell at you telling you a requirement is missing.
When packaging, this requirement will be changed for "toolbox" only.

## Known Bugs

 - This project will not work if python3 is not installed.

## Todo

 - Python2 only compat.
 - Git hook for version bump.
 
## Author & Licence

Copyright (c) 2014 Ronan Delacroix

This program is released under [MIT Licence](LICENCE.txt).
