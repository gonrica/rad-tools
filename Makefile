.DEFAULT_GOAL := help

# You can set these variables from the command line, and also
# from the environment for the first two.
SPHINXOPTS    ?=
SPHINXBUILD   ?= sphinx-build
SOURCEDIR     = source
BUILDDIR      = build

# Put it first so that "make" without argument is like "make help".
# help:
# 	@$(SPHINXBUILD) -M help "docs/$(SOURCEDIR)" "docs/$(BUILDDIR)" $(SPHINXOPTS) $(O)

# $(O) is meant as a shortcut for $(SPHINXOPTS).
html: 
	@make examples
	@$(SPHINXBUILD) -M html "docs/$(SOURCEDIR)" "docs/$(BUILDDIR)" $(SPHINXOPTS) $(O)

clean:
	-@rm -r docs/build
	-@rm -r docs/source/api/_autosummary
	-@rm -r rad_tools.egg-info
	-@rm -r build
	-@rm -r dist

test:
	@pip3 install . --upgrade
	@pip3 install pytest
	@pytest -s

pip:
#   @echo "\x1b[33m"
#	@echo "pip is disabled for your own safety"
#	@echo "\x1b[0m"
	-@rm -r dist
	-@rm -r build
	-@rm -r rad_tools.egg-info
	@python3 setup.py sdist bdist_wheel 
	@python3 -m twine upload --repository pypi dist/* --verbose

help:
	@echo "\x1b[31m"
	@echo "Please specify what do you want to do!"
	@echo "\x1b[32m"
	@echo "Available options are:"
	@echo "    test - for executing the testing suite"
	@echo "    html - for building the html docs"
	@echo "    pip - for publishing the package to PyPi index"
	@echo "    clean - for cleaning all files from docs and pip routines"
	@echo "    examples - for updating all examples"
	@echo "    push - for git push with updated examples"
	@echo "\x1b[0m"

examples:
	@pip3 install . --upgrade
	@identify-wannier-centres.py docs/examples/identify-wannier-centres/example_centres.xyz -nc > docs/examples/identify-wannier-centres/console_output.txt
	@identify-wannier-centres.py docs/examples/identify-wannier-centres/example_centres.xyz --span 0.11 --output-name example_centres.xyz_bigger_span
	@rad-make-template.py -op docs/examples/rad-make-template -on template_demo.txt

push: examples
	@git push
