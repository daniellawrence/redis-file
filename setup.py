#!/usr/bin/env
"""
RedisFile
===============

This is a simple hack to allow the writing to redis as if it was
just file object in python.

Usage
-----

    # Import and open up a ne "file"
    from redisfile import RedisFile
    f = RedisFile("myrediskey")
    # Write some lines to the "file"
    f.write('hello')
    f.writelines('world')
    f.writelines('Your\nAwesome')
    # Read the whole file
    print f.read()
    # Reading a file from the end shows no data
    print f.read()
    # seek to the start of the file
    f.seek(0)
    # Read a single line
    print f.readline()
    # Read the rest
    print f.read()
    # "close" will delete all the data
    f.close()

Installation
------------

Installation is simple too::

    $ pip install redis-file
"""
from setuptools import setup

setup(
    name="redis-file",
    version="0.0.1",

    description="Write to redis as if it was a file",
    long_description=__doc__,
    url="https://github.com/daniellawrence/redis-file",

    author="Daniel Lawrence",
    author_email="dannyla@linux.com",

    install_requires=["redis"],

    py_modules=["redisfile"],
    include_package_data=True,

    zip_safe=False,
)
