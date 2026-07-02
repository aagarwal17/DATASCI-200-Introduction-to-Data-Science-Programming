""" Script to manage contacts """
import contact
import pickle

# GLOBALS for menu choices
LOOK_UP = 1
ADD = 2
CHANGE = 3
DELETE = 4
QUIT = 5

# Global constant for the file name
FILENAME = "contacts.dat"

# main function
def main():
    """ main function that locats the contact dictionary
    and assigns the data to mycontacts """
    
    mycontacts = load_contacts()
    
    # init the choice var
    choice = 0
    
    # process menu selections 'til quit. 
    while choice != QUIT:
        choice = get_menu_choice()
        
        if choice == LOOK_UP:
            look_up(mycontacts)
        elif choice == ADD:
            add(mycontacts)
        elif choice == CHANGE:
            change(mycontacts)
        elif choice == DELETE:
            delete(mycontacts)
            
    # save the data to a file.
    save_contacts(mycontacts)

def load_contacts():
    try:
        input_file = open(FILENAME, 'rb')
        
        # unpickle the data
        contact_dct = pickle.load(input_file)
        
        # close the phone_inven tory.dat file
        input_file.close()
    except IOError:
        # cannot open the file so create empty dicttionary
        contact_dct = {}
    
    # return the dict.
    return contact_dct

def get_menu_choice():
    print("\n----- Menu -----")
    print("1. Look up a contact")
    print("2. Add a NEW contact")
    print("3. Change existing contact")
    print("4. Delete a contact")
    print("5. Quit the program\n")

    choice = int(input("What's your poison, partner? "))
    
    #validate the choice
    while choice < LOOK_UP or choice > QUIT:
        choice = int(input("Enter a valid option, cowboy: "))
        
    return choice

def look_up(mycontacts):
    # get a name to look up
    name = input("Enter a name: ")
    print(mycontacts.get(name, 'That name was not found.'))

def add(mycontacts):
    # get the contact info...
    name = input("Name: ")
    phone = input("Phone: ")
    email = input("Email: ")
    
    # create a Contact object named entry
    entry = contact.Contact(name, phone, email)
    
    # if the name doesn't exist, add it was the key with
    # the entry object as the associated value
    if name not in mycontacts:
        mycontacts[name] = entry
        print("The entry has been added.")
    else:
        print("Sorry, that person is already in the cornfield.")
        
def change(mycontacts):
    # get the name to edit
    name = input("Enter the pardner: ")
    
    if name in mycontacts:
        phone = input("Enter the new phone #: ")
        email = input("Enter the new email:   ")
        entry = contact.Contracts(name, phone, email)
        
        # update
        mycontacts[name] = entry
        print("The data have been updated.")
    else:
        print("Sorry, not found. :( ")

def delete(mycontacts):
    name = input("Who you wanna rubout? ")
    if name in mycontacts:
        del mycontacts[name]
        print("Problem solved (if you know what I mean)")
    else:
        print("Sorry, he got away!")
        
def save_contacts(mycontacts):
    output_file = open(FILENAME, "wb")
    # pickle the data
    pickle.dump(mycontacts, output_file)
    
    output_file.close()
    
""" START HERE """
if __name__ == "__main__":
    main()