create-venv:
	python3 -m venv venv
	source venv/bin/activate

create-venv-windows:
	python3 -m venv venv
	\path\to\env\Scripts\activate

install-dependencies:
	pip3 install -r requirements.txt

start-database:
	python3 manage.py db init
	python3 manage.py db migrate
	python3 manage.py db upgrade

start-app:
	export FLASK_ENV=development 
	python3 manage.py run

start-app-windows:
	set FLASK_ENV=development
	python3 manage.py run

run-test:
	pytest -v './app/test'

run-coverage:
	pytest -v --cov-report term-missing --cov=app --cov-fail-under=80