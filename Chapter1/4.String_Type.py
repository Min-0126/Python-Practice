a = "Jongmin"
b = "Kim"
c = "Min"

name = a + " " + b

print(a+b)

"Give space between Family and Given Name"
print(name)

print(name*3)

'd is number but its type is string type'
d = "100"
print(type(d))

'add " between the string'
e ='Life "is too short. You need Python'
print(e)
f ="I\'m hungry"
print(f)


'Multistring'
print("="*50)
print("Project")
print("="*50)

'Length of the String'
print(len(e))

'Index of Stirng -> Start from 0 -> 4th alphabet will be printed'
print(e[3])

'a[ x : y : z ] -> x is lowest, y is the highest, z is space'
z = e[19:]
print("Print after 20 alphabet", end=" ")
print(z)
 
y = e[:20]
print("Print first 19 alphabet", end = " ")
print(y)

x = e[::-1]
"Print from backward"
print(x)
"Print from backward and every second letter"
w = e[::-2]
print(w)
