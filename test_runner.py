import unittest
import runner 

class TestRunner(unittest.TestCase):
	def test_hello(self):
		self.assertEqual(runner.hello(), "hello")

if __name__ == '__main__':
	unittest.main()

