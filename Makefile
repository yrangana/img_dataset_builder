install:
		pip install --upgrade pip &&\
		pip install -r requirements.txt

format:
		black  */*.py *.py

test:
		python -m pytest -vv

lint:
		pylint --disable=R,C *.py */*.py

all: install format lint 