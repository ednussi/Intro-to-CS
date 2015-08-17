#############################################################
# FILE: NonRecursiveMystery.py
# WRITER: Eran Nussinovitch a.k.a ednussi
# EXERCISE : intro2cs ex5 2013-2014
# Description:
# This Functioon reutrns for a positive number the
# sum of all the number's smaller dividers
#############################################################

SUM_DIVDERS_INITIAL_VALUE = 0

#############################################################

# the unrecursified funtion which returns the sum of all it's dividers
def mystery_computation(number):
    original_num = number
    sum_dividers = SUM_DIVDERS_INITIAL_VALUE
    for num in range(1, number):
        if original_num % (num) == 0:
            sum_dividers += num
    return sum_dividers
