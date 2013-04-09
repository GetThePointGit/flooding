from setuptools import setup
import os.path

version = '1.67'

long_description = '\n\n'.join([
    open('README.rst').read(),
    open('TODO.txt').read(),
    open('CREDITS.txt').read(),
    open('CHANGES.txt').read(),
    ])

install_requires = [
    'Django',
    'django-extensions',
    'django-staticfiles',
    'django-nose',
    'gunicorn',
    'flooding-base >= 1.25',
    'flooding-lib >= 1.30',
    'lizard-worker',
    'nens >= 1.11',
    'supervisor',
    'south',
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
      extras_require = {'test': tests_require},
      entry_points={
          'console_scripts': [
          ]},
      )
