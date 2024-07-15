import datetime
n = "1 1"
d = int(n[0])
m = int(n[1])

def get_day_of_week(year, month, day):

    date = datetime.date(year, month, day)
    day_of_week = date.weekday()
    days = ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday"]
    return days[day_of_week]

print(get_day_of_week(2009, m, d))