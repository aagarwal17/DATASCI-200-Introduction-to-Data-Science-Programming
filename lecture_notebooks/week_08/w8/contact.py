""" The Contact Class holds basic info """

class Contact:
    # the __init__ method initializes the attributes.
    def __init__(self, name, phone, email):
        self.__name = name
        self.__phone = phone
        self.__email = email
        
    # set_name method to set the name attribute
    def set_name(self, name):
        self.__name = name
        
    # and similar for the other data
    def set_phone(self, phone):
        self.__phone = phone
    
    def set_email(self, email):
        self.__email = email

    # get_name method to set the name attribute
    def get_name(self):
        return self.__name

    def get_phone(self):
        return self.__phone
    
    def get_email(self):
        return self.__email

    """ the __str__ method returns the object's state 
    as a string for humans to read """
    def __str__(self):
        return "Name: " + self.__name + \
                "\nPhone: " + self.__phone + \
                "\nEmail: " + self.__email

