"%10s means there are 10 spaces"
"hi will at the last spaces"
a = "%10s" % "hi"
print(a)

"%-10s gives 10 spaces, but hi will be at the first space"
"jane will be after 10 spaces"
b = "%-10sjane." % "hi"
print (b)

"Decimal will be printed as 3.4213"
c = "%0.4f" % 3.42134234
print(c)

"will be total 10 spaces and then 3.4213 will fill the last"
d= "%10.4f" % 3.42134234
print(d)