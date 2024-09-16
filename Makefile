dev:
	set FLASK_DEBUG=1
	set FLASK_APP=main.py
	set FLASK_ENV=development
	flask run

var:
	@echo FLASK_DEBUG=%FLASK_DEBUG%
	@echo FLASK_APP=%FLASK_APP%
	@echo FLASK_ENV=%FLASK_ENV%