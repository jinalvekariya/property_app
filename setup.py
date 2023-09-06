from setuptools import setup, find_packages

with open("requirements.txt") as f:
	install_requires = f.read().strip().split("\n")

# get version from __version__ variable in property_app/__init__.py
from property_app import __version__ as version

setup(
	name="property_app",
	version=version,
	description="Property Management System",
	author="Jinal Balar",
	author_email="vekariyajinal7@gmail.com",
	packages=find_packages(),
	zip_safe=False,
	include_package_data=True,
	install_requires=install_requires
)
