# Libero Search
The purpose of this project is to provide the ability to search indexed data via the
`/search` endpoint.


## Dependencies

* [Docker](https://www.docker.com/)

## Getting started
This project provides a `Makefile` with short commands to run common tasks.

```bash
make help
```
Run this for a full list of commands.

```bash
make start
```
This command will build and/or run the site locally configured for development purposes.

```bash
make stop
```
Use this command to stop containers and clean up any anonymous volumes.

## Running the tests
```bash
make tests
```
Use this command to run unit tests.

```bash
make checks
```
Use this command to run static checks such as: mypy, flake8, pylint.

```bash
make all-tests
```
Combines the two commands above by running all checks followed by unit tests

## Adding and removing dependencies

The following commands update files that keep track of project dependencies.
```bash
make build
```
Run this if you would like to persist changes to dependencies to your docker container.

```bash
make dependency package=<package name>
make dev-dependency package=<package name>

# examples:
make dependency package=flask
make dependency package=flask==1.0.2
make dev-dependency package=pytest
```
Run either of these commands to add a python package as a project dependency or 
development dependency alike. You can specify just the package name to get the 
latest version or specify a specific version number.

```bash
make remove-dependency package=<package name>
make remove-dev-dependency package=<package name>
```
Run either of these commands to remove dependencies accordingly.

## Other useful commands
```bash
make run
```
Use this command to only run the python service.
It is possible to use pdb breakpoints with this configuration.

```bash
make shell
```
Use this to run the python container that would run the application and enter a
bash prompt.

```bash
make dependency-tree
# or
make d-tree
```
Use this to display a dependency tree

```bash
make fix-imports
```
When checks are run warnings are displayed because imports do not follow the
project conventions as specified in `setup.cfg` under `[isort]`.
Use this command to automatically fix imports for all project python files.