MANAGE := python manage.py

.PHONY: help
help: ## Show this help
	@egrep -h '\s##\s' $(MAKEFILE_LIST) | sort | awk 'BEGIN {FS = ":.*?## "}; {printf "\033[36m%-20s\033[0m %s\n", $$1, $$2}'

.PHONY: install
install: venv ## Make a new virtual environment and Install dependencies
	pipenv shell
	pipenv install

freeze: ## Pin current dependencies
	pipenv run pip freeze > requirements.txt

.PHONY: venv
venv: ## Make a new virtual environment
	python3 -m ven venv

pip: ## Pin current dependencies
	pip install -r requirements.txt

migrate: ## Make and run migrations
	$(MANAGE) makemigrations
	$(MANAGE) migrate

collectstatic: ## Run collectstatic
	$(MANAGE) collectstatic --noinput

changepassword: ## Change password superuser
	$(MANAGE) changepassword users@pm.me

.PHONY: test
test: ## Run tests
	$(MANAGE) --verbosity=0 --parallel --failfast

.PHONY: createsuperuser
createsuperuser: ## Run the Django server
	$(MANAGE) createsuperuser --email="users@pm.me"

dumpdata: ## dump data
	$(MANAGE) dumpdata --indent=4 --natural-foreign --natural-primary -e contenttypes --format=json user.user > fixtures/user.json

loaddata: ## load data
	$(MANAGE) loaddata fixtures/*.json
