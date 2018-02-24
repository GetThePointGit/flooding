from setuptools import setup
import monkeypatch_setuptools


version = '1.96dev'

long_description = '\n\n'.join([
    open('README.rst').read(),
    open('CHANGES.txt').read(),
    ])

install_requires = [
    'Django > 1.4.0, < 1.7',
    'django-extensions',
    'django-nose',
    'flooding-lib >= 2.92',
    'gislib',
    'gunicorn',
    'lizard-worker',
    'nens >= 1.11',
    'raven',
    'south',
    'supervisor',
    'flask',
    'django-markdown-deux'
    ],

tests_require = [
    ]

setup(name='flooding',
      version=version,
      description="TODO",
      long_description=long_description,
      # Get strings from http://www.python.org/pypi?%3Aaction=list_classifiers
      classifiers=['Programming Language :: Python',
                   'Framework :: Django',
                   ],
      keywords=[],
      author='TODO',
      author_email='TODO@nelen-schuurmans.nl',
      url='',
      license='GPL',
      packages=['flooding'],
      include_package_data=True,
      zip_safe=False,
      install_requires=install_requires,
      tests_require=tests_require,
      extras_require={'test': tests_require},
      entry_points={
          'console_scripts': [
            'runflask=raster_server.server:run',
            'gunicorn=flooding.gunicorn_wsgi_wrapper:run',
          ]},
      )
