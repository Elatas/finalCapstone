import math
# Variables assign for the initial messages when customer visits the page:

investment= print("INVESTMENT is to calculate the amount of interest you will earn on your investment")

bond=print("BOND is to calculate the amount you will have to pay on a home loan")

the_choice=input("Choose either 'investment' or 'bond' from the menu below to proceed: ")

# In case the answer is investment or bond we have several paths:

if the_choice.upper()=="INVESTMENT":
    the_amount=float(input("How much are you depositing?: "))
    the_interest=float(input("Enter the interest rate without the %: "))
    years=float(input("How many years are you investing for?: "))
    interest_type=input("Would you like simple or compound interest: ")

    # Now we have other two options here for different type of interest selected:
    if interest_type.upper()=="SIMPLE":
        total_investment=the_amount*(1+(the_interest/100)*years)
        print(total_investment)
    elif interest_type.upper()=="COMPOUND":
        total_investment=the_amount*math.pow((1+(the_interest/100)), years)
        print(total_investment)

# If Bond calculator was selected then the formula below will be functional:
elif the_choice.upper()=="BOND":
    house_value=float(input("What is the present value of the house?: "))
    the_interest=float(input("Enter the interest rate without the %: "))
    the_lenght=float(input("How many months are you planning to take to repay the bond?: "))
    total_bond = (((the_interest/12)/100)*house_value)/(1 - (1+((the_interest/12)/100))**(-the_lenght))
    print(total_bond)
