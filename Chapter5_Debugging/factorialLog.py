#Logging
# Easy to create a record of custom mussages that you write
# This moudel indicates when the program execution has reached the logging funciton call
# ALso, it list any variables at that point in time

# 5 stages for logging
# DEBUG
# INFO
# WARNING
# ERROR
# CRITICAL

# logging.disable() function disable logging entirely
# ex) logging.disable(logging.CRITICIAL)

import logging
# Display log messages on the screen as program runs.
# Specify what details you want to see and how you wnat those details displayed.
logging.basicConfig(level=logging.DEBUG, format = '%(asctime)s - %(levelname)s - %(message)s')
logging.debug('Start of Program')

def factorial(n):
    logging.debug('Start of factorial(' + str(n) + ')')
    total = 1
    for i in range(1, n + 1):
        total *= i
        logging.debug('i is ' + str(i) + ', total is ' + str(total))
    logging.debug('End of factorial(' + str(n) + ')')
    return total

print(factorial(5))
logging.debug('End of program')