import unittest
import urllib2
from wsgiref.simple_server import demo_app

from wsgi_liveserver import LiveServerTestCase


class LiveServerTest(LiveServerTestCase):
    def create_app(self):
        return demo_app

    def test_server_running(self):
        self.assertNotEqual(self._thread, None)
        self.assertTrue(self._thread.is_alive())

    def test_server_listening(self):
        response = urllib2.urlopen(self.url_base())
        self.assertEqual(response.code, 200)
        self.assertTrue('Hello world!' in response.read())


if __name__ == '__main__':
    unittest.main()
