# Makefile for Projectify!

# Variables
VERSION_PART := patch
PACKAGE_NAME := projectify

# Determina el sistema operativo (Windows o no)
ifeq ($(OS),Windows_NT)
    RM := rmdir /S /Q
    SHELL := cmd
    FIND := findstr
else
    RM := rm -rf
    SHELL := /bin/sh
    FIND := grep
endif

# Incrementa la versión del paquete
bump_version:
	@bump2version $(VERSION_PART) --allow-dirty || echo "Error: bump2version command failed."

# Verifica si el directorio de trabajo está limpio (Git)
check_git_clean:
	@if git status --porcelain | $(FIND) . ; then \
		echo "Error: Git working directory is not clean."; \
		echo "Please commit or stash your changes before running this command."; \
		exit 1; \
	else \
		echo "Git working directory is clean."; \
	fi

# Crea y envía un tag al repositorio
tag_release: bump_version
	@git tag $(shell git describe --tags --abbrev=0) || echo "Error: Failed to create tag."
	@git push origin $(shell git describe --tags --abbrev=0) || echo "Error: Failed to push tag."

# Verifica la configuración del paquete
check:
	@python setup.py check || echo "Error: setup.py check failed."

# Limpia los archivos generados por la construcción
clean:
	@$(RM) build dist $(PACKAGE_NAME).egg-info || echo "Nothing to clean."

# Construye el paquete (sdist y bdist_wheel)
build: clean
	@python setup.py sdist bdist_wheel || echo "Error: Failed to build the package."

# Sube el paquete a PyPI
upload: build
	@twine upload dist/* || echo "Error: Failed to upload to PyPI."

# Publica automáticamente una nueva versión
release: check_git_clean tag_release check upload
