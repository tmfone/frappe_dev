from setuptools import setup, find_packages

with open("requirements.txt") as f:
	install_requires = f.read().strip().split("\n")

# get version from __version__ variable in frappe_dev/__init__.py
from frappe_dev import __version__ as version

setup(
	name="frappe_dev",
	version=version,
	description="Tools to help develop custom apps",
	author="tmf.one",
	author_email="info@tmf.one",
	packages=find_packages(),
	zip_safe=False,
	include_package_data=True,
	install_requires=install_requires
)
