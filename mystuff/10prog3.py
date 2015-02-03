# A program to compare dates
import datetime

def dateAfter(d1, d2):
	da1 = datetime.datetime.strptime(d1, "%d.%m.%Y").date()
	da2 = datetime.datetime.strptime(d2, "%d.%m.%Y").date()
	if da1>da2:
		return True
	else:
		return False










first = "29.09.2001"
second = "13.03.2003"
print dateAfter(first, second)
