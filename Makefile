test:
	python3 -m pytest --cache-clear -s -v 


update-requirements:
	python3 -m pip freeze > requirements.txt
	git add requirements.txt


lint:
	python3 -m black . -l79


lint-check:
	pylint src -rn -sn --rcfile=.pylintrc --load-plugins=pylint.extensions.docparams
