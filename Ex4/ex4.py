#############################################################
# FILE: ex3.py
# WRITER: Eran Nussinovitch a.k.a ednussi
# EXERCISE : intro2cs ex4 2013-2014
# Description:
# Diffrent function for uses in diffrent situations in life
# esspicly in the retirement field about money and choosing house
# according to drffrent logics
#############################################################

MINIMUM_GROWTH_RATE = -100
MINIMUM_EPSILON = 0
MINIMUM_SALARY = 0
MINIMUM_SAVE = 0
MAX_SAVE = 100
MINIMUM_SAVINGS = 0
MINIMUM_BUDGET = 0
MINIMUM_EXPENSES = 0

############################# Assignment 1 ####################################

# a funcation from Exrcise 3:

# A function which returns in a list the values of the retirement fund
# you have invessted in. Ment to use for basic calculation assuming you
# have a fixed salary and save %, with a changing growths rates over the years
# entering them as arguments

def variable_pension(salary, save, growth_rates):
    
    # checking the inputs
    for rate in range(0,len(growth_rates)):
        if growth_rates[rate] < MINIMUM_GROWTH_RATE:
            return None
    if salary < MINIMUM_SALARY or save < MINIMUM_SAVE or save > MAX_SAVE:
        return None
    else:
        
        # creating the list of values with changing growth rates
        saved_money_variable=[]
        for rate in range(0,len(growth_rates)):
            if rate == 0:
                saved_money_variable.append(salary*save*0.01)
            else:
                saved_money_variable.append(salary*save*0.01+(
                    saved_money_variable[rate-1])*(1+growth_rates[rate]*0.01))
        return(saved_money_variable)

# A function which takes in fixed salary, save precentage, 2 list of
# changing frowth rates in your account before and after your retirement
# and epsilon - a minimum amount of money you want to keep after spending
# everything. and returns the maximum amount of money one can withdraw each
# year
def live_like_a_king(salary, save, pre_retire_growth_rates,
                  post_retire_growth_rates, epsilon):
    
    # checking the inputs
    if (salary < MINIMUM_SALARY or save < MINIMUM_SAVE or save > MAX_SAVE or 
        epsilon <= MINIMUM_EPSILON):
        return None
    if pre_retire_growth_rates==[]:
        return 0.0
    if post_retire_growth_rates==[]:
        return None
    else:
        
        # checking the inputs in the lists
        if (len(pre_retire_growth_rates) or len(post_retire_growth_rates))==1:
            if (pre_retire_growth_rates[0] or
                post_retire_growth_rates[0]) < MINIMUM_GROWTH_RATE:
                return None
        else:            
            for rate in range(0,len(pre_retire_growth_rates)):
                if pre_retire_growth_rates[rate] < MINIMUM_GROWTH_RATE:
                    return None
            for rate in range(0,len(post_retire_growth_rates)):
                if post_retire_growth_rates[rate] < MINIMUM_GROWTH_RATE:
                    return None
    
    # getting the retirement money start amount using the function from
    # last Exrecise
    savings_list = variable_pension(salary,save,pre_retire_growth_rates)    
    retirement_money = savings_list[len(savings_list)-1]

    # using aritmatic solution - 
    # using recurrence formula we can find an arthimtic solution
    # calculating the max amount of money and max amount of spending
    # possible and dividing the two would give out exactly the max amount
    # of money you can spend

    for rate in range(0,len(post_retire_growth_rates)):
        
        # in case living only 1 year
        if rate == 0:
            final_money = retirement_money*(1+post_retire_growth_rates[0]*0.01)
            overall_spendings = 1
            
        # in case of living more than 1 year
        else:
            final_money = final_money*(1+post_retire_growth_rates[rate]*0.01)
            overall_spendings = overall_spendings*(
                1+post_retire_growth_rates[rate]*0.01)+1
            
    # calculating the max amount of spending possible
    max_spending = final_money / overall_spendings
    return max_spending



   
""" Find the maximal expenses you may expend during your lifetime  

    A function that calculates what is the maximal annual expenses you may
    expend each year and not enter into debts
    You may Calculate it using binary search or using arithmetics
    Specify in your README in which method you've implemnted the function

    Args:  
    -salary: the amount of money you make each year-a non negative float.
    -save: the percent of your salary to save in the investment account
    each working year -  a non negative float between 0 and 100
    -pre_retire_growth_rates: a list of annual growth percentages in your
    investment account - a list of floats larger than or equal to -100.
    -post_retire_growth_rates: a list of annual growth percentages
    on investments while you are retired. a list of floats larger
    than or equal to -100. In case of empty list return None
    - epsilon: an upper bound on the money must remain in the account
    on the last year of retirement. A float larger than 0

    Returns the maximal expenses value you found (such that the amount of
    money left in your account will be positive but smaller than epsilon)

    In case of bad input: values are out of range returns None

    You can assume that the types of the input arguments are correct."""


############################# Assignment 2 ####################################

def bubble_sort_2nd_value(tuple_list):

    tuples_list = tuple_list.copy()
    # creating a run for the length of the list
    for i in range(0,len(tuples_list)):
        
        # for each run in the current place in the length
        # a run on all list componennts
        for j in range(0,len(tuples_list)-i-1):
            
            # moving to the end the highest value
            if(tuples_list[j][1] > tuples_list[j+1][1]):
                tuples_list[j], tuples_list[j+1] = (
                               tuples_list[j+1], tuples_list[j])
                
    # returnning the arranged list
    return tuples_list


    
    """sort a list of tuples using bubble sort algorithm

    Args:
    tuple_list - a list of tuples, where each tuple is composed of a string
    value and a float value - ('house_1',103.4)

    Return: a NEW list that is sorted by the 2nd value of the tuple,
    the numerical one. The sorting direction should be from the lowest to the
    largest. sort should be stable (if values are equal, use original order)

    You can assume that the input is correct."""


