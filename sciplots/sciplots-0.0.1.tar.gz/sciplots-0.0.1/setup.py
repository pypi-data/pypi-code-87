#!/usr/bin/env python
#-*- coding:utf-8 -*-

#############################################
# File Name: setup.py
# Author: Songyan Zhu
# Mail: zhusy93@gmail.com
# Created Time:  2021-06-09 08:22
#############################################


from setuptools import setup, find_packages

setup(
	name = "sciplots",
	version = "0.0.1",
	keywords = ("scientific plots for academic publications"),
	description = "draw and basic calculations/conversions",
	long_description = "coming soon",
	license = "MIT Licence",

	url="https://github.com/soonyenju/sciplots",
	author = "Songyan Zhu",
	author_email = "zhusy93@gmail.com",

	packages = find_packages(),
	include_package_data = True,
	platforms = "any",
	install_requires=[

	]
)