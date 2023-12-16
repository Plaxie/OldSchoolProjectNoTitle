# !IMPORTANT! BY : ADIL : XII-D:2110092 : YARA INTERNATIONAL SCHOOL : AUGUST 2022-23
#
#    THIS MODULE CONTAINS ALL THE FUNCTIONS RELATED TO Extras:

#    ALL THE FUNCTIONS HAVE BEEN MADE FROM SCRATCH WITH NO TYPE OF PLAGERIZING INVOLVED.
#    THIS INCLUDES THE PRINT STATEMENTS AND ALL THE LOGIC USED. HENCE THERE MUST BE NO COMPLAINS
#    IN REGARDS TO THIS MODULE'S CREATION. EXCEPT FOR THE IN-BUILT MODULES


# This module will have Extra Functions that are required to build other modules

from math import cos, sin;from os import system

PageWidth = 60; BorderCharacter = "X"

# Creating a list of all the functions available in the module.

FunctionsAvailable = ["IsInteger", "IsFloat", "digitCounter", 
                      "Calculator", "Calculate", "Factorial", 
                      "Euler_s_Number", "e", "cosec", "sec", 
                      "tan", "cot", "PrintPage", "InputToExitOrReturn",
                      "InputNextPage", "ListAllFunctions","EndModuleInterface",
                      "EXPOFFError", "StrReplaceByte", "ReadFileReplaceByte", "stringRepeater"]


# Used to convert to the numbers in the range 0-9.

NumbersInStrings = ["ZERO","ONE","TWO","THREE","FOUR","FIVE","SIX","SEVEN","EIGHT","NINE"]

PositionsInStrings = ["NULL","FIRST","SECOND","THIRD","FOURTH","FIFTH","SIXTH","SEVENTH","EIGTH","NINTH"]

PosInStrings = ["0TH","1ST","2ND","3RD","4TH","5TH","6TH","7TH","8TH","9TH"]

RomansInStrings = ["","I","II","III","IV","V","VI","VII","VIII","IX"]

AlphasInStrings = ["","A","B","C","D","E","F","G","H","I"]


# A dictionary that contains the names of the modules, and the page numbers of the modules.
ModuleDict = {"CURVES":[1,2],"ONEDGS":[2,2],"TWODGS":[3,3],"THREEDGS":[4,3],"GRAPHS":[5,2],"INTERFACE":[6,1],"EXTRAS":[7,1]}


def IsInteger(value):
    
    """
    If the value can be converted to an integer, return True, otherwise return False
    
    :param value: The value to be checked
    :return: True or False
    """
    
    try:
        value = int(value)
        return True
    except ValueError:
        return False
    
def IsFloat(value):
    
    """
    If the value can be converted to a float, return True, otherwise return False
    
    :param value: The value to be checked
    :return: True or False
    """
    
    try:
        value = float(value)
        return True
    except ValueError:
        return False

def digitCounter(x):
    
    """
    "While x is greater than or equal to 1, divide x by 10 and add 1 to Digits."
    
    The while loop is a very powerful tool. It allows you to repeat a block of code as long as a
    condition is true
    
    :param x: The number you want to count the digits of
    :return: The number of digits in the number.
    """
    
    Digits = 0
    while x >= 1:
        x /= 10
        Digits += 1
    return Digits

def Calculator():
    
    """
    It takes in a string, checks if it's an integer, if it is, it evaluates it and prints the result, if
    not, it prints an error message.
    """
    
    ExitConditon = 0
    while(ExitConditon != 1):
        UserInput = input("Start:  ")
        #Check if user has inputed in correct Format.
        if IsInteger(UserInput[0]):
            print("Result: "+ str(eval(UserInput)))
            ExitCondition = input("Do You Want to Continue?\nIf Yes, Press Enter. If No, Type \'1\':\n")
            if IsInteger(ExitCondition):
                ExitConditon = int(ExitCondition)
        else:
            print("Inputed Calculation is in wrong Format Please Try again!")
            ExitCondition = 0
        
    
def Calculate(Expression):
    
    """
    It takes a string as input, and returns the result of evaluating that string as a Python expression
    
    :param Expression: The expression to be calculated
    :return: The result of the expression.
    """
    
    return eval(Expression)

def Factorial(value):
    
    """
    The function takes a value and returns the factorial of that value
    
    :param value: The number you want to find the factorial of
    :return: The factorial of the value.
    """
    
    Answer = 1
    if value < 0:
        return "Negative Factorials Do not Exist!"
    elif value == 0:
        return 1
    else:
        for i in range(1,value+1):
            Answer *= i
    return Answer

def Euler_s_Number(x = 50): # A good Estimate
    
    """
    It takes the value of x, and then adds the value of 1/x! to the variable E, and then returns the
    value of E
    
    :param x: The number of terms to be used in the summation, defaults to 50 (optional)
    :return: The Euler's Number.
    """
    

    E = 0.0
    
    if x > 171: x = 171
    if x < 7: x = 7 # For a Correct generation of E.
    # Due to OverflowError:
    # Meaning the Factorials of 172 and beyond
    # are very large for python to handle at all.

    for i in range(x):
        E += 1.0/Factorial(i)
    return E

# TRIGONOMETRIC FUNCTIONS

def e():
    return Euler_s_Number()

def cosec(value):
    
    """
    It takes a value and returns the cosecant of that value
    
    :param value: The value to be passed to the function
    :return: the value of the cosine of the value.
    """
    
    return 1/sin(value)

def sec(value):
    
    """
    The function `sec` takes a value and returns the secant of that value
    
    :param value: The value to be converted
    :return: The secant of the value.
    """
    
    return 1/cos(value)

