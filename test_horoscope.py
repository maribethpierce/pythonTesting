import unittest
from horoscope import horoscope

class TestHoroscope(unittest.TestCase):
	def setUp(self):
		pass

	def test_capricorn_mid(self):
		self.assertEqual( horoscope("January, 3"), 'Capricorn' )

	def test_capricorn_start(self):
		self.assertEqual( horoscope('December, 22'), 'Capricorn' )

	def test_capricorn_end(self):
		self.assertEqual( horoscope('January, 19'), 'Capricorn' )

	def test_incorrect_format_month(self):
		self.assertIsNone( horoscope(1) )


suite = unittest.TestLoader().loadTestsFromTestCase(TestHoroscope)
unittest.TextTestRunner(verbosity=2).run(suite)

# if __name__ == '__main__':
# 	unittest.main()

# file: test_horoscope.py
# expect horoscope(january) == "Capricorn"
# expect horoscope(2018) == NIL
# expect horoscope(1) == "Capricorn"

