#############################################################
# FILE: ex3.py
# WRITER: Eran Nussinovitch a.k.a ednussi
# EXERCISE : intro2cs ex3 2013-2014
# Description:
# Containing 6 diffrent function of calculating retirement pension.
# Each one is fitted for a specific calculation5 differnet functions which
#############################################################

#  Implement the following function according the description in ex3

############################# Assignment 1 ####################################

# A function which returns a list of values a retirement fund you have
# invested in. Ment to use for the most basic calculation assuming you have a
# fixed salary, save %, growth rates per year, for a specific amount of years
# which are taken as arguments

def constant_pension(salary, save, growth_rate, years):
    
    # checking the inputs
    if (salary<0) or save<0 or save>100 or (
        growth_rate < -100) or (years < 0):
        return None
    else:
        
        # creating the list of values
        saved_money_constant=[]
        for i in range(0,years):
            if i==0:
                saved_money_constant.append(salary*save*0.01)
            else:
                saved_money_constant.append(
                    salary*save*0.01+saved_money_constant[i-1]*(
                        1+growth_rate*0.01))
        print(saved_money_constant)
        return saved_money_constant
    return None



    """ calculate retirement fund assuming constant pesnion

    A function that calculates the value of a retirement fund in each year
    based on the worker salary, savings, working years and assuming constant
    growthRate of the fund

    Args:
    - salary: the amount of money you earn each year,
           a non negative float.
    - save: the percent of your salary to save in the investment account
            each working year -  a non negative float between 0 and 100
    - growth_rate: the annual percent increase/decrease in your investment
           account, a float larger than or equal to -100 (minus 100)
    - years: number of years to work - non negative int

    return: a list whose values are the size of your retirement account at
      the end of each year.

    In case of bad input: values are out of range
    returns None

    You can assume that the types of the input arguments are correct. """

############################# Assignment 2 ####################################

# A function which returns in a list the values of the retirement fund
# you have invessted in. Ment to use for basic calculation assuming you
# have a fixed salary and save %, with a changing growths rates over the years
# entering them as arguments

def variable_pension(salary, save, growth_rates):
    
    # checking the inputs
    for j in range(0,len(growth_rates)):
        if growth_rates[j] < -100:
            return None
    if salary<0 or save<0 or save>100:
        return None
    else:
        
        # creating the list of values with changing growth rates
        saved_money_variable=[]
        for j in range(0,len(growth_rates)):
            if j==0:
                saved_money_variable.append(salary*save*0.01)
            else:
                saved_money_variable.append(salary*save*0.01+(
                    saved_money_variable[j-1])*(1+growth_rates[j]*0.01))
        return(saved_money_variable)

    """ calculate retirement fund assuming variable_pension

    A function that calculates the value of a retirement fund in each year
    based on the worker salary, savings,  and a list of growthRates values.
    Number of working years is as the length of growthRats

    Args:
    - salary: the amount of money you earn each year, a non negative float.
    - save: the percent of your salary to save in the investment account
    each working year -  a non negative float between 0 and 100
    - growth_rates: a list of annual growth percentages in your investment
    account - a list of floats larger than or equal to -100. The length of 
    the list defines the number of years you plan to work.

    return: a list whose values are the size of your retirement account at
    the end of each year.

    In case of bad input: values are out of range
    returns None

    You can assume that the types of the input arguments are correct. """

############################# Assignment 3 ####################################

# A function which calculates from a list of funds and changing growth rates
# which is the best and return you a list of the name and valuse in last year
# of the fund which was best. takes into consideration your salary, save %,
# and the funds file as arguments

def choose_best_fund(salary,save,funds_file):
    
    # checking the inputs
    if salary<0 or save<0 or save>100:
        return None
    else:
        last_year_worth=[]
        highest_value=0
        with open(funds_file,'r') as funds:
            
            # creating a list from the fun_file to work with
            for line in funds:
                print(line)
                fund_list = line.strip("\n").strip("#").split(",")
                print(fund_list)

                # creating a list of growths rates per fund
                growths_per_year=[]
                for i in range(1,len(fund_list)):
                    growths_per_year.append(float(fund_list[i]))
                    
                # calculate the worth of a fund
                worth_of_fund=variable_pension(
                    salary,save,growths_per_year)

                # takes highest value and name of fund into new list
                if worth_of_fund[-1]>highest_value:
                    highest_value=worth_of_fund[-1]
                    highest_name=fund_list[0]
                best_fund=(highest_name,highest_value)
        return best_fund
    return None
                        
    
    """find the best fund to invest in

    A function that calculates the best fund to invest money in from a list
    of funds in a file.

    Args:
    - salary: the amount of money you earn each year, a non negative float.
    - save: the percent of your salary to save in the investment account
    each working year -  a non negative float between 0 and 100
    - funds_file: A string -a path to a file that lists the different funds
    that you may choose to invest in
    format of the file:
    nameOfFund0,annoalGrowthYear0, annoalGrowthYear1, annoalGrowthYear2 …
    nameOfFund1,annoalGrowthYear0, annoalGrowthYear1, annoalGrowthYear2 …
    nameOfFund2,annoalGrowthYear0, annoalGrowthYear1, annoalGrowthYear2 …


    return: a tuple, where its first value is the name of the best fund to
    invest in assuming such an annual deposition, and the seocnd value in the
    tuple is the value of the pension fund in its end assuming we choose the
    best fund.

    In case of bad input: values are out of range
    returns None

    Note that for this specific exercise you may assume a correct form
    of the file. If an error accourd (File not exist, wrong type inside
    the file - Let python print its error and exit (Will happen
    automatically)

    You may also assume that the lists of growthRates have the same length
    and that the types of the inputs arguments are correct. """
    
