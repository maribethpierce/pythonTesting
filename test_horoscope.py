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
	start = datetime.strptime("22 12 2000", "%d %m %Y")
	end = datetime.strptime("19 01 2001", "%d %m %Y")
	interum_date = fake.date_between(start, end)
	assert( horoscope(interum_date) == "Capricorn")

def test_aquarius():
	start = datetime.strptime("20 01", "%d %m")
	end = datetime.strptime("18 02", "%d %m")
	interum_date = fake.date_between(start, end)
	assert( horoscope(interum_date) == "Aquarius")

def test_pisces():
	start = datetime.strptime("19 02", "%d %m")
	end = datetime.strptime("20 03", "%d %m")
	interum_date = fake.date_between(start, end)
	assert( horoscope(interum_date) == "Pisces")

def test_aries():
	start = datetime.strptime("21 03", "%d %m")
	end = datetime.strptime("19 04", "%d %m")
	interum_date = fake.date_between(start, end)
	assert( horoscope(interum_date) == "Aries")

def test_taurus():
	start = datetime.strptime("20 04", "%d %m")
	end = datetime.strptime("20 05", "%d %m")
	interum_date = fake.date_between(start, end)
	assert( horoscope(interum_date) == "Taurus")

def test_gemini():
	start = datetime.strptime("21 05", "%d %m")
	end = datetime.strptime("20 06", "%d %m")
	interum_date = fake.date_between(start, end)
	assert( horoscope(interum_date) == "Gemini")

def test_cancer():
	start = datetime.strptime("21 06", "%d %m")
	end = datetime.strptime("22 07", "%d %m")
	interum_date = fake.date_between(start, end)
	assert( horoscope(interum_date) == "Cancer")

def test_leo():
	start = datetime.strptime("23 07", "%d %m")
	end = datetime.strptime("22 08", "%d %m")
	interum_date = fake.date_between(start, end)
	assert( horoscope(interum_date) == "Leo")

def test_virgo():
	start = datetime.strptime("23 08", "%d %m")
	end = datetime.strptime("22 09", "%d %m")
	interum_date = fake.date_between(start, end)
	assert( horoscope(interum_date) == "Virgo")

def test_libra():
	start = datetime.strptime("23 09", "%d %m")
	end = datetime.strptime("22 10", "%d %m")
	interum_date = fake.date_between(start, end)
	assert( horoscope(interum_date) == "Libra")

def test_scorpio():
	start = datetime.strptime("23 10", "%d %m")
	end = datetime.strptime("21 11", "%d %m")
	interum_date = fake.date_between(start, end)
	assert( horoscope(interum_date) == "Scorpio")

def test_sagittarius():
	start = datetime.strptime("22 11", "%d %m")
	end = datetime.strptime("21 12", "%d %m")
	interum_date = fake.date_between(start, end)
	assert( horoscope(interum_date) == "Sagittarius")

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