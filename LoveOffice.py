# I have always been considered as a love doctor by those around me.
# I have decided to make an environment or office that can provide the services of a love doctor.
# It is a fun way to resolve the love-related concerns of clients.

# random module will be used for calculations involving random integers
import random 
# Defining variables with the user inputs; for later
lovecalc = 'Love Calculator' 
lovebank = 'Love Bank'

# The program will first ask for the user's name
person = input("Enter your name: ")
print('---------------------------------------------------')
# It will then print a welcome message with a menu
print('Welcome to the Love Doctor Office,', person + '!') 
# There is a function for every service including the Main Menu, Love Calculator and Love Bank
def MainMenu() :
    choice = 'not lovecalc or lovebank'
    # While loop will prompt the user to enter a service until they do so correctly 
    while choice != lovecalc or lovebank : 
        # The user can choose either the Love Calculator or Love Bank service
        print('-------------------------------------------') 
        print('Love Calculator | Love Bank')
        print('-------------------------------------------')
        # forward has to be global to be accessed outside of the MainMenu() function
        global forward
        # the program will ask the user to choose a service
        forward = input('Please choose a service: ')
        # The inputs 'Love Calculator' or 'Love Bank will be verified with the previously defined variables
        # If 'Love Calculator' is entered, it will exit the while loop and the function
        if forward == lovecalc :
            break 
        # If 'Love Bank' is entered, it will exit the while loop and the function
        elif forward == lovebank :
            break
        # If something else is entered, it will continue to prompt the user to enter a service
        else :
            print("Please choose an available service (services are case sensitive)")
            continue
MainMenu()

# If 'Love Calculator' was entered 
if forward == lovecalc :
    # Love Calculator Function
    def LoveCalculator() :
        # It will print a welcome message
        # It will also ask how many people they want to calculate their success with
        print('\nWelcome to the Love Calculator!')
        num_soulmates = int(input('\nEnter the number of potential soulmates: '))
        # for loop for each calculation
        # i has to start from 0 due to the next line which adds 1 to i
        for i in range(0, num_soulmates) : 
            # (i + 1) is counting/numbering each calculation made
            soulmate = input("\nname of potential soulmate " + str(i + 1) + ': ')
            # make a random calculation based on the lengths of the names and a random integer
            score = (len(soulmate) * len(person)) + random.randint(0, 100)
            # it will show the user each calculation
            print('\nYou have a ' + str(score) + '%' + ' chance of success with ' + soulmate)
            # will print a follow up message depending on their score
            if score >= 100 :
                print("You were both made for each other!")
            elif score < 100 and score >= 80 :
                print("You have a pretty good chance!")
            elif score < 80 and score >= 60 :
                print("Not a bad chance!")
            elif score < 60 and score >= 40 :
                print("It might work out...")
            elif score < 40 and score >= 10 :
                print("You might want to rethink this one...")
            elif score < 10 :
                print("There are many other fish in the sea...")
        # after the service is over, the program prints a thank you message
        print("\nThank you for using the Love Calculator!")
    LoveCalculator()

# if the "Love Bank" service is entered
if forward == lovebank :
    # Love Bank function
    def LoveBank() : 
        # prints a welcome message
        print("\nWelcome to your personal Love Bank Account where you can manage and track your expenses spent on love!")
        print('--------------------------------------------------------------------------------------------------------')
        # There is another menu specific to the bank including Withdrawal & Deposit and Budget Tracker
        print('Withdrawal & Deposit | Budget Tracker')
        # Because this is a bank, a net balance is shown
        balance = 0.00 
        print('\nNet Available Balance: ', balance)
        
        # Defining variables for the possible inputs from the user
        withdrawaldep = 'Withdrawal & Deposit'
        budtrack = 'Budget Tracker'
        choice = 'not Withdrawal & Deposit or Budget Tracker'
        # A while loop to prompt the user to enter a service until they do so correctly
        while choice != withdrawaldep or budtrack :
            # The program will ask the user to enter a service specific to the bank
            forward2 = input("\nPlease choose a service: ")
            # If the user enters 'Withdrawal & Deposit' the program will break out of the loop
            if forward2 == withdrawaldep :
                break
            # If the user enters 'Budget Tracker' the program will break out of the loop
            elif forward2 == budtrack :
                break
            # If the user enters something else, the program will continue to prompt for a service
            else :
                print("Please choose an available service (services are case sensitive)") 
                continue
        
        # If 'Withdrawal & Deposit' is entered
        if forward2 == withdrawaldep :
            # A welcome message is shown
            print('\nWelcome to the Withdrawal & Deposit Machine!')
            print('\nEnter 0 if you do not wish to withdraw or deposit anything')
            # Asks the user for how much they would like to deposit
            deposit = float(input('Enter the deposit amount: '))
            # Add the deposit to their net balance
            balance += deposit
            # Asks the user for how much they would like to withdraw
            withdraw = float(input('Enter the withdrawal amount: '))
            # Remove the withdrawal amount from their balance
            balance -= withdraw
            # Will print the deposit, withdrawal and current balance amounts
            print('\nDeposit amount: ', deposit, '\nWithdrawal amount: ', withdraw, '\nNet Available Balance: ', balance)
        
        # if 'Budget Tracker' is entered
        elif forward2 == budtrack :
            # Budget Tracker Function
            # This function creates a list of the expenses spent on love and finds the total amount spent
            def BudgetTracker() :
                # a welcome message is shown
                print('\nTrack your expenses spent on love here!')
                # Defne the dictionary to store the list
                BudDict = {}
                # The total sum of all the expenses
                sum = 0 
                # While loop to continuously prompt the user to enter their items
                while True : 
                    # asks the user to enter an item and its cost
                    KeyValue = input("Enter an item and its cost e.g. wine 60 ('quit' to quit): ") 
                    # If the user enters 'quit' the program will break out of the loop
                    if KeyValue == 'quit' : 
                        break
                    # If the input is in the incorrect format it will continue and ask for correct entries 
                    if KeyValue.count(' ') != 1 :
                        print('please enter in the format: item cost')
                        continue
                    # for each entry :
                    # split the string where the space is in each input
                    key, value = KeyValue.split()
                    # Add the entries into the dictionary  
                    BudDict.update({key: '$' + value})  
                    # BudDict[key] = value   # this also works
                    
                    # Calculating the total cost
                    if value.isdigit() :
                        sum += int(value)
                # Once the user types 'quit' or breaks out of the loop
                # The dictionary will be printed    
                print(BudDict)
                # The total of expenses will also be printed
                print('You have spent ' + '$' + str(sum) + ' on love')
            BudgetTracker()         
    LoveBank()
