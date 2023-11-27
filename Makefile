.PHONY: test

test:
	python3 -m pytest -s -v

.PHONY: update-requirements

update-requirements:
	python3 -m pip freeze > requirements.txt
	git add requirements.txt
