# ------------------------------------------------------------------------ #
# Title: Assignment 08
# Description: Working with classes

# ChangeLog (Who,When,What):
# RRoot,1.1.2030,Created started script
# RRoot,1.1.2030,Added pseudo-code to start assignment 8
# JMurphy,11.26.2019,Modified code to start assignment 8
# JMurphy,11.27.2019,Modified code to complete assignment 8
# JMurphy,11.28.2019,Modified code to complete assignment 8
# JMurphy,11.29.2019,Modified code and completed assignment 8
# ------------------------------------------------------------------------ #

# Data -------------------------------------------------------------------- #
strFileName = 'products.txt'
lstOfProductObjects = []


class Product:
    """Stores data about a product:
    properties:
        product_name: (string) with the products's  name
        product_price: (float) with the products's standard price
    methods:
    changelog: (When,Who,What)
        RRoot,1.1.2030,Created Class
        JMurphy,11.29.2019,Modified code to complete assignment 8
    """

    def __init__(self, product_name: str, product_price: float):
        """Sets the user inputted name and price of product(s)"""
        try:
            self.p_name = str(product_name)
            self.p_price = float(product_price)
        except Exception as e:
            raise Exception("Error setting initial values: \n" + str(e))

    # Properties--------------------------------------------------------------- #
    @property
    def product_name(self):
        return str(self.p_name)

    @product_name.setter
    def product_name(self, value: str):
        if str(value).isnumeric():
            self.p_name = value
        else:
            print("Please enter a valid name for your product")

    @property
    def product_price(self):
        return float(self.p_price)

    @product_price.setter
    def product_price(self, value: float):
        if str(value).isnumeric():
            self.p_price = float(value)
        else:
            print("Prices must be numeric!")

# Methods ------------------------------------------------------------------#
    def convert_str(self):
        return self.__str__()

    def __str__(self):
        return self.product_name + ',' + str(self.product_price)


# Data -------------------------------------------------------------------- #

# Processing  ------------------------------------------------------------- #
class FileProcessor:
    """Processes data to and from a file and a list of product objects:
    methods:
    save_data_to_file(file_name, list_of_product_objects):
    read_data_from_file(file_name): -> (a list of product objects)
    changelog: (When,Who,What)
    RRoot,1.1.2030,Created Class
    JMurphy,11.26.2019,Modified code to complete assignment 8
    JMurphy,11.29.2019,Modified code to complete assignment 8
    """

    @staticmethod
    def read_data_from_file(file_name: str):
        """Shows the user the current items within products.txt
        :param: file_name: string
        :return: a list of products in rows
        """
        list_of_rows = []
        file = open(strFileName, 'r')
        for line in file:
            data = line.split(",")
            row = Product(data[0], data[1])
            list_of_rows.append(row)
        file.close()
        return list_of_rows

    # TODO: Add Code to process data to a file

    @staticmethod
    def save_data_to_file(file_name: str, list_of_product_objects: list):
        """Write data to a file from a list
        :param file_name: (string) file name
        :param list_of_product_objects: (list) of products
        """
        file = open(file_name, "w")
        for product in list_of_product_objects:
            file.write(product.__str__() + "\n")
        file.close()

    # ------- Processing  ------------------------------------------------------------- #

    # Presentation (Input/Output)  -------------------------------------------- #


class inputOutput:
    """ A class for performing Input and Output
    methods:
    mainMenu(): displays user menu
    inputMenuChoice(): captures the users choice within mainMenu()
    print_current_lst(list_of_rows): prints a list (list_of_rows)
    add_obj_lst(): captures the users inputs before being transferred to a list
    """

    @staticmethod
    def mainMenu():
        print('''
        ****** Product and Price Program ******
        
        Main Menu:
        1. Display current saved data
        2. Add new product and price
        3. Save new product and price to file
        4. Exit
        ''')

    @staticmethod
    def inputMenuChoice():
        """ Gets the menu  choice from a user
        :return: string
        """
        choice = str(input("  Please enter a valid selection [1 - 4]: ")).strip()
        print()
        return choice

    @staticmethod
    def print_current_lst(list_of_rows: list):
        """Prints the current list

        :param list_of_rows: (list) of rows to be displayed
        :return: list of rows
        """
        print("Current product and prices in list:")
        for row in list_of_rows:
            print(row.product_name + "(" + str(row.product_price) + ")")


    @staticmethod
    def add_obj_lst():
        """adds objects to the current list
        :param: __name: placeholder to save in name of product
        :param: __price: same as above but with price
        :return: product(inputted user data)
              """
        __name = str(input('Enter product name: ')).strip()
        __price = float(input('Enter product price (ex. 9.99): ').strip())
        print()
        newProd = Product(product_name=__name, product_price=__price)
        print(newProd, " " "Was added to your data!")
        return newProd


# Presentation (Input/Output)  -------------------------------------------- #

# Main Body of Script  ---------------------------------------------------- #
try:
    lstOfProductObjects = FileProcessor.read_data_from_file(strFileName)

    while True:
        inputOutput.mainMenu()
        strChoice = inputOutput.inputMenuChoice()
        if strChoice.strip() == '1':
            inputOutput.print_current_lst(lstOfProductObjects)
            continue
        elif strChoice.strip() == '2':
            lstOfProductObjects.append(inputOutput.add_obj_lst())
            continue
        elif strChoice.strip() == '3':
            FileProcessor.save_data_to_file(strFileName, lstOfProductObjects)
            input("Your data has been saved! Press any key to return to main menu....")
            continue
        elif strChoice.strip() == '4':
            input("Press any key to exit.....")
            break
except Exception as e:
    print("There was an error! Check file permissions.")
    print(e, e.__doc__, type(e), sep='\n')
# Main Body of Script  ---------------------------------------------------- #
