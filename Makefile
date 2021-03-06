PYTHON = python3
PROJECT_DIR = src/pyqt5-rps
PROJECT_MAIN = ${PROJECT_DIR}/pyqt5-rps.py


.DEFAULT_GOAL = help

.PHONY: help setup clean test build upload standalone install run

help:
	@echo "---------------HELP-----------------"
	@echo "make help - display this message"
	@echo "make setup - setup the project for development"
	@echo "make clean - clean the project"
	@echo "make test - run tests on the project"
	@echo "make build - build the project"
	@echo "make upload - upload the project to PyPI"
	@echo "make standalone - build standalone application"
	@echo "make install - install the project to local python installation"
	@echo "make run - run the project"
	@echo "------------------------------------"

setup: clean
	@echo "Setting up project"
	sudo apt-get install python3-pyqt5 qtcreator
	${PYTHON} -m pip install -r requirements.txt
	${PYTHON} -m pip install -r ${PROJECT_DIR}/requirements.txt

clean:
	@echo "Cleaning project"
	rm --force *.bin
	find . -name '*.pyc' -exec rm --force {} +
	find . -name '*.pyo' -exec rm --force {} +
	find . -name '*.egg-info' -exec rm --force {} +
	rm --force --recursive build/
	rm --force --recursive dist/
	rm --force --recursive *.build/
	rm --force --recursive *.dist/

test:
	${PYTHON} -m nose2 -v

build: clean
	@echo "Building project"

upload: clean
	@echo "Uploading project"
	${PYTHON} setup.py sdist bdist_wheel
	${PYTHON} -m twine upload dist/*

standalone: clean
	@echo "Building standalone application"

install: clean
	@echo "Installing project"
	${PYTHON} -m pip install .

run: clean
	@echo "Running project"
	${PYTHON} ${PROJECT_MAIN}