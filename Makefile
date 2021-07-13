SHELL = /bin/sh

.PHONY: init mypy pylint test dev build clean

init:
	pip install -r requirements.txt  # Install dependencies

mypy:
	mypy --ignore-missing-imports build_readme

pylint:
	pylint build_readme

test:
	@printf "WIP\n"

dev:
	python build_readme/build_readme.py > README-dev.md  # For development

build:
	python build_readme/build_readme.py > README.md  # For release

clean:
	rm README-dev.md

help:
	@printf "Usage: make [options]\n"
	@printf "Options:\n"
	@printf "  %-10s %s\n" "init" ""
	@printf "  %-10s %s\n" "mypy" ""
	@printf "  %-10s %s\n" "pylint" ""
	@printf "  %-10s %s\n" "test" ""
	@printf "  %-10s %s\n" "dev" ""
	@printf "  %-10s %s\n" "build" ""
	@printf "  %-10s %s\n" "clean" ""
