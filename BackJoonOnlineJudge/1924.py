import calendar
month,date = map(int,input().split())
day = ['MON','TUE','WED','THU','FRI','SAT','SUN']
print(day[calendar.weekday(2007,month,date)])
