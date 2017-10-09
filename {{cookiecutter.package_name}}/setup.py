"""
setuptools module for project.
"""

import setuptools

setuptools.setup(
    name="{{cookiecutter.package_name}}",
    version="{{cookiecutter.package_version}}",
    url="https://github.com/{{ cookiecutter.github_username }}/{{ cookiecutter.package_name }}",

    author="{{ cookiecutter.author_name }}",
    author_email="{{ cookiecutter.author_email }}",

    description="{{ cookiecutter.package_description }}",
    long_description=open('README.rst').read(),

    packages=setuptools.find_packages(),

    install_requires=[],

    classifiers=[
        'Development Status :: 2 - Pre-Alpha',
        'Programming Language :: Python',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.4',
        'Programming Language :: Python :: 3.5',
        'Programming Language :: Python :: 3.6',
    ],

    entry_points={
        'console_scripts': ['{{ cookiecutter.package_name }}={{ cookiecutter.package_name }}.command_line:main'],
    },

    test_suite='nose.collector',
    tests_require=['nose'],

    include_package_data=True,
    zip_safe=False,
)
