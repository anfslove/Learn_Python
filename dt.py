import datetime


def minutes(dt1, dt2):
    aa = dt2 - dt1
    print(aa)
    bb = datetime.timedelta.total_seconds(aa)
    print(int(bb/60))
    return aa

now = datetime.datetime.now()
dt1 = now.replace(minute=5)
dt2 = now.replace(minute=11)
minutes(dt1, dt2)