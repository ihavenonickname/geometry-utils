rm -rf dist/* && python3 setup.py sdist bdist_wheel && twine check dist/* && python3 -m twine upload --repository-url https://test.pypi.org/legacy/ dist/*
