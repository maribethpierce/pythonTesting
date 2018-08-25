from horoscope import horoscope
from random import randint
from datetime import datetime
from faker import Faker
fake = Faker()
import array
signs = [
	"Capricorn",
	"Aquarius",
	"Pisces",
	"Aries",
	"Taurus",
	"Gemini",
	"Cancer",
	"Leo",
	"Virgo",
	"Libra",
	"Scorpio",
	"Sagittarius"
]



#  Test each sign within its date range
def test_horoscope():
	for sign in signs:
		sign_index = signs.index(sign) + 1 
		err_message = "Sign for month %s should be %s" % (sign_index, sign)
		assert( horoscope(sign_index ) == sign ), err_message

def test_non_month():
	assert( horoscope(13) == None )

def test_empty_input():
	empty_string = ""
	assert( horoscope(empty_string) == None )
