"""Create a program that asks a user for their birthdate ( YYYY_MM_DD ) and
calculates their exact age in years, months, and days."""

from datetime import datetime, date

birthday = input("Enter you birthday [YYYY-MM-DD]: ")
birth_date = datetime.strptime(birthday, "%Y-%m-%d").date()

today = date.today()

year = today.year - birth_date.year
month = today.month - birth_date.month
day = today.day - birth_date.day

if day < 0:
    month -= 1

    prev_month = today.month - 1 if today.month > 1 else 12
    prev_year = today.year if today.month > 1 else today.year - 1
    days_in_prev_month = (date(today.year, today.month, 1) -
                          date(prev_year, prev_month, 1)).days
    day += days_in_prev_month

if month < 0:
    year -= 1
    month += 12

print(f"You are {year} years, {month} months, {day} days old")