def tan(value):
    
    """
    The tan function returns the tangent of the given value.
    
    :param value: The value to calculate the tangent of
    :return: The value of the tangent of the input value.
    """
    
    return sin(value)/cos(value)

def cot(value):
    
    """
    The function cot(value) returns the cotangent of value
    
    :param value: The value to be converted to radians
    :return: the cosine of the value divided by the sine of the value.
    """
    
    return cos(value)/sin(value)

# INTERFACE RELATED FUNCTIONS

def PrintPage(FilePath):
    
    """
    It opens the file, reads the lines, prints the lines, and closes the file.
    
    :param FilePath: The path to the file you want to print
    """
    
    system("cls")
    with open(FilePath, 'r') as F:
        lines = F.readlines()
        for line in lines:
            print(line, end='')
        F.close()

def InputToExitOrReturn(main_page):
    
    """
    It takes a function as an argument and returns the function if the user types 'X' or exits the
    program if the user presses enter
    
    :param main_page: The function that will be called when the user wants to return to the main menu
    """
    
    ch = input("Press Enter to Exit the page or\nType 'X' to Return to Main Menu:")
    ch = ch.upper()
    
    if ch == '':
        system('cls')
        exit()
        
    elif ch == "X":
        main_page()
        

def InputNextPage(main_page, page_path, page_range):
    
    """
    It takes in a page path, and a page range, and then asks the user if they want to go to the next
    page. If so, it asks them to type the page number they want to go to. If they type 'X', it returns
    to the main menu. If they type a number, it modifies the page path to the page number they typed,
    and then prints that page
    
    :param main_page: The path to the main page
    :param page_path: The path to the page you want to print
    :param page_range: The number of pages in the book
    """

    choice =  input("\t\t\tDo you want to go to the next page? if so\n\t\t\tThen Type the Page Number to Go to that Page.\n\t\t\tYou can also Type 'X' To Return to Main Menu:")
    def Loop(CHOICE, MAIN_PAGE, PAGE_PATH, PAGE_RANGE):
        try:ch = CHOICE.upper()
        except ValueError:pass
            
        try:ch = int(CHOICE)
        except ValueError:pass
                
        if ch == 'X':
                try_again = 0; # Return to Main Menu:

        if ch in NumbersInStrings[0:PAGE_RANGE+1]: # Changes Numbers in Letters to Integers:
            for index in range(PAGE_RANGE+1):
                if ch == NumbersInStrings[index]: ch = index

        if ch in range(1,PAGE_RANGE+1): # Modifies Path to choosen Page
            try_again = 0; PAGE_PATH = PAGE_PATH[0:-6]; PAGE_PATH += f"_{ch}.txt"
            print(ch);PrintPage(PAGE_PATH)
            
        if try_again == 1:Loop(CHOICE, MAIN_PAGE, PAGE_PATH, PAGE_RANGE)
        else:pass
    Loop(choice, main_page, page_path, page_range)
        

def ListAllFunctions(_list):
    
    """
    This function prints out all the functions in a list, with a comma and space after each function
    except the last one, and a newline after every 70 characters
    
    :param _list: a list of strings, each string being the name of a function
    """
    
    print()
    _count = 0
    for i in _list:
        if i == _list[-1]:
            print(i, end = '()')
        else:
            print(i, end = '(), ')
        _count += len(i)
        if _count > 70:
            print()
            _count = 0
            
def EndModuleInterface(module_page,main_page):
    
    """
    This function is used to end the module interface and return to the main menu.
    
    :param module_page: This is the name of the function that you want to return to
    :param main_page: This is the function that will be called when the user wants to return to the main
    menu
    """
    
    choice = input("Enter 'X' or 'R' to Exit the Program or Retry with different Values\nOR\nPress Enter to return to Main Menu: ")
    choice = choice.upper()
            
    if choice in "EXIT" and choice != '':
        exit()
    elif choice in "RETRY" and choice != '':
        module_page()
    else:
        main_page()

def EXPOFFError(module_page, main_page):
    
    """
    It prints a message to the user that the function they are trying to access is in Experimental Mode,
    and that they need to turn Experimental Mode ON in the Main Menu to access it
    
    :param module_page: The page that the user is currently in
    :param main_page: The main page of the program
    """
    
    print()
    for i in range(PageWidth):
        print(BorderCharacter, end = '')
    print();print()
        
    print("The User is in Restricted Mode:\nTry Turning Experimental Mode ON\nIn the Main Menu to Access this Function.")
    print()
    for i in range(PageWidth):
        print(BorderCharacter, end = '')
    print();print()
        
    choice = input("Type 'M' to return to Main Menu, or\npress ENTER to stay at the LAST Page Attended: ")
    choice = choice.upper()
        
    if choice == "M" and choice != '':
        main_page()
    else:
        module_page()

# String Manipulation to Replace Characters [not possible with immutable data type]

def StrReplaceByte(string, index, item):
    return string[:index] + str(item) + string[index+1:]

def ReadFileReplaceByte(Path, position, item):
    
    """
    It opens a file, reads it, replaces a byte at a given position, and then writes the file back to the
    same location
    
    :param Path: The path to the file you want to edit
    :param position: (row, index)
    :param item: The item to replace the byte with
    """
    
    row, index = position
    with open(Path, "r+") as File:
        Lines = File.readlines()
        Lines[row] = StrReplaceByte(Lines[row], index, item)
        with open(Path, "w+") as File:
            File.writelines(Lines)
            File.close()
        File.close()

def stringRepeater(times,character):
    
    """
    This function takes in a number and a character, and returns a string of the character repeated the
    number of times specified.
    
    :param times: The number of times you want the character to be repeated
    :param character: The character to repeat
    :return: A string of the character repeated the number of times specified.
    """
    
    char = ""
    for i in range(times):
        char += character
    return char


    