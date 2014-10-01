% Date: 2014-09-30  
% Title: PACKAGE USAGE  
% Author: Ronan Delacroix

# PACKAGE INSTALLATION AND USAGE


### I. PYTHON INSTALLATION INSTRUCTIONS FOR LINUX

1. First install Python (2.7 or 3.4), pip and python-setuptools. Depending on your system it is something like :

		sudo apt-get install python3.4 python3-setuptools python3-pip

2. You can install the python package "pip" with setuptools if you don't have a python-pip package :

		sudo easy_install pip
	
3. If you fancy it, you can add in your PYTHONPATH variable the current folder ".". Place that line in your ".profile" :

		export PYTHONPATH="$PYTHONPATH:."
		

### II. PACKAGE INSTALLATION

Install current packages and its dependencies :

    pip install my_project.tar.gz

You should now be able to launch the scripts installed with your package.


### III. DEVELOP

Install Fabric globally :

    sudo pip install fabric

Create a virtual env, and setup the dev mode : 

    fab dev


### IV. PYTHON PACKAGING / EGG BUILD

You can create a Python egg simply by doing :

    python setup.py sdist


### V. DEBIAN PACKAGING / .DEB BUILD

If you want to create a .deb, first, check the debian.cfg file and add the dependencies you want.

Go to tools/build folder :

    cd tools/build

Build the package using vagrant (the .deb package will be generated with a jessie64 vagrant box):

    ./vagrant_build_deb.sh

Or if you are already on a Debian system:

    ./build_deb.sh


