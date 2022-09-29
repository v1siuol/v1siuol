# Build README

[![Tests](https://github.com/v1siuol/v1siuol/actions/workflows/test.yml/badge.svg)](https://github.com/v1siuol/v1siuol/actions/workflows/test.yml)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](./build_readme/LICENSE.md)

Build README is an automatic app that builds a decent section on your public profile.

Demo: https://github.com/v1siuol

## Features
- Powerful skeleton.
- Easy to configure.
- Deploy automatically.

## Requirements
- python (3.6+)
- pip

## Installation
1. Fork this repository.
2. Create a virtual environment if you would like to.
3. `make init`
4. Edit `build_readme/config.py` to generate your own content.
5. `python build_readme/build_readme.py > README.md`

## Repository contents
*with respect to the root directory*
- **build_readme/config.py**: Custom configurations.
- **Makefile**: Handy and useful tool to communicate with python codes. You can reference commands here.
- **build_readme/build_readme.py**: Main interface to build README.md: Start here.
- **build_readme/layout/**: Control different parts of layout.
- **.github/workflows/**: CI/CD using GitHub Actions.

## Contents
- **GitHub Stats Card.** To configure your own GitHub Stats Card, please refer to [github-readme-stats](https://github.com/anuraghazra/github-readme-stats).
- **Blog.** To fetch your own posts, please generate an RSS feed of your blog.

## Tests
1. `pip install -r build_readme/requirements-dev.txt`
2. `make mypy`
3. `make pylint`
4. `make test`
