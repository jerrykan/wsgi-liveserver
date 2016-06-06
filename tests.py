import unittest
from wsgiref.simple_server import demo_app

from wsgi_liveserver import LiveServerTestCase

# Python 2/3 compatibility
try:
    # Python 3
    from urllib.request import urlopen
except ImportError:
    # Python 2
    from urllib2 import urlopen


class LiveServerTest(LiveServerTestCase):
    def create_app(self):
        return demo_app

    def test_server_running(self):
        self.assertNotEqual(self._thread, None)
        self.assertTrue(self._thread.is_alive())

    def test_server_listening(self):
        response = urlopen(self.url_base())
        self.assertEqual(response.code, 200)
        self.assertTrue(b'Hello world!' in response.read())


class ConfiguredPortTest(LiveServerTestCase):
    port_range = (20080, 20090)

    def create_app(self):
        return demo_app

    def test_configured_port(self):
        self.assertEqual(self.port, 20080)

    def test_server_listening(self):
        response = urlopen(self.url_base())
        self.assertEqual(response.code, 200)
        self.assertTrue(b'Hello world!' in response.read())


if __name__ == '__main__':
    unittest.main()
