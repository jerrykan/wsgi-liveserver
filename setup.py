import os
from distutils.core import setup

import wsgi_liveserver


def read(filename):
    return open(os.path.join(os.path.dirname(__file__), filename)).read()


setup(
    name='wsgi-liveserver',
    version=wsgi_liveserver.__version__,
    description='start/stop WSGI applications in the background for '
                'functional testing',
    author=wsgi_liveserver.__author__,
    author_email='john@jerrykan.com',
    license='GPLv3',
    keywords='wsgi liveserver',
    url='http://github.com/jerrykan/wsgi-liveserver/',
    long_description=read('README.rst'),
    py_modules=['wsgi_liveserver'],
    platforms='any',
    classifiers=[
        'Development Status :: 5 - Production/Stable',
        'Environment :: Web Environment',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: GNU General Public License v3 (GPLv3)',
        'Programming Language :: Python :: 2',
        'Programming Language :: Python :: 2.6',
        'Programming Language :: Python :: 2.7',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.3',
        'Programming Language :: Python :: 3.4',
        'Programming Language :: Python :: 3.5',
        'Topic :: Internet :: WWW/HTTP :: WSGI',
        'Topic :: Software Development :: Testing',
    ],
)
