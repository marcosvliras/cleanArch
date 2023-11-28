.PHONY: test

test:
	python3 -m pytest --cache-clear -s -v 

.PHONY: update-requirements

update-requirements:
	python3 -m pip freeze > requirements.txt
	git add requirements.txt

.PHONY: lint

lint:
	python3 -m black . -l79

.PHONY: lint-check

lint-check:
	pylint src -rn -sn --rcfile=.pylintrc --load-plugins=pylint.extensions.docparams
