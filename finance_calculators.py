import math

print("investment - to calculate the amount of interest you'll earn on your investment")
print("bond - to calculate the amount you'll have to pay on a home loan")
print( "\nEnter either 'investment' or 'bond' from the menu above to proceed:") 

choice = input("Plese enter your choice: ")
choice = choice.lower()

# User has to select between two option: bond or investment
if choice == "investment":
    amount = int(input("How much money You would like to invest?"))
    rate = int(input("What's the interest rate?")) 
    invest_time = int(input("How many years you would like to invest?"))
    
    interest = input("Would you like to check math for 'Simple' or 'Compound' interest?")
    interest = interest.lower()
 
    # if user selected investment option, than should choose between intrest type: simple or compound
    if interest == "simple":
        #simple intrest calculation
        total_simple = amount* (1+ rate/100 * invest_time)
        print("You'll get",total_simple)
    elif interest == "compound":
        #compound intrest calculation
        total_compound = amount*math.pow((1+rate/100), invest_time)
        print("You'll get",total_compound)
    else:
        print("Please choose between 'simple' or 'compound' intrest type!")   
        
#if user will chose bond:    
elif choice == "bond":
    property_value= int(input("What's the value of the property?"))
    loan_intrest=  int(input("What's the intrest for this loan?"))
    pay_back_time= int(input("How many months you would like to take for repayment?"))
 
    repayment= (loan_intrest/100/12 * property_value) / (1-(1+loan_intrest/100/12) ** (-pay_back_time))
    
    print("Every month you will have to pay", repayment)
    
else:
    print("Please chose between these two option!")    