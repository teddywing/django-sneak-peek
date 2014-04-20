import os

from setuptools import setup, find_packages


setup(
    name='django-sneak-peek',
    version='0.0.1',
    description='',
    long_description='',
    url='',
    license='MIT',
    author='Teddy Wing',
    author_email='',
    include_package_data=True,
    packages=find_packages(),
    install_requires=[
        'Django >= 1.4'
    ],
    extras_require={
        'South': ['South']
    },
    classifiers=[],
)