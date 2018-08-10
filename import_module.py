#from turtle import *
#color('red', 'yellow')
#begin_fill()
#while True:
#    forward(200)
#    left(170)
#    if abs(pos()) < 1:
#        break
#end_fill()
#done()

#import math
#print(math.factorial(549))

#import calendar
#c = calendar.TextCalendar(calendar.SUNDAY)
#str = c.formatmonth(2018, 7)
#print(str)

from turtle import *
color('red', 'green')
begin_fill()
i = 0
while onclick():
    forward(30)
    left(10)
    if not onclick():
        end_fill()
        done()

#color('black', 'red')
#begin_fill()
#while True:
#    forward(10)
