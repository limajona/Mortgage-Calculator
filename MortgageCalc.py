########################################################################################################################
#   Computer Project #3
#
#   initialize variables
#   loop while stop running program
#       welcome text and main prompt printed
#       input string for location, square footage, max monthly payment, down payment, APR
#       throughout the program data will be run differently according to inputs
#       All following cases include calculations, print data for user, print monthly schedule table
#
#       CASE 1: only square footage is given
#       CASE 2: both square footage and max monthly payment are given
#       CASE 3: square footage isn't given but max monthly payment is
#       CASE 4: neither square footage nor max monthly payment are given
#       CASE 5: only condition is max monthly payment not being given
#       CASE 6: accounts for any other combination of data given
#
#       prompt user to make another attempt
########################################################################################################################

#initializing variables
NUMBER_OF_PAYMENTS = 360  # 30-year fixed rate mortgage, 30 years * 12 monthly payments
SEATTLE_PROPERTY_TAX_RATE = 0.0092  # Tax rate for properties in Seattle
SAN_FRANCISCO_PROPERTY_TAX_RATE = 0.0074  # Tax rate for properties in San Francisco
AUSTIN_PROPERTY_TAX_RATE = 0.0181  # Tax rate for properties in Austin
EAST_LANSING_PROPERTY_TAX_RATE = 0.0162  # Tax rate for properties in East Lansing
AVERAGE_NATIONAL_PROPERTY_TAX_RATE = 0.011  # Average tax rate for properties in the U.S.
SEATTLE_PRICE_PER_SQ_FOOT = 499.0  # Price per square foot in Seattle
SAN_FRANCISCO_PRICE_PER_SQ_FOOT = 1000.0  # Price per square foot in San Francisco
AUSTIN_PRICE_PER_SQ_FOOT = 349.0  # Price per square foot in Austin
EAST_LANSING_PRICE_PER_SQ_FOOT = 170.0  # Price per square foot in East Lansing
AVERAGE_NATIONAL_PRICE_PER_SQ_FOOT = 244.0  # Average price per square foot in the U.S.
APR_2023 = 0.0668  # Average annual percentage rate in the U.S.
KEEP_GOING_TEXT = "".lower()  # empty sting to initialize the while loop below

#program will keep running until KEEP_GOING_TEXT is not equal to "N" or "n"
while KEEP_GOING_TEXT != "n".lower():
    WELCOME_TEXT = print('''\nMORTGAGE PLANNING CALCULATOR\n============================ ''')
    MAIN_PROMPT = print('''\nEnter a value for each of the following items or type 'NA' if unknown ''')

    LOCATIONS_TEXT = input('''\nWhere is the house you are considering '''\
    '''(Seattle, San Francisco, Austin, East Lansing)? ''')

#the next 5 if clauses are to make the use of the right numbers according to the desired location.
    if LOCATIONS_TEXT == "Seattle":
        LOCATION_PER_SQFT = SEATTLE_PRICE_PER_SQ_FOOT
        LOCATION_TAX = SEATTLE_PROPERTY_TAX_RATE

    elif LOCATIONS_TEXT == "San Francisco":
        LOCATION_PER_SQFT = SAN_FRANCISCO_PRICE_PER_SQ_FOOT
        LOCATION_TAX = SAN_FRANCISCO_PROPERTY_TAX_RATE

    elif LOCATIONS_TEXT == "Austin":
        LOCATION_PER_SQFT = AUSTIN_PRICE_PER_SQ_FOOT
        LOCATION_TAX = AUSTIN_PROPERTY_TAX_RATE

    elif LOCATIONS_TEXT == "East Lansing":
        LOCATION_PER_SQFT = EAST_LANSING_PRICE_PER_SQ_FOOT
        LOCATION_TAX = EAST_LANSING_PROPERTY_TAX_RATE

    else:
        LOCATION_PER_SQFT = AVERAGE_NATIONAL_PRICE_PER_SQ_FOOT
        LOCATION_TAX = AVERAGE_NATIONAL_PROPERTY_TAX_RATE

    SQUARE_FOOTAGE_TEXT = input('''\nWhat is the maximum square footage you are considering? ''').lower()
    if SQUARE_FOOTAGE_TEXT == "na":
        SQUARE_FOOTAGE_FLOAT = 0 #if not given assume to be zero
    else:
        SQUARE_FOOTAGE_FLOAT =float(SQUARE_FOOTAGE_TEXT)

    MAX_MONTHLY_PAYMENT_TEXT = input('''\nWhat is the maximum monthly payment you can afford? ''').lower()
    if MAX_MONTHLY_PAYMENT_TEXT =="na":
        MAX_MONTHLY_PAYMENT_FLOAT = 0 #if not given assume to be zero

    else:
        MAX_MONTHLY_PAYMENT_FLOAT = float(MAX_MONTHLY_PAYMENT_TEXT)

    DOWN_PAYMENT_TEXT = input('''\nHow much money can you put down as a down payment? ''').lower()
    if DOWN_PAYMENT_TEXT == "na":
        DOWN_PAYMENT_FLOAT = 0 #if not gien assume to be zero

    else:
        DOWN_PAYMENT_FLOAT = float(DOWN_PAYMENT_TEXT)

    APR_TEXT = input('''\nWhat is the current annual percentage rate? ''').lower()
    if APR_TEXT == "na":
        APR_2023 = 0.0668 #if APR not given then use national average number
        INTEREST_RATE = APR_2023/12 #since APR is annual then divided by 12 is monthly
        APR_FLOAT = APR_2023*100 #when being displayed in strings we still want it as a percentage so times 100
    else:
        APR_FLOAT = float(APR_TEXT)
        INTEREST_RATE = APR_FLOAT/1200
        #convert from annual to month so divided by 12, then percentage to number so divide by 100

