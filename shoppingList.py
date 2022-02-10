# Your Name, Date, List Exercise combination : - Lists
# To Do - User Interface for a shopping list creation platform
# Implement the functionality in the if/elif statements

#create the list that items will be added to
shoppingList = []

print("Welcome to the Deele College Shopping List experience")

finished = False

while finished != True:
    # Create the Interface
    print ("**************************************************")
    print ("*                                                *")
    print ("*\t 1. Add Item to the Shopping List        *")
    print ("*                                                *")
    print ("*\t 2. Remove Item from the Shopping List   *")
    print ("*                                                *")
    print ("*\t 3. View the Shopping List               *")
    print ("*                                                *")
    print ("*\t 4. Save Shopping List                   *")
    print ("*                                                *")
    print ("*\t 5. Load a Shopping List                 *")
    print ("*                                                *")
    print ("*\t 6. Exit the System                      *")
    print ("*                                                *")
    print ("**************************************************")
    
    usrInput = input("Please enter your choice 1 - 6  :-   ")
    #print (type(int(usrInput)))
    
    #Lets Validate the input, ie make sure its a number and nothing else
    while not usrInput.isdigit(): # check if it is a valid digit, ie number...
        usrInput = input("ERROR Please enter your choice 1 - 6  :-   ")
        
    usrInput= int(usrInput)
    #cater for numbers less than 1 and greater than 6
   
    if usrInput ==6:
        print("Goodbye")
        finished = True
        
    elif usrInput == 1:
        print("We will add an item to the List")
    elif usrInput == 2:
        print("We will remove an item from the List")
    elif usrInput == 3:
        print("We will view the List")
    elif usrInput == 4:
        print("We will save the shopping list")
    elif usrInput == 5:
        print("We will load a previously saved List")
    else:
        print("THE NUMBER YOU ENTERD IS EITHER TOO BIG OR TOO SMALL>>> PLEASE PUT ON YOUR GLASSES")
