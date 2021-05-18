from random import randrange
from datetime import datetime, time, timedelta
import sys


class _date:
    def __init__(self, *args):
        """
        yyyy,mm,dd / str: yyyy-mm-dd / datetimeobj
        """
        if len(args) == 3:
            self.day = args[2]
            self.month = args[1]
            self.year = args[0]
        elif len(args) == 0:
            self.day = 1
            self.month = 1
            self.year = 2010
        elif type(args[0]) == str:
            self.day = int(args[0][-2:])
            self.month = int(args[0][-5:-3])
            self.year = int(args[0][:-6])
        elif type(args[0]) == datetime:
            self.day = args[0].day
            self.month = args[0].month
            self.year = args[0].year
        else:
            print("Invalid Arguments")
            sys.exit(1)

    def __str__(self):
        return "{:04d}-{:02d}-{:02d}".format(self.year, self.month, self.day)

    def __add__(self, days):
        temp = datetime(self.year, self.month, self.day)+timedelta(days=days)
        return _date(temp)

    def __sub__(self, days):
        temp = self.toDatetime()-timedelta(days=days)
        return _date(temp)

    def toDatetime(self):
        return datetime(self.year, self.month, self.day)


class _time:
    def __init__(self, *args):
        """
        hh,mm/hh:mm/ timeDeltaObj
        """
        if len(args) == 2:
            self.hour = args[0]
            self.minute = args[1]
        elif len(args) == 0:
            self.hour = 0
            self.minute = 0
        elif len(args) == 1:
            if type(args[0]) == str:
                self.hour = int(args[0][:-3])
                self.minute = int(args[0][-2:])
            elif type(args[0]) == timedelta:
                self.hour = args[0].days*24 + args[0].seconds // 3600
                self.minute = (args[0].seconds % 3600)/60
            elif type(args[0]) == datetime:
                self.hour = args[0].hour
                self.minute = args[0].minute
            else:
                print(type(args[0]))
                print(args[0])
                print("Invalid Arg Type")
                sys.exit()
        else:
            print(type(args[0]))
            print(args[0])
            print("Invalid Nr.Arguments")
            sys.exit()

    def __str__(self):
        return "{:02d}:{:02d}".format(self.hour, self.minute)

    def __add__(self, other):
        t1 = timedelta(hours=self.hour, minutes=self.minute)
        t2 = timedelta(hours=other.hour, minutes=other.minute)
        t3 = t1 + t2
        return _time(t3.seconds // (3600)+t3.days*24, (t3.seconds % 3600)//60)

    def __sub__(self, other):
        t1 = timedelta(hours=self.hour, minutes=self.minute)
        t2 = timedelta(hours=other.hour, minutes=other.minute)
        t3 = t1.seconds - t2.seconds + (t1.days-t2.days)*86400
        return _time(t3 // (3600), (t3 % 3600)//60)

    def __eq__(self, other):
        if self.hour == other.hour and self.minute == other.minute:
            return True
        return False

    def _toStr(self):
        return "{:02d}:{:02d}".format(self.hour, self.minute)

    def toTimeDel(self):
        return timedelta(hours=self.hour, minutes=self.minute)

    def toMin(self):
        return self.hour*60+self.minute


def generate_time(starting_time=_time()):
    if starting_time.hour == 23:
        hh = 23
    else:
        hh = randrange(starting_time.hour, 23)
    if hh == starting_time.hour and hh != 23:
        if starting_time.minute == 58 or starting_time.minute == 59:
            hh += 1
            mm = randrange(59)
        else:
            mm = randrange(starting_time.minute+1, 59)
    elif hh != starting_time.hour:
        mm = randrange(59)
    else:
        if starting_time.minute < 55:
            mm = randrange(starting_time.minute, 59)
        else:
            mm = 59
    return _time(hh, mm)


def generate_a_time_invertal(starting_time=_time()):
    starting = generate_time(starting_time)
    ending = generate_time(starting)
    return {"start": str(starting), "end": str(ending)}


# Test Unit
if __name__ == "__main__":
    # print(generate_a_time_invertal())
    print(generate_a_time_invertal(_time(8, 1)))

    pass