############################# Assignment 4 ####################################

# 4.1
# A simple function which takes as arguments the growths rates of a fund
# and the specific year you want to know what would be the value in the
# given year, and returns just that.

def growth_in_year(growth_rates,year):
    
    # checking inputs
    for h in range(0,len(growth_rates)):
        if growth_rates[h] < -100:
            return None
    if year < 0 or year > len(growth_rates)-1:
        return None
    else:
        
        # calculate the value of the given year
        value_of_growth=float(growth_rates[year])
        return value_of_growth
    return None
  
    """return the growth value in a given year

    Args:
    - growth_rates: a list of annual growth percentages in your investment
    account - a list of floats larger than or equal to -100.
    -year: the index in the list we are intersted in
    a int between 0 and the size of growthRates

    return: a float with the value of growthRates in the specified year or
    None in case of a year not in the list

    You can assume that the types of the input arguments are correct."""

# 4.2  
# A function which takes as arguments a list of growth rates and inflation
# factors and returns to you the growth rates after the inflation
# has influecned it.

def inflation_growth_rates(growth_rates,inflation_factors):
    
    # checking the inputs
    if(growth_rates == False):
        return None
    elif (inflation_factors==False):
        return (growth_rates)
    else:
        for h in range(0,len(growth_rates)):
            if growth_rates[h] < -100:
                return None
        for h in range(0,len(inflation_factors)):
            if inflation_factors[h] <= -100:
                return None
            
        # creating the new list of growths rates after inflation
        inflated_list=[]
        for f in range(0,len(growth_rates)):
            if f>len(inflation_factors)-1:
                inflated_list.append(growth_rates[f])
            else:
                inflated_list.append(100*((
                    100+growth_rates[f])/(100+inflation_factors[f])-1))
        print(inflated_list)
        return inflated_list
    return None




    """ Calculate the adjusted growth list given inflation


    A function that return a new list with a adjusted growth rates due to
    the inflation. inflation should be adjusted for all years there is both
    inflation factor and growth factor.
    inflation is defined as 100*((100+g)/(100+i)-1)
    where g is growth in that year and i is the inflation.

    Args:
    - growth_rates: a list of annual growth percentages in your investment
    account - a list of floats larger than or equal to -100. 
    -inflation_factors: the annual inflation in percents.
    a list of floats larger than (BUT NOT EQUAL) to -100 .
    The list may have different size from growth_rates.

    returns a NEW list with the same length as growth_rates but during the
    inflation years the rates are adjusted.
    In case of bad input: values are out of range returns None

    You can assume that the types of the input arguments are correct."""
    

############################# Assignment 5 ####################################

# A function which takes in as arguments your savings, growth rates of
# your fund and expenses per year and returns after calculation
# a list of the fund values each year

def post_retirement(savings, growth_rates, expenses):
    # checks the inputs
    if savings < 0 or expenses < 0 or growth_rates == False:
        return None
    else:
        for h in range(0,len(growth_rates)):
            if growth_rates[h] < -100:
                return None
            
        # creating the new list after expenses and growth rate per year
        # are considerd
        after_spending=[]
        for i in range(0,len(growth_rates)):
            if i==0:
                after_spending=[savings*(
                    1+growth_rates[i]*0.01)-expenses]
            else:
                after_spending.append(
                    after_spending[i-1]*(1+growth_rates[i]*0.01)-expenses)
        print(after_spending)
        return after_spending
    return None


    """ calculates the account status after retirement

    A function that calculates the account status after retirement, assuming
    constant expenses and no income
    Args:
    -savings: the initial amount of money in your savings account.
    A float larger than 0
    - growth_rates: a list of annual growth percentages in your investment
    account - a list of floats larger than or equal to -100.
    -expenses: the amount of money you plan to spend each year during
    retirement. A non negative float

    return: a list of your retirement account value at the end of each year.

    Note in case of a negative balance - the growth rate will change into
    rate on the debt
    In case of bad input: values are out of range returns None

    You can assume that the types of the input arguments are correct."""
    


