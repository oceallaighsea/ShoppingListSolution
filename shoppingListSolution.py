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
        
    elif usrInput == 1: # add item
        print("We will add an item to the List")
        temp = input("What would you like to add to the list ? ")
        shoppingList.append(temp)
        print("List now contains :", shoppingList)
    elif usrInput == 2:
        print("We will remove an item from the List")
        temp = input("What would you like to remove ? ")
        shoppingList.remove(temp)
        print("List now contains :", shoppingList)
    elif usrInput == 3:
        print("We will view the List")
    elif usrInput == 4:
        print("We will save the shopping list")
        f = open("shoppingList.txt", "a")
        # Save the shopping list in a csv format
        # take each item out of the list and put it into a string separated by ,'s
        tempString =""
        #get length of the shoppingList list
        lengthOL = len(shoppingList)
        for index in range(lengthOL):
            if index == lengthOL -1:
                tempString += shoppingList[index]
            else:
                tempString += shoppingList[index]+","
            #tempString += item
        f.write(tempString)
        f.close()
        
    elif usrInput == 5:
        print("We will load a previously saved List")
        f = open("shoppingList.txt", "r")

        #print(f.readline())
        fileContents = f.readline()
        print(fileContents)
        #fileContents is a string with the items in the shopping list
        #each item separated by a ,
        loadedList = fileContents.split(",")
        print(loadedList)
        shoppingList += loadedList
        print ("Both lists added together = ",shoppingList)
        
    else:
        print("THE NUMBER YOU ENTERD IS EITHER TOO BIG OR TOO SMALL>>> PLEASE PUT ON YOUR GLASSES")
