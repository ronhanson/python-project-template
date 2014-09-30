Python Bootstrap Project
------------------------

(Made for Python >= 3.4)

HOW TO INIT YOUR PROJECT

	1 - Copy all files in the python bootstrap folder to your new repo.
	2 - Replace MYPROJECT by your project name in setup.py.
	3 - Rename the MYPROJECT folder and use this as your base application module.
	4 - Rename the bin/MYPROJECT script and use this as an executable if necessary.
	5 - Type "fab dev" to initialise your development environment.

HOW TO PACKAGE YOUR PROJECT

	1 - Create a Python package (egg) :
		> python setup.py sdist

	2 - Create a .deb (on a debian) after editing stdeb.cfg :
		> ./build_deb.sh

	3 - Create a .deb (from any machine, using vagrant) after editing stdeb.cfg : 
		> ./build_deb_vagrant.sh