############################# Assignment 3 ####################################

# A function which helps to you to conclude according to your savings,
# a list of changing growth rates and a list of retirement houses
# which is the best one you can afford, and returns you that name

def choosing_retirement_home(savings,growth_rates,retirement_houses):
    
    # checking the inputs
    if savings < 0 or growth_rates == [] or retirement_houses == []:
        return None
    else:
        for rate in range(0,len(growth_rates)):
            if growth_rates[rate] < MINIMUM_GROWTH_RATE:
                return None    
                
    #sorting the list with the function we built
    retirement_houses = bubble_sort_2nd_value(retirement_houses)

    # using binary search in order to find the the name of the most
    # expensive house you can afford

    # creating values
    hi_house = len(retirement_houses)
    low_house = 0
    best_house_yet = None
    
    # binary search logic
    while low_house < hi_house:
        mid_house = (low_house+hi_house)//2
        mid_val = retirement_houses[mid_house][1]
        
        # using a funcation we build last exrecise
        # calculates the remainning money when u passes away
        def post_retirement(savings, growth_rates, expenses):
            
            # checks the inputs
            if (savings < MINIMUM_SAVINGS or expenses < MINIMUM_EXPENSES or
                growth_rates == False):
                return None
            else:
                for rate in range(0,len(growth_rates)):
                    if growth_rates[rate] < MINIMUM_GROWTH_RATE:
                        return None
                    
                # creating the new list after expenses and growth rate per year
                # are considerd
                after_spending=[]
                for rate in range(0,len(growth_rates)):
                    if rate == 0:
                        after_spending=[savings*(
                            1+growth_rates[rate]*0.01)-expenses]
                    else:
                        after_spending.append(
                            after_spending[rate-1]*(
                                1+growth_rates[rate]*0.01)-expenses)
                        
                # returns the new list
                return after_spending
            return None
        
        # the last compersion and binary search logic
        remainings = post_retirement(savings, growth_rates, mid_val)[-1]
        if remainings > 0:
            low_house = mid_house + 1
            best_house_yet = retirement_houses[mid_house][0]
        elif remainings < 0:
            hi_house = mid_house
        else:
            return retirement_houses[mid_house][0]
        
    # return the best house you can afford
    return best_house_yet  

      
"""Find the most expensive retirement house one can afford.

    Find the most expensive, but affordable, retiremnt house.
    Implemnt the function using binary search

    Args:
    -savings: the initial amount of money in your savings account.
    -growth_rates: a list of annual growth percentages in your
    investment account - a list of floats larger than or equal to -100.
    -retirement_houses: a list of tuples of retirement_houses, where
    the first value is a string - the name of the house and the
    second is the annual rent of it - nonnegative float.

    Return: a string - the name of the chosen retirement house
    Return None if can't afford any house.

    You need to test the legality of savings and growth_rates
    but you can assume legal retirement_house list 
    You can assume that the types of the input are correct"""

############################# Assignment 5 ####################################

# A function which calls back a function
# in use as the logic of re-arranging the list of houses by our
# desired new ideas of values of houses

def get_value_key(value=0):

    # the new function
    def new_house_val(triple):
        return (triple[1] + value*triple[2])
    
    return new_house_val
        

    """returns a function that calculates the new value of a house

    #Args:
    -value: the value added per opponent - a float - the default value is 0

    This function returns a function that accepts triple containing
    (house ,anntual rent,number of opponents) and returns the new value of
    this house - annual_rent+value*opponents

    You can assume that the input is correct."""
    

# A function which gives you your desired house according to
# a logic of values between all affordable houses from a list

def choose_retirement_home_opponents(budget,key,retirement_houses):
    
    # checks the inputs
    if budget < MINIMUM_BUDGET:
        return None
    else:
        for house in range(0, len(retirement_houses)):
            if (retirement_houses[house][1] < 0 or
                retirement_houses[house][2] < 0):
                return None
          
    # creating a list of houses values
    affordable_houses=[]
    for house in range(0,len(retirement_houses)):
        if budget-retirement_houses[house][1] >= 0:
            affordable_houses.append(retirement_houses[house])
    
    # sorting the list 
    affordable_houses =  sorted(affordable_houses , key=key)
    
    # returns the name of the best valued house out of the affordable houses
    if affordable_houses == []:
        return None
    else:
        return affordable_houses[-1][0]

""" Find the best retiremnt house that is affordable and fun

    A function that returns the best retiremnt house to live in such that:
    the house is affordable and
    his value (annual_rent+value*opponents) is the highest

    Args:
    -budget: positive float. The amount of money you can
    expand per year.
    -key: a function of the type returned by get_value_key
    -retirement_houses: a list of houses (tuples), where  the first value
    is a string - the name of the house,
    the second is the annual rent on it - a non negative float, and the third
    is the number of battleship opponents the home hosts - non negative int
    
    Returns the name of the retirement home which provides the best value and
    which is affordable.

    You need to test the legality of annual_budget,
    but you can assume legal retirement_house list 
    You can assume that the types of the input are correct"""

   

    
