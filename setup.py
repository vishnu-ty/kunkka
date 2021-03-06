import os

from setuptools import setup, find_packages

here = os.path.abspath(os.path.dirname(__file__))
README = open(os.path.join(here, 'README.txt')).read()
CHANGES = open(os.path.join(here, 'CHANGES.txt')).read()

requires = [
    'pyramid_mako', 
    'pyramid',
    'SQLAlchemy',
    'transaction',
    'pyramid_tm',
    'pyramid_debugtoolbar',
    'zope.sqlalchemy',
    'waitress',
    'mysql-python',    
#    'cryptacular',
#    'pycrypto',
    'pymongo',
    'ordereddict',
    'certifi',
    'google-api-python-client',
    'simplejson', #only required for python 2.6
    'fabric',
    'paste'
    #'pylibmc' # need to install manually
    ]

setup(name='kunkka',
      version='0.0',
      description='kunkka',
      long_description=README + '\n\n' + CHANGES,
      classifiers=[
        "Programming Language :: Python",
        "Framework :: Pyramid",
        "Topic :: Internet :: WWW/HTTP",
        "Topic :: Internet :: WWW/HTTP :: WSGI :: Application",
        ],
      author='Heera',
      author_email='heera.jaiswal810@gmail.com',
      url='',
      keywords='web wsgi bfg pylons pyramid',
      packages=find_packages(),
      include_package_data=True,
      zip_safe=False,
      test_suite='kunkka',
      install_requires=requires,
      entry_points="""\
      [paste.app_factory]
      main = kunkka:main
      [console_scripts]
      initialize_kunkka_db = kunkka.scripts.initializedb:main
      """,
      )