#If only square footage is given by user this block of code will be executed
    if MAX_MONTHLY_PAYMENT_TEXT =="na" and DOWN_PAYMENT_TEXT == "na" and APR_TEXT == "na":
        HOME_COST = SQUARE_FOOTAGE_FLOAT * LOCATION_PER_SQFT #find home cost
        PRINCIPAL_AMOUNT = HOME_COST - DOWN_PAYMENT_FLOAT #find principal amount
        PROPERTY_TAX = HOME_COST*LOCATION_TAX #find property tax for the year
        MONTHLY_TAX = PROPERTY_TAX/12 #find tax per month
        MONTH_PAY = ((PRINCIPAL_AMOUNT*(INTEREST_RATE*(1+INTEREST_RATE)**NUMBER_OF_PAYMENTS))/(
                (1+INTEREST_RATE)**NUMBER_OF_PAYMENTS-1)) #find mortgage month pay

        TOTAL_PAY = MONTHLY_TAX + MONTH_PAY #find the total amount due in the month

        sq_ft_int = round(SQUARE_FOOTAGE_FLOAT) # transform value into an integer
        home_cost_int = round(HOME_COST) # transform value into an integer
        d_payment_int = round(DOWN_PAYMENT_FLOAT) # transform value into an integer

#will consider average national values if the conditions are met
        if LOCATIONS_TEXT != "Seattle" and LOCATIONS_TEXT != "San Francisco" and LOCATIONS_TEXT !="Austin"\
                and LOCATIONS_TEXT!= "East Lansing":

            LOCATIONS_TEXT = "the average U.S. housing market"
            print("\nUnknown location. Using national averages for price per square foot and tax rate.")

        print('\n\nIn {0}, an average {1:,} sq. foot house would cost ${2:,}.'.format(
            LOCATIONS_TEXT, sq_ft_int,home_cost_int))

        print('A 30-year fixed rate mortgage with a down payment of ${0:,} at {1:.1f}% APR results'.format(
            d_payment_int,APR_FLOAT))

        print('\tin an expected monthly payment of ${0:,.2f} (taxes) + ${1:,.2f} (mortgage payment) = ${2:,.2f}'.format(
            MONTHLY_TAX,MONTH_PAY,TOTAL_PAY))

        AMORTIZATION_TEXT = input('''\nWould you like to print the monthly payment schedule (Y or N)? ''').lower()
        if AMORTIZATION_TEXT == "y":
            Month = 1 #amount of months
            Interest = PRINCIPAL_AMOUNT * INTEREST_RATE #calculates interest per month
            Payment = MONTH_PAY - Interest #calculates payment per month
            Balance = PRINCIPAL_AMOUNT #calculates the total balance

#print header of the table and the separator between it and the actual data
            print('\n{0:^7}|{1:^12}|{2:^13}|{3:^14}'.format('Month', 'Interest', 'Payment', 'Balance'))
            separator = '=' #separate header from data
            print(separator * 48)

