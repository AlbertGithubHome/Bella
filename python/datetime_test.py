# datetime test

from datetime import datetime

print(datetime.now())

dt = datetime(2000, 8, 8, 13, 45, 6)
print('dt =',dt)

time_stamp = dt.timestamp()
print('dt.timestamp =', time_stamp)

print('now.timestamp =', datetime.now().timestamp())

now_timestamp = datetime.now().timestamp();
print('now_timestamp =', now_timestamp)

print(datetime.fromtimestamp(now_timestamp))
print(datetime.utcfromtimestamp(now_timestamp))


# str and datetime
print()
print(datetime.strptime('2016-12-21 15:59:32', '%Y-%m-%d %H:%M:%S'))
print(datetime.now().strftime('%a, %b %d %H:%M:%S'))

from datetime import timedelta
print(datetime.now() + timedelta(hours = 1))
print(datetime.now() + timedelta(days = 1))

#set time zone
from datetime import timezone

tz_utc_8 = timezone(timedelta(hours=8))
print(datetime.now().replace(tzinfo =tz_utc_8))


#timezone change
print()
utc_dt = datetime.utcnow().replace(tzinfo=timezone.utc)
print(utc_dt)
bj_dt = utc_dt.astimezone(timezone(timedelta(hours = 8)))
print(bj_dt)
tokyo_dt = utc_dt.astimezone(timezone(timedelta(hours = 9)))
print(tokyo_dt)