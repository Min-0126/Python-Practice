# Global variables can be used within function
# Local variables that defined in the function can't be used outside of function

def spam():
    # set variable 'eggs' as global variable
    global eggs
    eggs = 'spam'

eggs = 'global'
spam()
print(eggs)     #print spam