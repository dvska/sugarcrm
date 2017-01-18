"""
    setupTools based setup script for

    To install: python setup.py install

"""

from distutils.core import setup

version = '0.3.3'

PACKAGES = ['sugarcrm']

setup(name='sugarcrm',
      version=version,
      description="SugarCRM Python library",
      author="Daniel Casper, et al",
      author_email="dancasper@gmail.com",
      url="http://github.com/dvska/sugarcrm",
      classifiers=["Programming Language :: Python",
                   "Inteded Audience :: Developers",
                   "Topic :: Office/Business"],
      keywords="Customer Relationship Management SugarCRM CRM",
      packages=PACKAGES,
      install_requires=['simplejson>=2.2', 'six>=1.4.1']
      )
