import utils as u


t1 = u._time(24, 00)
a = 1
str = "A"

dict = {str: a}
a = 2
str = "B"
dict[str] = a
str = "C"
a = 10
dict[str] = a
print(dict)
