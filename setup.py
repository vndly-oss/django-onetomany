import re
from distutils.core import setup
import os


CLASSIFIERS = [
    'Environment :: Web Environment',
    'Framework :: Django',
    'Intended Audience :: Developers',
    'License :: OSI Approved :: BSD License',
    'Operating System :: OS Independent',
    'Programming Language :: Python',
    'Topic :: Software Development :: Libraries :: Application Frameworks',
]


def get_version(filename):
    path = os.path.join(os.path.dirname(__file__), filename)
    with open(path, encoding="utf-8") as handle:
        content = handle.read()
    return re.search(r'__version__ = "([^"]+)"', content).group(1)


setup(
    name='django-onetomany',
    version=get_version('onetomany/__init__.py'),
    author='Adi Sieker',
    author_email='adi@sieker.io',
    packages=['onetomany',],
    url='http://github.com/adsworth/django-onetomany/',
    platforms=['OS Independent'],
    license='LICENSE.txt',
    classifiers=CLASSIFIERS,
    description='A django relation field.',
    long_description=open(os.path.join(os.path.dirname(__file__), 'README.rst')).read(),
    install_requires=[
        "Django >= 1.5",
    ],
)
