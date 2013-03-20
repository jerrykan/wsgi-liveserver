wsgi-liveserver
===============
wsgi-liveserver provides a simple LiverServerTestCase class that can be used to
help start a web server in the background to serve a WSGI compliant application
for use with testing. Generally it will be used in conjuction with something
like Selenium to perform a series of functional tests using a browser.

Licensed under the GNU GPL v3

Copyright (c) 2013 John Kristensen (unless explicitly stated otherwise).


Installation and Dependencies
-----------------------------
Install wsgi-liveserver with ``pip install wsgi-liveserver`` or just `download
wsgi_liveserver.py <http://github.com/jerrykan/wsgi-liveserver>`_ and place it
in your project directory. There are no dependencies other than the Python
Standard Library.


Usage
-----
The wsgi-liveserver LiveServerTestCase can be used instead of unittest.TestCase
for any tests that require a running web server. Simply define a create_app()
method that returns the wsgi application that you want to have started up in
the background, then write your tests as normal. LiveServerTestCase will handle
starting and stopping the server for you.


Example
-------
The following is a very basic example of using wsgi-liveserver with the
`wsgiref demo_app
<http://docs.python.org/2/library/wsgiref.html#wsgiref.simple_server.demo_app>`_:

.. code-block:: python

    import unittest
    from wsgiref.simple_server import demo_app
    from selenium import webdriver
    from wsgi_liveserver import LiveServerTestCase

    class SimpleTest(LiveServerTestCase):
        def create_app(self):
            return demo_app

        def setUp(self):
            self.driver = webdriver.Firefox()

        def tearDown(self):
            self.driver.close()

        def test_page_title(self):
            self.driver.get(self.url_base())
            self.assertTrue('Hello world!' in self.driver.page_source)

    if __name__ == '__main__':
        unittest.main()


Another simple but fully functional `bottle <http://bottlepy.org/>`_ web
application with tests can be found at:
https://github.com/jerrykan/bottle-selenium


Contact
-------
Send your questions, comments, patches to John Kristensen <john@jerrykan.com>
