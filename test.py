import unittest
import app as test_app
import json

class FlaskAppTests(unittest.TestCase):

	def setUp(self):
		self.app = test_app()

	def test_get_hello_endpoint(self):
		r = self.app.get('/')
		self.assertEqual(r.status, '200 OK')
		self.assertEqual(r.data, 157)
		self.assertIsNotNone(r.data)
		self.assertGreater(r.data, 0)

if __name__ =='__main__':
	unittest.main()