#loop will iterate 360 times to create a amortization table
            for numbers in range(NUMBER_OF_PAYMENTS):
                print('{0:^7.0f}| ${1:>9,.2f} | ${2:>10,.2f} | ${3:>11,.2f}'.format(Month, Interest, Payment, Balance))

                Balance -= Payment
                Interest = Balance * INTEREST_RATE
                Payment = MONTH_PAY - Interest
                Month += 1

#if both square footage and max montlhy payment are given this block will be executed
    elif DOWN_PAYMENT_FLOAT == 0 and APR_FLOAT ==6.68:
        HOME_COST = SQUARE_FOOTAGE_FLOAT * LOCATION_PER_SQFT
        PRINCIPAL_AMOUNT = HOME_COST - DOWN_PAYMENT_FLOAT
        PROPERTY_TAX = HOME_COST * LOCATION_TAX
        MONTHLY_TAX = PROPERTY_TAX / 12
        MONTH_PAY = ((PRINCIPAL_AMOUNT * (INTEREST_RATE * (1 + INTEREST_RATE) ** NUMBER_OF_PAYMENTS)) /(
                (1 + INTEREST_RATE) ** NUMBER_OF_PAYMENTS - 1))

        TOTAL_PAY = MONTHLY_TAX + MONTH_PAY

        sq_ft_int = round(SQUARE_FOOTAGE_FLOAT)
        home_cost_int = round(HOME_COST)
        d_payment_int = round(DOWN_PAYMENT_FLOAT)

        if LOCATIONS_TEXT != "Seattle" and LOCATIONS_TEXT != "San Francisco" and LOCATIONS_TEXT !="Austin"\
                and LOCATIONS_TEXT!="East Lansing":

            LOCATIONS_TEXT = "the average U.S. housing market"
            print("\nUnknown location. Using national averages for price per square foot and tax rate.")

        print('\n\nIn {0}, an average {1:,} sq. foot house would cost ${2:,}.'.format(
            LOCATIONS_TEXT, sq_ft_int,home_cost_int))

        print('A 30-year fixed rate mortgage with a down payment of ${0:,} at {1:.1f}% APR results'.format(
            d_payment_int,APR_FLOAT))

        print('\tin an expected monthly payment of ${0:,.2f} (taxes) + ${1:,.2f} (mortgage payment) = ${2:,.2f}'.format(
            MONTHLY_TAX, MONTH_PAY, TOTAL_PAY))

#will display either you can or cannot afford the desired house based on your max monthly payment and home cost.
        if TOTAL_PAY > MAX_MONTHLY_PAYMENT_FLOAT:
            print('Based on your maximum monthly payment of ${0:,.2f} you cannot afford this house.'.format(
                MAX_MONTHLY_PAYMENT_FLOAT))

        else:
            print('Based on your maximum monthly payment of ${0:,.2f} you can afford this house.'.format(
                MAX_MONTHLY_PAYMENT_FLOAT))

            AMORTIZATION_TEXT = input('''\nWould you like to print the monthly payment schedule (Y or N)? ''').lower()
            if AMORTIZATION_TEXT == "y":
                Month = 1
                Interest = PRINCIPAL_AMOUNT * INTEREST_RATE
                Payment = MONTH_PAY - Interest
                Balance = PRINCIPAL_AMOUNT
                print('\n{0:^7}|{1:^12}|{2:^13}|{3:^14}'.format('Month', 'Interest', 'Payment', 'Balance'))
                separator = '='
                print(separator * 48)

                for numbers in range(NUMBER_OF_PAYMENTS):
                    print('{0:^7.0f}| ${1:>9,.2f} | ${2:>10,.2f} | ${3:>11,.2f}'.format(
                        Month, Interest, Payment,Balance))

                    Balance -= Payment
                    Interest = Balance * INTEREST_RATE
                    Payment = MONTH_PAY - Interest
                    Month += 1

#if square footage is given but max monthly payment isn't then this block of code will run
    elif SQUARE_FOOTAGE_TEXT =="na" and MAX_MONTHLY_PAYMENT_TEXT!="na":

#first we assume the square footage to be any value, in this case 900 sq ft
        SQUARE_FT = 900
        HOME_COST = SQUARE_FT * LOCATION_PER_SQFT
        PRINCIPAL_AMOUNT = HOME_COST - DOWN_PAYMENT_FLOAT
        PROPERTY_TAX = HOME_COST * LOCATION_TAX
        MONTHLY_TAX = PROPERTY_TAX / 12
        MONTH_PAY = ((PRINCIPAL_AMOUNT * (INTEREST_RATE * (1 + INTEREST_RATE) ** NUMBER_OF_PAYMENTS)) / (
                (1 + INTEREST_RATE) ** NUMBER_OF_PAYMENTS - 1))

        TOTAL_PAY = MONTHLY_TAX + MONTH_PAY

