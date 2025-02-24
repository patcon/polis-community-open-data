install: ## Install dependencies
	uv sync

update-csv: ## Update CSV of closed conversations
	uv run scripts/update_convo_csv.py

fetch-data: ## Fetch Polis datasets
	uv run scripts/fetch_polis_datasets.py

clear-test-cache: ## Clear the SQLite database of cached HTTP requests
	rm -f test_cache.sqlite


# These make tasks allow the default help text to work properly.
%:
	@true

.PHONY: help

help:
	@echo 'Usage: make <command>'
	@echo
	@echo 'where <command> is one of the following:'
	@echo
	@grep -E '^[a-zA-Z_-]+:.*?## .*$$' $(MAKEFILE_LIST) | awk 'BEGIN {FS = ":.*?## "}; {printf "\033[36m%-20s\033[0m %s\n", $$1, $$2}'

.DEFAULT_GOAL := help
