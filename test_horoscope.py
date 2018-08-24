from horoscope import horoscope
from random import randint
from datetime import datetime
from faker import Faker
fake = Faker()

# signs = {
# 	"Aries" : "March 21 - April 19"
# 	"Taurus" : "April 20 - May 20"
# 	"Gemini" : "May 21 - June 20"
# 	"Cancer" : "June 21 - July 22"
# 	"Leo" : "July 23 - August 22"
# 	"Virgo" : "August 23 - September 22"
# 	"Libra" : "September 23 - October 22"
# 	"Scorpio" : "October 23 - November 21"
# 	"Sagittarius" : "November 22 - December 21"
# 	"Capricorn" : "December 22 - January 19"
# 	"Aquarius" : "January 20 - February 18"
# 	"Pisces" : "February 19 - March 20"
# }

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
	assert( horoscope(13) == None)

#  Test acceptable date input formats
def test_date_input_format_1():
	date_format = "January 12"
	assert( horoscope(date_format) == "Capricorn")

def test_date_input_format_2():
	date_format = "January 12, 1963"
	assert( horoscope(date_format) == "Capricorn")

def test_date_input_format_3():
	date_format = "01/12"
	assert( horoscope(date_format) == "Capricorn")

def test_date_input_format_4():
	date_format = "01/12/1963"
	assert( horoscope(date_format) == "Capricorn")

def test_date_input_format_5():
	date_format = "12 January"
	assert( horoscope(date_format) == "Capricorn")

def test_date_input_format_6():
	date_format = "Jan 12"
	assert( horoscope(date_format) == "Capricorn")

def test_date_input_format_7():
	date_format = "january 12"
	assert( horoscope(date_format) == "Capricorn")

def test_date_input_format_8():
	date_format = "12 January 63"
	assert( horoscope(date_format) == "Capricorn")

# Test for graceful failure
def test_friendly_input_error_response():
	not_a_date = "nonsense"
	assert( horoscope(not_a_date) == "Please enter a date to learn its horoscope.")

def test_friendly_input_error_response2():
	not_a_date = "February 30"
	assert( horoscope(not_a_date) == "Please enter a date to learn its horoscope.")

def test_empty_input():
	empty_string = ""
	assert( horoscope(empty_string) == "Please enter a date to learn its horoscope.")