#loop will estimate the maximum square footage that the user's max monthly payment can afford
        while SQUARE_FT :
            if TOTAL_PAY > MAX_MONTHLY_PAYMENT_FLOAT:
                SQUARE_FT -=1
                break
            else:
                SQUARE_FT +=1

            HOME_COST = SQUARE_FT * LOCATION_PER_SQFT
            PRINCIPAL_AMOUNT = HOME_COST - DOWN_PAYMENT_FLOAT
            PROPERTY_TAX = HOME_COST * LOCATION_TAX
            MONTHLY_TAX = PROPERTY_TAX / 12
            MONTH_PAY = ((PRINCIPAL_AMOUNT * (INTEREST_RATE * (1 + INTEREST_RATE) ** NUMBER_OF_PAYMENTS)) / (
                    (1 + INTEREST_RATE) ** NUMBER_OF_PAYMENTS - 1))

            TOTAL_PAY = MONTHLY_TAX + MONTH_PAY

        HOME_COST = SQUARE_FT*LOCATION_PER_SQFT #will recalculate the home cost with the new square footage
        sq_ft_int = round(SQUARE_FT)
        home_cost_int = round(HOME_COST)
        d_payment_int = round(DOWN_PAYMENT_FLOAT)

        if LOCATIONS_TEXT != "Seattle" and LOCATIONS_TEXT != "San Francisco" and LOCATIONS_TEXT !="Austin"\
                and LOCATIONS_TEXT!="East Lansing":

            LOCATIONS_TEXT = "the average U.S. housing market"
            print("\nUnknown location. Using national averages for price per square foot and tax rate.")

        print('\n\nIn {0}, a maximum monthly payment of ${1:,.2f} allows the purchase of a house of {2:,}' \
              'sq. feet for ${3:,}'.format(LOCATIONS_TEXT, MAX_MONTHLY_PAYMENT_FLOAT, sq_ft_int, home_cost_int))

        print('\t assuming a 30-year fixed rate mortgage with a ${0:,} down payment at {1:.1f}% APR.'.format(
            d_payment_int, APR_FLOAT))

#if neither square footage nor max monthly payment are given than calculations cannot be made.
    elif SQUARE_FOOTAGE_TEXT=="na" and MAX_MONTHLY_PAYMENT_TEXT =="na":
        print("\nYou must either supply a desired square footage or a maximum monthly payment. Please try again.")

#if only max monthly payment is given then this block of code will be executed
    elif MAX_MONTHLY_PAYMENT_TEXT =="na":
        HOME_COST = SQUARE_FOOTAGE_FLOAT * LOCATION_PER_SQFT
        PRINCIPAL_AMOUNT = HOME_COST - DOWN_PAYMENT_FLOAT
        PROPERTY_TAX = HOME_COST * LOCATION_TAX
        MONTHLY_TAX = PROPERTY_TAX / 12
        MONTH_PAY = ((PRINCIPAL_AMOUNT * (INTEREST_RATE * (1 + INTEREST_RATE) ** NUMBER_OF_PAYMENTS)) / (
                (1 + INTEREST_RATE) ** NUMBER_OF_PAYMENTS - 1))

        TOTAL_PAY = MONTHLY_TAX + MONTH_PAY

        sq_ft_int = round(SQUARE_FOOTAGE_FLOAT)
        home_cost_int = round(HOME_COST)
        d_payment_int = round(DOWN_PAYMENT_FLOAT)

        if LOCATIONS_TEXT != "Seattle" and LOCATIONS_TEXT != "San Francisco" and LOCATIONS_TEXT !="Austin"\
                and LOCATIONS_TEXT!="East Lansing":

            LOCATIONS_TEXT = "the average U.S. housing market"
            print("\nUnknown location. Using national averages for price per square foot and tax rate.")

        print('\n\nIn {0}, an average {1:,} sq. foot house would cost ${2:,}.'.format(
            LOCATIONS_TEXT, sq_ft_int,home_cost_int))

        print('A 30-year fixed rate mortgage with a down payment of ${0:,} at {1:.1f}% APR results'.format(
            d_payment_int,APR_FLOAT))

        print('\tin an expected monthly payment of ${0:,.2f} (taxes) + ${1:,.2f} (mortgage payment) = ${2:,.2f}'.format(
            MONTHLY_TAX, MONTH_PAY, TOTAL_PAY))

        AMORTIZATION_TEXT = input('''\nWould you like to print the monthly payment schedule (Y or N)? ''').lower()
        if AMORTIZATION_TEXT == "y":
            Month = 1
            Interest = PRINCIPAL_AMOUNT * INTEREST_RATE
            Payment = MONTH_PAY - Interest
            Balance = PRINCIPAL_AMOUNT
            print('\n{0:^7}|{1:^12}|{2:^13}|{3:^14}'.format('Month', 'Interest', 'Payment', 'Balance'))
            separator = '='
            print(separator * 48)
            for numbers in range(NUMBER_OF_PAYMENTS):
                print('{0:^7.0f}| ${1:>9,.2f} | ${2:>10,.2f} | ${3:>11,.2f}'.format(Month, Interest, Payment, Balance))

                Balance -= Payment
                Interest = Balance * INTEREST_RATE
                Payment = MONTH_PAY - Interest
                Month += 1

