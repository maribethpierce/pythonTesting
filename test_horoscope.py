from horoscope import horoscope
from random import randint
from datetime import datetime
from faker import Faker
fake = Faker()

#  Test each sign within its date range
def test_capricorn():
	assert( horoscope(1) == "Capricorn")

def test_aquarius():
	assert( horoscope(2) == "Aquarius")

def test_pisces():
	assert( horoscope(3) == "Pisces")

def test_aries():
	assert( horoscope(4) == "Aries")

def test_taurus():
	assert( horoscope(5) == "Taurus")

def test_gemini():
	assert( horoscope(6) == "Gemini")

def test_cancer():
	assert( horoscope(7) == "Cancer")

def test_leo():
	assert( horoscope(8) == "Leo")

def test_virgo():
	assert( horoscope(9) == "Virgo")

def test_libra():
	assert( horoscope(10) == "Libra")

def test_scorpio():
	assert( horoscope(11) == "Scorpio")

def test_sagittarius():
	assert( horoscope(12) == "Sagittarius")

def test_non_month():
	assert( horoscope(13) == None )

def test_empty_input():
	empty_string = ""
	assert( horoscope(empty_string) == None )
