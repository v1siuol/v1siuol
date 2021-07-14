SHELL = /bin/sh

.PHONY: init mypy pylint test dev build clean

init:
	pip install -r build_readme/requirements.txt  # Install dependencies

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
	@printf "  %-10s %s\n" "init" "Install dependencies."
	@printf "  %-10s %s\n" "mypy" "Run static type checker."
	@printf "  %-10s %s\n" "pylint" "Run linter."
	@printf "  %-10s %s\n" "test" "Run tests."
	@printf "  %-10s %s\n" "dev" "Build README-dev.md in development."
	@printf "  %-10s %s\n" "build" "Build README.md."
	@printf "  %-10s %s\n" "clean" "Clean README-dev.md."