#this block will account for any other combination of inputs given by the user
    else:
        HOME_COST = SQUARE_FOOTAGE_FLOAT * LOCATION_PER_SQFT
        PRINCIPAL_AMOUNT = HOME_COST - DOWN_PAYMENT_FLOAT
        PROPERTY_TAX = HOME_COST * LOCATION_TAX
        MONTHLY_TAX = PROPERTY_TAX / 12
        MONTH_PAY = ((PRINCIPAL_AMOUNT * (INTEREST_RATE * (1 + INTEREST_RATE) ** NUMBER_OF_PAYMENTS)) / (
                (1 + INTEREST_RATE) ** NUMBER_OF_PAYMENTS - 1))

        TOTAL_PAY = MONTHLY_TAX + MONTH_PAY

        sq_ft_int = round(SQUARE_FOOTAGE_FLOAT)
        home_cost_int = round(HOME_COST)
        d_payment_int = round(DOWN_PAYMENT_FLOAT)

        if LOCATIONS_TEXT != "Seattle" and LOCATIONS_TEXT != "San Francisco" and LOCATIONS_TEXT !="Austin"\
                and LOCATIONS_TEXT!= "East Lansing":

            LOCATIONS_TEXT = "the average U.S. housing market"
            print("\nUnknown location. Using national averages for price per square foot and tax rate.")

        print('\n\nIn {0}, an average {1:,} sq. foot house would cost ${2:,}.'.format(
            LOCATIONS_TEXT, sq_ft_int,home_cost_int))

        print('A 30-year fixed rate mortgage with a down payment of ${0:,} at {1:.1f}% APR results'.format(
            d_payment_int,APR_FLOAT))

        print('\tin an expected monthly payment of ${0:,.2f} (taxes) + ${1:,.2f} (mortgage payment) = ${2:,.2f}'.format(
            MONTHLY_TAX, MONTH_PAY, TOTAL_PAY))

        if TOTAL_PAY > MAX_MONTHLY_PAYMENT_FLOAT:
            print('Based on your maximum monthly payment of ${0:,.2f} you cannot afford this house.'.format(
                MAX_MONTHLY_PAYMENT_FLOAT))

        else:
            print('Based on your maximum monthly payment of ${0:,.2f} you can afford this house.'.format(
                MAX_MONTHLY_PAYMENT_FLOAT))

        AMORTIZATION_TEXT = input('''\nWould you like to print the monthly payment schedule (Y or N)? ''').lower()
        if AMORTIZATION_TEXT == "y":
            Month = 1
            Interest = PRINCIPAL_AMOUNT * INTEREST_RATE
            Payment = MONTH_PAY - Interest
            Balance = PRINCIPAL_AMOUNT
            print('\n{0:^7}|{1:^12}|{2:^13}|{3:^14}'.format('Month', 'Interest', 'Payment', 'Balance'))
            separator = '='
            print(separator * 48)
            for numbers in range(NUMBER_OF_PAYMENTS):
                print('{0:^7.0f}| ${1:>9,.2f} | ${2:>10,.2f} | ${3:>11,.2f}'.format(Month, Interest, Payment,Balance))

                Balance -= Payment
                Interest = Balance * INTEREST_RATE
                Payment = MONTH_PAY - Interest
                Month += 1

#prompts user to try again
    KEEP_GOING_TEXT = input("\nWould you like to make another attempt (Y or N)? ").lower()
