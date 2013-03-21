# -*- coding: utf-8 -*-
"""
wsgi-liveserver provides a simple LiverServerTestCase class that can be used to
help start a web server in the background to serve a WSGI compliant application
for use with testing. Generally it will be used in conjuction with something
like Selenium to perform a series of functional tests using a browser.

Licensed under the GNU GPL v3

Copyright (c) 2013 John Kristensen (unless explicitly stated otherwise).
"""

__author__ = 'John Kristesen'
__version__ = '0.1'
__license__ = 'GPLv3'

import multiprocessing
import socket
import time
import unittest
from wsgiref.simple_server import make_server, WSGIRequestHandler


class QuietHandler(WSGIRequestHandler):
    def log_request(*args, **kwargs):
        pass


class LiveServerTestCase(unittest.TestCase):
    def create_app(self):
        """Create your wsgi app and return it."""
        raise NotImplementedError

    def __call__(self, result=None):
        """
        Do some custom setup stuff and then hand off to TestCase to do its
        thing.
        """
        try:
            self._pre_setup()
            super(LiveServerTestCase, self).__call__(result)
        finally:
            self._post_teardown()

    def url_base(self):
        """Return the url of the test server."""
        return 'http://{0}:{1}'.format(self.host, self.port)

    def _pre_setup(self):
        """Setup and start the test server in the background."""
        server = None
        port_range = (8080, 8090)

        self.host = 'localhost'
        self.port = port_range[0]
        self._process = None

        # Get the app
        self.app = self.create_app()

        # Cycle through the port range to find a free port
        while server is None and self.port <= port_range[1]:
            try:
                server = make_server(self.host, self.port, self.app,
                                     handler_class=QuietHandler)
            except socket.error as e:
                self.port += 1

        # No free port, raise an exception
        if server is None:
            raise socket.error('Ports {0}-{1} are all already in use'.format(
                *port_range))

        # Start the test server in the background
        self._process = multiprocessing.Process(target=server.serve_forever)
        self._process.start()

        # Give the test server a bit of time to prepare for handling requests
        time.sleep(1)

    def _post_teardown(self):
        """Stop the test server."""
        if self._process is not None:
            self._process.terminate()
