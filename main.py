import os
import openai
import datetime

from dateutil.parser import parse
from dotenv import load_dotenv

load_dotenv()
openai.api_key = os.getenv("OPENAI_API_KEY")

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

name = input("Enter your name: ")
birthday = input("Enter your birthday (DD/MM/YYYY): ")
birthday = parse(birthday, dayfirst=True)
zoidiac_sign = get_zodiac_sign(birthday)
current_date = datetime.datetime.now()

response = openai.ChatCompletion.create(
    model="gpt-3.5-turbo",
    messages=[
        {"role": "system", "content": "You are an astrologer. The date is " + current_date.strftime("%d/%m/%Y") + "." + " The user's name is " + name + "."},
        {"role": "user", "content": "What is my horoscope for today, I'm a " + zoidiac_sign + "Born on " + birthday.strftime("%d/%m/%Y") + "."},
    ],
    max_tokens=150
)

print(response.choices[0].message.content)