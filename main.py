"""
A program that uses openai api to give astrology readings from the command line

Takes in a birthday and converts it to a zodiac sign

Uses the zodiac sign and the current date to get a horoscope from the openai api
"""

import datetime
from dateutil.parser import parse

def get_zodiac_sign(birthday):
    zodiac_sign = ""
    month = birthday.month
    day = birthday.day

    if month == 12:
        zodiac_sign = "Sagittarius" if (day < 22) else "Capricorn"
    elif month == 1:
        zodiac_sign = "Capricorn" if (day < 20) else "Aquarius"
    elif month == 2:
        zodiac_sign = "Aquarius" if (day < 19) else "Pisces"
    elif month == 3:
        zodiac_sign = "Pisces" if (day < 21) else "Aries"
    elif month == 4:
        zodiac_sign = "Aries" if (day < 20) else "Taurus"
    elif month == 5:
        zodiac_sign = "Taurus" if (day < 21) else "Gemini"
    elif month == 6:
        zodiac_sign = "Gemini" if (day < 21) else "Cancer"
    elif month == 7:
        zodiac_sign = "Cancer" if (day < 23) else "Leo"
    elif month == 8:
        zodiac_sign = "Leo" if (day < 23) else "Virgo"
    elif month == 9:
        zodiac_sign = "Virgo" if (day < 23) else "Libra"
    elif month == 10:
        zodiac_sign = "Libra" if (day < 23) else "Scorpio"
    elif month == 11:
        zodiac_sign = "Scorpio" if (day < 22) else "Sagittarius"
    
    return zodiac_sign

# get birthday (day/month/year)
birthday = input("Enter your birthday (DD/MM/YYYY): ")
birthday = parse(birthday, dayfirst=True)
print("You are a " + get_zodiac_sign(birthday) + ".")

