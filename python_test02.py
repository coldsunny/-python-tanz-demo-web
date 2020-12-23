#-*-coding:utf-8-*-
import sys
import math
#if条件判断
'''a=88
b=int(raw_input("\nPlease enter a number:"))
if b>a:
    print "The number too big!"
elif b<a:
    print "The number too small!"
else:
    print "Good! congratulation to you!"
'''

'''
if True:
    print "It's true"

print "I'm true" if True else "False"
'''

#for循环
a = ['cat','window','administrator']
for x in a:
    print x,len(x)
print type(a)

#range函数
a1 = xrange(10)
print a1,type(a1)

print range(5,10)
print range(0,10,3)

if True:
    pass

print math.cos(math.pi / 4.0)

#序列-list&tuple
s1 = (5,2.1,'hello',True)
print s1,type(s1)
s2 = [3,False,'world']
print s2,type(s2)