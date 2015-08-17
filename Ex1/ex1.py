#######################################################
# FILE: ex1.py
# WRITER: Eran, ednussi, 302186408
# EXERCISE: intro2cs ex1 2013-2014
# DESCRIPITION:
# A simple program that runs Einstein riddle
########################################################

# printing of the welcoming statment
print ("Welcome to the Einstein puzzle")

#print text which asks for a 3 digit numer
num1_str=(input("Please enter a three digit number:"))

# turning the string into an int
num1_int=int(num1_str)
a=num1_int
# callin each number from the 3 digit number
# by a name - h=hundereds, t=tens, o=ones

h=a//100

t=((a%100)//10)

o=((a%100)%10)

#reverse the number r-reversed
r=o*100+t*10+h

#printing the 2 statments and the diffrence
print("For the number:", a, "the reverse number is:", r)
print("The difference between", a, "and", r, "is", abs(a-r))

#creating the reverse diffrence, - d-diffrence y-reversed differnce
# q/w/e same as h/t/o in the upper findings
d=abs(a-r)

q=d//100

w=((d%100)//10)

e=((d%100)%10)

#reversing the diffrrence
y=e*100+w*10+q

#printing the last 2 statements and amazing your friend!!
print("The reverse difference is:", y)
print("The sum of:", d, "and", y, "is:", abs(d+y))
