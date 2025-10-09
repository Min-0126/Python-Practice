# indent variable keep track of how many spaces of indentation occur before the band of eigth asterisks
# indentIncreasing variable contains a Boolean value to determine whether the amount of indentation is increasing or decreasing
import time, sys

#How many spaces to indent
indent = 0
indentIncreasing = True # Whether the indentation is increasing or not

# Ctrl + C raises the keyboardInterrupt exception
# ' ' * indent    --->   number of spaces in front of *
try:
    while True:
        print(' ' * indent, end = ' ')
        print('********')
        time.sleep(0.1) # Pause for 1/10th of a second

        if indentIncreasing:
            #Increase the number of spaces:
            indent = indent + 1

            if indent == 20:
                #Change direction:
                indentIncreasing = False
        else:
            #Decrease the number of spaces
            indent = indent - 1
            if indent == 0:
                #Change direction
                indentIncreasing = True
except KeyboardInterrupt:
    sys.exit()