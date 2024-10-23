from setuptools import setup, find_packages

setup(
   name="my-python-project",
   version="1.0.0",
   packages=find_packages(where="src"),
   package_dir={"": "src"},
   entry_points={
       'console_scripts': [
           'myapp = app:main',
        ],
   },
) 
