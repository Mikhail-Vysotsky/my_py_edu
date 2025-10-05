import calendar
import datetime

cal = calendar.TextCalendar().formatyear(2025)
print(cal)

m, d, y = map(int, input().split())
idx = datetime.date(y, m, d).weekday()

print(calendar.day_name[idx].upper())