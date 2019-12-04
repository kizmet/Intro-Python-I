"""
The Python standard library's 'calendar' module allows you to
render a calendar to your terminal.
https://docs.python.org/3.6/library/calendar.html

Write a program that accepts user input of the form
  `14_cal.py month [year]`
and does the following:
 - If the user doesn't specify any input, your program should
   print the calendar for the current month. The 'datetime'
   module may be helpful for this.
 - If the user specifies one argument, assume they passed in a
   month and render the calendar for that month of the current year.
 - If the user specifies two arguments, assume they passed in
   both the month and the year. Render the calendar for that
   month and year.
 - Otherwise, print a usage statement to the terminal indicating
   the format that your program expects arguments to be given.
   Then exit the program.
"""

import sys
import calendar
from datetime import datetime

args = sys.argv
today = datetime.today()
thismonth = today.month
thisyear = today.year


def getcal(*args):
    print(len(args))
    if len(args) > 1:
        m = args[1][:3]
        m = list(calendar.month_abbr).index(m)
        if len(args) > 2:
            y = int(args[2])
        else:
            y = thisyear
    else:
        m = thismonth
        y = thisyear

    cal = calendar.TextCalendar(calendar.SUNDAY)
    str = cal.formatmonth(y, m)
    print(str)


getcal(*args)
