'%d is decimal, 3 will be go into d'
a = "I eat %d apples." % 3
print(a)

'%s is string, five will be go into s'
b = "I eat %s apples." % "five"
print(b)

number = 6
c = "I eat %d apples." % number
print(c)

'More than two values'
number = 10
day = "three"
d = "I ate %d apples, so I was sick for %s days" % (number,day)
print(d)

'%c is one character'
'%f is floating-point'
'%s can be used in any situation.'