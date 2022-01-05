#!/usr/bin/env python3

"""
setup.py file for webcam2rgb
"""

from setuptools import setup

setup (name = 'webcam2rgb',
       version = '1.0.0',
       author      = "Bernd Porr",
       author_email = "mail@berndporr.me.uk",
       url = "https://github.com/berndporr/webcam2rgb",
       description = 'Central pixel data to datastream',
       py_modules = ["webcam2rgb"],
       license='MIT',
       install_requires=[
           'numpy',
           'opencv-contrib-python',
           'opencv-python'
       ],
       classifiers=[
          'Intended Audience :: Developers',
          'Operating System :: POSIX',
	  'Operating System :: Microsoft :: Windows',
          'Programming Language :: Python :: 3',
          ]
      )
