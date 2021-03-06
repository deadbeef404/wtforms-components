"""
WTForms-Components
------------------

Additional fields, validators and widgets for WTForms.
"""

from setuptools import setup
import sys


PY3 = sys.version_info[0] == 3


extras_require = {
    'test': [
        'pytest==2.2.3',
        'Pygments>=1.2',
        'Jinja2>=2.3',
        'docutils>=0.10',
        'flexmock>=0.9.7',
        'psycopg2>=2.4.6',
        'WTForms-Test>=0.1.1'
    ],
    'babel': ['Babel>=1.3'],
    'arrow': ['arrow>=0.3.4'],
    'phone': ['phonenumbers>=5.9.2'],
    'password': ['passlib >= 1.6, < 2.0'],
    'color': ['colour>=0.0.4'],
    'ipaddress': ['ipaddr'] if not PY3 else [],
    'timezone': ['python-dateutil'],
}


# Add all optional dependencies to testing requirements.
for name, requirements in extras_require.items():
    if name != 'test':
        extras_require['test'] += requirements


setup(
    name='WTForms-Components',
    version='0.9.3',
    url='https://github.com/kvesteri/wtforms-components',
    license='BSD',
    author='Konsta Vesterinen',
    author_email='konsta@fastmonkeys.com',
    description='Additional fields, validators and widgets for WTForms.',
    long_description=__doc__,
    packages=[
        'wtforms_components',
        'wtforms_components.fields'
    ],
    zip_safe=False,
    include_package_data=True,
    platforms='any',
    dependency_links=[
        # 5.6b1 only supports python 3.x / pending release
        'git+git://github.com/daviddrysdale/python-phonenumbers.git@python3'
        '#egg=phonenumbers3k-5.6b1',
    ],
    install_requires=[
        'WTForms>=1.0.4',
        'SQLAlchemy>=0.8.0',
        'SQLAlchemy-Utils>=0.23.0',
        'six>=1.4.1',
        'validators>=0.5.0',
        'intervals>=0.2.0'
    ],
    extras_require=extras_require,
    classifiers=[
        'Environment :: Web Environment',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: BSD License',
        'Operating System :: OS Independent',
        'Programming Language :: Python',
        'Topic :: Internet :: WWW/HTTP :: Dynamic Content',
        'Topic :: Software Development :: Libraries :: Python Modules'
    ]
)
