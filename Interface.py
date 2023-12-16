# THIS IS WHAT THE USER WILL BE LOOKING AT.
# COMMONLY KNOWN AS THE G.U.I (GRAPHICAL USER INTERFACE) 

# Importing the modules that are needed for the program to run.
import Curves; import ThreeDGs; import TwoDGs; import Graphs; import Extras; import Matrices as Matrix;

from os import system

Experimental_Toggle = False   

# Defining two variables.
PageWidth = 60; BorderCharacter = "X"

# Setting up the variables for the game.
EastersCollected = 0; TotalEasters = 1

Col_I_Easter = False; Col_II_Easter = False



def MainPage():
    
    """
    It's the main page of the program
    """
    
    x = 0; system('cls')
    while(x != 1):
        Extras.PrintPage('Pages/Main/Main Page.txt')
        
        option = input("Type Selected Option and press Enter: ").upper()
        
        if option == '1':
            x = 1
            Shapes_Or_Arithemetic()
            
        elif option == '2':
            x = 1
            Special_Options()
            
        elif option == '3':
            x = 1
            Credits()
            
        elif option == '4':
            HELP()
            
        elif option == '5':
            x = 1
            Exit_Program()
            
        else:
            x = 0
            input("Error In Input Try Again By Pressing Enter: "); system("cls")



def Shapes_Or_Arithemetic():
    
    """
    It's a function that allows the user to choose between shapes and arithemetic.
    """
    
    x = 0; system('cls')
    while(x != 1):
        Extras.PrintPage('Pages/Main/Shapes Or Arithemetic.txt')
        
        option = input("Type Selected Option and press Enter: ").upper()
        
        if option == '1':
            x = 1
            Shapes()
            
        elif option == '2':
            x = 1
            Arithemetic()
            
        elif option == '3':
            x = 1
            MainPage()
            
        else:
            x = 0
            input("Error In Input Try Again By Pressing Enter: "); system("cls")

def Shapes():
    
    """
    It's a function that allows the user to choose between 3D shapes, 2D shapes, conic sections, or
    going back to the main page.
    """
    
    x = 0; system('cls')
    while(x != 1):
        Extras.PrintPage('Pages/Main/Shapes.txt')
        
        option = input("Type Selected Option and press Enter: ").upper()
        
        if option == '1':
            x = 1
            ThreeDS()
            
        elif option == '2':
            x = 1
            TwoDS()
            
        elif option == '3':
            x = 1
            if Extras.EXPOFFError(Experimental_Toggle,Shapes,MainPage):
                ConicSections()
                
        elif option == '4':
            x = 1
            Shapes_Or_Arithemetic()
            
        else:
            x = 0
            input("Error In Input Try Again By Pressing Enter: "); system("cls")

def ThreeDS():
    
    """
    It's a function that allows the user to select a 3D Geometry option.
    """
    
    x = 0; system('cls')
    while(x != 1):
        Extras.PrintPage('Pages/Main/ThreeDG/Opt3DGs.txt')
        
        option = input("Type Selected Option and press Enter: ").upper()
        
        if option == '1':
            x = 1
            Cubes()
            
        elif option == '2':
            x = 1
            Cuboids()
            
        elif option == '3':
            x = 1
            Shapes()
        else:
            x = 0
            input("Error In Input Try Again By Pressing Enter: "); system("cls")
            
def Cubes():
    
    """
    It's a function that prints the 3D Geometry Cubes page and then calls the appropriate function based
    on the user's input.
    """
    
    x = 0; system("cls")
    while(x != 1):
        Extras.PrintPage('Pages/Main/ThreeDG/_Cubes.txt')
        
        option = input("Type Selected Option and press Enter: ").upper()
        
        if option == '1':
            x = 1 # Hollow Cube
            
            for i in range(PageWidth):
                print(BorderCharacter, end = '')
            print()
            
            SideLength = int(input("Enter the length of the Edge: "))
            FillerCharacters = input("Enter the Face Characters (Any character): ")
            
            try:
                ThreeDGs.Filled_Cube(SideLength, FillerCharacters)
            except Exception:
                ThreeDGs.Filled_Cube(SideLength, "  ")
                
            print()
            for i in range(PageWidth):
                print(BorderCharacter, end = '')
            print()
            
            Extras.EndModuleInterface(Cubes,MainPage)
            
            
            
        elif option == '2':
            x = 1 # Filled Cube
            
            for i in range(PageWidth):
                print(BorderCharacter, end = '')
            print()
            
            SideLength = int(input("Enter the length of the Edge: "))
            FillerCharacters = input("Enter the Face Characters (Any character): ")
            
            try:
                ThreeDGs.Filled_Cube(SideLength, FillerCharacters)
            except Exception:
                ThreeDGs.Filled_Cube(SideLength, "  ")
                
            print()
            for i in range(PageWidth):
                print(BorderCharacter, end = '')
            print()
            
            Extras.EndModuleInterface(Cubes,MainPage)
            
        elif option == '3':
            x = 1
            ThreeDS()
        else:
            x = 0
            input("Error In Input Try Again By Pressing Enter: "); system("cls")
    

def Cuboids():
    
    """
    It's a function that prints the Cuboids page and then calls the appropriate function based on the
    user's input.
    """
    
    x = 0; system("cls")
    while(x != 1):
        Extras.PrintPage('Pages/Main/ThreeDG/_Cuboids.txt')
        
        option = input("Type Selected Option and press Enter: ").upper()
        
        if option == '1':
            x = 1 # Hollow Cuboid
            
            for i in range(PageWidth):
                print(BorderCharacter, end = '')
            print()
            
            SideLength = int(input("Enter the length of the Edge: "))
            SideWidth = int(input("Enter the Width of the Edge: "))
            SideHigh = int(input("Enter the Height of the Edge: "))
            FillerCharacters = input("Enter the Face Characters (Any character): ")
            
            try:
                ThreeDGs.Hollow_Cuboid(SideLength, SideWidth, SideHigh, FillerCharacters)
            except Exception:
                ThreeDGs.Hollow_Cuboid(SideLength, SideWidth, SideHigh, "  ")
                
            print()
            for i in range(PageWidth):
                print(BorderCharacter, end = '')
            print()
            
            Extras.EndModuleInterface(Cuboids,MainPage)
            
        elif option == '2':
            x = 1 # Filled Cuboid
            
            for i in range(PageWidth):
                print(BorderCharacter, end = '')
            print()
            
            SideLength = int(input("Enter the length of the Edge: "))
            SideWidth = int(input("Enter the Width of the Edge: "))
            SideHigh = int(input("Enter the Height of the Edge: "))
            FillerCharacters = input("Enter the Face Characters (Any character): ")
            
            try:
                ThreeDGs.Filled_Cuboid(SideLength, SideWidth, SideHigh, FillerCharacters)
            except Exception:
                ThreeDGs.Filled_Cuboid(SideLength, SideWidth, SideHigh, "  ")
                
            print()
            for i in range(PageWidth):
                print(BorderCharacter, end = '')
            print()
            
            Extras.EndModuleInterface(Cuboids,MainPage)
            
        elif option == '3':
            x = 1
            ThreeDS()
        else:
            x = 0
            input("Error In Input Try Again By Pressing Enter: "); system("cls")
    
    
    
def TwoDS():
    
    """
    It's a function that allows the user to select a 2D Geometry option.
    """
    
    x = 0; system("cls")
    while(x != 1):
        Extras.PrintPage('Pages/Main/TwoDG/Opt2DGs.txt')
        
        option = input("Type Selected Option and press Enter: ").upper()
        
        if option == '1':
            x = 1
            Square()
            
        elif option == '2':
            x = 1
            Rectangle()
            
        elif option == '3':
            x = 1
            Triangle()
                    
        elif option == '4':
            x = 1
            Shapes()
        else:
            x = 0
            input("Error In Input Try Again By Pressing Enter: "); system("cls")

def Square():
    
    """
    It's a function that prints a square
    """
    
    x = 0; system("cls")
    while(x != 1):
        Extras.PrintPage('Pages/Main/TwoDG/_Square.txt')
        
        option = input("Type Selected Option and press Enter: ").upper()
        
        if option == '1':
            x = 1 # Hollow Square
            for i in range(PageWidth):
                print(BorderCharacter, end = '')
            print()
            
            SideLength = int(input("Enter the length of the Side: "))
            TwoDGs.Square(SideLength, False)
            
            print()
            for i in range(PageWidth):
                print(BorderCharacter, end = '')
            print()
            
            Extras.EndModuleInterface(Square,MainPage)
            
        elif option == '2':
            x = 1 # Filled Square
            for i in range(PageWidth):
                print(BorderCharacter, end = '')
            print()
            
            SideLength = int(input("Enter the length of the Side: "))
            TwoDGs.Square(SideLength, True)
            
            print()
            for i in range(PageWidth):
                print(BorderCharacter, end = '')
            print()
            
            Extras.EndModuleInterface(Square,MainPage)
            
        elif option == '3':
            x = 1
            TwoDS()
        else:
            x = 0
            input("Error In Input Try Again By Pressing Enter: "); system("cls")

def Rectangle():
    
    """
    It's a function that prints a rectangle.
    """
    
    x = 0; system("cls")
    while(x != 1):
        Extras.PrintPage('Pages/Main/TwoDG/_Rectangle.txt')
        
        option = input("Type Selected Option and press Enter: ").upper()
        
        if option == '1':
            x = 1 # Hollow Rectangle
            
            for i in range(PageWidth):
                print(BorderCharacter, end = '')
            print()
            
            SideLength = int(input("Enter the length of the Side: "))
            SideWidth = int(input("Enter the Width of the Side: "))
            
            TwoDGs.Rectangle(SideWidth, SideLength, False)
            
            print()
            for i in range(PageWidth):
                print(BorderCharacter, end = '')
            print()
            
            Extras.EndModuleInterface(Rectangle,MainPage)
            
        elif option == '2':
            x = 1 # Filled Rectangle
            
            for i in range(PageWidth):
                print(BorderCharacter, end = '')
            print()
            
            SideLength = int(input("Enter the length of the Side: "))
            SideWidth = int(input("Enter the Width of the Side: "))
            
            TwoDGs.Rectangle(SideWidth, SideLength, True)
            
            print()
            for i in range(PageWidth):
                print(BorderCharacter, end = '')
            print()
            
            Extras.EndModuleInterface(Rectangle,MainPage)
            
        elif option == '3':
            x = 1
            TwoDS()
        else:
            x = 0
            input("Error In Input Try Again By Pressing Enter: "); system("cls")

def Triangle():
    
    """
    It's a function that generates a triangle of the user's choice.
    """
    
    x = 0; system("cls")
    while(x != 1):
        Extras.PrintPage('Pages/Main/TwoDG/_Triangle.txt')
        
        option = input("Type Selected Option and press Enter: ").upper()
        
        if option == '1':
            INPUTERROR = 1
            x = 1 # Hollow Triangle
            
            for i in range(PageWidth):
                print(BorderCharacter, end = '')
            print()
            
            SideLength = int(input("Enter the length of the Side: "))
            
            while(INPUTERROR != 0):
                
                Type = input("Enter the type of Triangle To Be Generated\n(TopRight, TopLeft, DownRight, DownLeft, Upwards) :")
                Type = Type.upper()
                
                if Type == "TOPRIGHT": Type = "tr"; INPUTERROR = 0
                elif Type == "TOPLEFT": Type = "tl"; INPUTERROR = 0
                elif Type == "DOWNRIGHT": Type = "dr"; INPUTERROR = 0
                elif Type == "DOWNLEFT": Type = "dl"; INPUTERROR = 0
                elif Type == "UPWARDS": Type = "up"; INPUTERROR = 0
                
                else:
                    INPUTERROR = 1; print("INPUT ERROR: Try Again!")
                    for i in range(PageWidth):
                        print(BorderCharacter, end = '')
                    print()
                
            TwoDGs.Triangle(SideLength, Type, False)
            
            print()
            for i in range(PageWidth):
                print(BorderCharacter, end = '')
            print()
            
            Extras.EndModuleInterface(Triangle,MainPage)
            
        elif option == '2':
            INPUTERROR = 1
            x = 1 # Filled Triangle
            
            for i in range(PageWidth):
                print(BorderCharacter, end = '')
            print()
            
            SideLength = int(input("Enter the length of the Side: "))
            
            while(INPUTERROR != 0):
                
                Type = input("Enter the type of Triangle To Be Generated\n(TopRight, TopLeft, DownRight, DownLeft, Upwards) :")
                Type = Type.upper()
                
                if Type == "TOPRIGHT": Type = "tr"; INPUTERROR = 0
                elif Type == "TOPLEFT": Type = "tl"; INPUTERROR = 0
                elif Type == "DOWNRIGHT": Type = "dr"; INPUTERROR = 0
                elif Type == "DOWNLEFT": Type = "dl"; INPUTERROR = 0
                elif Type == "UPWARDS": Type = "up"; INPUTERROR = 0
                
                else:
                    INPUTERROR = 1; print("INPUT ERROR: Try Again!")
                    for i in range(PageWidth):
                        print(BorderCharacter, end = '')
                    print()
                
            TwoDGs.Triangle(SideLength, Type, True)
            
            print()
            for i in range(PageWidth):
                print(BorderCharacter, end = '')
            print()
            
            Extras.EndModuleInterface(Triangle,MainPage)
            
        elif option == '3':
            x = 1
            TwoDS()
        else:
            x = 0
            input("Error In Input Try Again By Pressing Enter: "); system("cls")



def ConicSections():
    x = 0; system('cls')
    print("ERROR 404: Please Try Again later")




def Arithemetic():
    
    """
    It's a function that allows the user to choose between the Robust Calculator, Matrices, Calculus,
    and Shapes.
    """
        
    x = 0; system('cls')
    while(x != 1):
        Extras.PrintPage('Pages/Main/Arithemetic.txt')
        
        option = input("Type Selected Option and press Enter: ").upper()
        
        if option == '1':
            x = 1
            RobustCalculator()
            
        elif option == '2':
            if Experimental_Toggle:
                x = 1
                Matrices()
            else:
                Extras.EXPOFFError(Arithemetic, MainPage)
            

        elif option == '3':
            if Experimental_Toggle:
                x = 1
                Calculus()
            else:
                Extras.EXPOFFError(Arithemetic, MainPage)
            
            
            
        elif option == '4':
            x = 1
            Shapes_Or_Arithemetic()
            
        else:
            x = 0
            input("Error In Input Try Again By Pressing Enter: "); system("cls")

def SimpleCalculations():
    
    """
    It takes a string input, evaluates it and prints the result
    """
    
    x = 0; system('cls')
    while(x != 1):
        Extras.PrintPage('Pages/Main/Arithemetic/SimpleCalc.txt')
        
        option = input("Type Selected Option/Calculation and press Enter:\n").upper()
        if "=" in option[-1]:
            option = option[:-1]
        
        if option == 'X':
            x = 1
            MainPage()
            
        elif option == 'R':
            x = 1
            Arithemetic()
        
        try:
            result = eval(option)
            print(f"Calculate: {option}")
            print(f"Result: {result}")
            _option = input("Press Enter to Continue or Type 'X' to Return to Main Menu: ")
            if _option == 'X':
                x = 1
                MainPage()
            else:
                SimpleCalculations()
            
            
        except Exception:
            x = 0
            input("Error In Input Try Again By Pressing Enter: "); system("cls")
            SimpleCalculations()

def RobustCalculator():
    
    """
    It's a calculator that can do basic arithemetic operations
    """
    
    Path = 'Pages\Main\Arithemetic\Robust Calculator.txt'
    row = 8
    item = "X                                                          X\n"  

    with open(Path, "r+") as File:
        Lines = File.readlines()
        Lines[row] = item
        with open(Path, "w+") as File:
            File.writelines(Lines)
            File.close()
        File.close()
    Extras.PrintPage('Pages\Main\Arithemetic\Robust Calculator.txt')
    
    while(x != 1):
        x = 0; system('cls')  
        
        calc = ""
        while option != "=":
            option = input("Start: ")
            if option == 'X'.lower():
                x = 1
                MainPage()
                    
            elif option == 'R'.lower():
                x = 1
                Arithemetic()
            elif option in "1234567890.%/*-+sincosectancotrootpower()ce":
                    calc += option
                    input(calc)
                    try: eval(calc)
                    except Exception:
                        option = "="
                        x = 0
                        input("Unknown Calculation Format!"); system("cls")
                        RobustCalculator()
                    
                    for index in range(len(calc)):
                        Extras.ReadFileReplaceByte("Pages\Main\Arithemetic\Robust Calculator.txt", (8,3+(index+1)),calc[index])
                    Extras.PrintPage('Pages\Main\Arithemetic\Robust Calculator.txt')
                    try:
                        result = eval(option)
                        
                        for index in range(len(result)):
                            Extras.ReadFileReplaceByte("Pages\Main\Arithemetic\Robust Calculator.txt", (8,3+(index+1)),result[index])
                            Extras.PrintPage('Pages\Main\Arithemetic\Robust Calculator.txt')
                            
                            
                        
                        _option = input("Press Enter to Continue or Type 'X' to Return to Main Menu:")
                        if _option == 'X':
                            x = 1
                            MainPage()
                        else:
                            for index in range(len("X                                                          X\n")):
                                Extras.ReadFileReplaceByte("Pages\Main\Arithemetic\Robust Calculator.txt", (8,0),
                                                           "X                                                          X\n"[index])
                                RobustCalculator()

                    except Exception:
                        x = 0
                        input("Unknown Calculation Format!"); system("cls")
                        RobustCalculator()
                    
                
            
        


def Matrices():

    """
    It's a function that allows the user to create a matrix, modify it, and void it.
    """
    
    x = 0; system('cls')
    
    global EastersCollected, Col_II_Easter, M1
    
    while(x != 1):
        Extras.PrintPage('Pages/Main/Arithemetic/Matrices/Matrices.txt')
        
        option = input("Type Selected Option and press Enter: ").upper()
        
        if option == '1':
            x = 0
            
            for i in range(PageWidth):
                print(BorderCharacter, end = '')
            print()
            
            Columns = int(input("Enter the number of Columns for the Matrix: "))
            if Columns < 0: Columns = 0
            Rows = int(input("Enter the number of Rows for the Matrix: "))
            if Rows < 0: Rows = 0
            
            if Columns == 6 and Rows == 9:
                if Col_II_Easter == False:
                    system("cls")
                    input("<<<Easter Egg Collected!>>>\nGo To Special Options For more Info! Press ENTER to Continue! ")
                    EastersCollected += 1
                    Col_II_Easter = True
                else:
                    system("cls")
                    input("Don't be Greedy this Easter Egg has already been collected!\nPress Enter to return to Last Page: ")
            M1 = Matrix.Matrix(Rows, Columns, unity = False)
            
            print()
            M1()
            
            input("Press Enter to Return to the Last Page.")
            Matrices()
            
            
            
        elif option == '2':
            x = 1
            Modify_M()

        elif option == '3':
            x = 1; y = 0
            M1 = None
            input("The Matrix is now Voided. Press Enter to Return: ")
            Matrices()
            
        
        elif option == 'X':
            x = 1
            MainPage()
            
        elif option == 'R':
            
            x = 1
            Arithemetic()
            
        else:
            x = 0
            input("Error In Input Try Again By Pressing Enter: "); system("cls")

def Modify_M():
    
    """
    It's a function that allows the user to modify the matrix M1
    """
    
    global M1
    
    x = 0; system('cls')
    
    while(x != 1):
        Extras.PrintPage('Pages/Main/Arithemetic/Matrices/Modify_M.txt')
        
        option = input("Type Selected Option and press Enter: ").upper()
        
        if option == '1':
            x = 1
            
            for i in range(PageWidth):
                print(BorderCharacter, end = '')
            print()
            
            # Input cols n rows
            
            Columns = int(input("Enter the number of Columns for the Matrix: "))
            if Columns < 0: Columns = 0
            Rows = int(input("Enter the number of Rows for the Matrix: "))
            if Rows < 0: Rows = 0
            
            # Initiate matrix
            
            M1 = Matrix.Matrix(Rows, Columns, unity = False)
            
            # Path / Set / Input
            
            option = input("\nEnter the Path to a csv file to load The values into the\nMatrix or Press Type 'set' to set the values into the Matrix\nor press Enter to input values: ").upper()
            print()
            
            if option == "SET":
                x = 1
                Set_M()   
            try:
                M1.load_data(option, deli = ","); x = 1
            except FileNotFoundError:
                M1.input_items(); x = 1
                
            M1()
            
            for i in range(PageWidth):
                print(BorderCharacter, end = '')
            print()
            
            input("Press Enter to Return to last Page: ")
            Modify_M()
            
            
        elif option == '2': # Display
            x = 1
            try:
                M1()
                input("Press Enter to return to the last Known Page: ")
                Modify_M()
            except Exception:
                input("The Matrix Has Yet to Initiated!")
                Modify_M()

        elif option == '3': # Transform
            x = 1;
            Transform_M()
            
        
        elif option == 'X':
            x = 1
            MainPage()
            
        elif option == 'R':
            
            x = 1
            Arithemetic()
            
        else:
            x = 0
            input("Error In Input Try Again By Pressing Enter: "); system("cls")    


def Set_M():
    
    """
    It sets the matrix with the given data type and range.
    """
        
    global M1
    
    x = 0; system("cls")
                
    while(x != 1):
                
        for i in range(PageWidth):
            print(BorderCharacter, end = '')
        print()
                    
        Type = input("Enter the data type that you want to set the Matrix with.\n(Types => int/float/byte/identity/diagnol): "); Type = Type.upper()

        if Type in ["INT", "FLOAT", "BYTE"]:
            Range = int(input("Enter the range of the datas. (Recommended from <10 - 10000> for best results): "));
            M1.set_rand(Type, Range); x = 1
            input("Press Enter to return to the Last Known Page: ")
            Modify_M()
        elif Type == "IDENTITY":
            M1.set_identity(); x = 1
            input("Press Enter to return to the Last Known Page: ")
            Modify_M()
        elif Type == "DIAGNOL":
            M1.set_diagnol(input("Enter the Diagnol Element: ")); x = 1
            input("Press Enter to return to the Last Known Page: ")
            Modify_M()
            
        else:
            x = 0
            input("Error In Input Try Again By Pressing Enter: "); system("cls")  

def Transform_M():
    
    """
    It's a function that allows the user to transform the matrix M1 in various ways.
    """
    
    global M1
    
    x = 0; system('cls')
    
    while(x != 1):
        Extras.PrintPage('Pages/Main/Arithemetic/Matrices/Transform_M.txt')
        
        option = input("Type Selected Option and press Enter: ").upper()
        
        if option == '1':
            x = 1
            M1 = M1.transpose()
            M1()
            input("Press Enter to return to the last Known Page: ")
            Transform_M()
            
        elif option == '2':
            x = 1
            M1 = M1.symmetric()
            M1()
            input("Press Enter to return to the last Known Page: ")
            Transform_M()
        
        elif option == '3':
            x = 1
            M1 = M1.skew_symmetric()
            M1()
            input("Press Enter to return to the last Known Page: ")
            Transform_M()
        
        elif option == 'X':
            x = 1
            MainPage()
            
        elif option == 'R':
            
            x = 1
            Modify_M()
            
        else:
            x = 0
            input("Error In Input Try Again By Pressing Enter: "); system("cls")   
            
                
            
            
        
            
               

def Calculus():
    x = 0; system('cls')
    print("ERROR 404: Please Try Again later")

def Special_Options():
    
    """
    This function is used to toggle the Experimental Mode on or off
    """
    
    x = 0; system('cls')
    global Experimental_Toggle
    global EastersCollected
    while(x != 1):
        
        if EastersCollected > 0:
            
            Extras.ReadFileReplaceByte('Pages/Main/Special_Options_EGGS.txt', (8, 39), EastersCollected) 
            Extras.PrintPage('Pages/Main/Special_Options_EGGS.txt')
            
        else:Extras.PrintPage('Pages/Main/Special_Options.txt')
        
        # Experimental Notification:
        
        if Experimental_Toggle == False: 
            print("Experimental Mode is OFF")
        elif Experimental_Toggle == True:
            print("Experimental Mode is ON")
        
        option = input("Type Selected Option and press Enter: ").upper()
        
        if option == '1': #ToggleEXPMode ON or OFF
            x = 1
            if Experimental_Toggle == False: ExperimentalOFF()
            elif Experimental_Toggle == True: ExperimentalON()  
     
            
        elif option == '2':
            x = 1
            MainPage()
            
        else:
            x = 0
            input("Error In Input Try Again By Pressing Enter: "); system("cls")

def ExperimentalOFF():
    
    """
    It's a function that allows the user to turn off the experimental mode.
    """
    
    x = 0; system('cls')
    global Experimental_Toggle
    while(x!= 1):
                    
        Extras.PrintPage('Pages/Main/Special_Options/ExpOFF.txt')
            
        option = input("Type Selected Option and press Enter: ").upper()
        
        if option == '1':
            Experimental_Toggle = True
            x = 1
            ExperimentalON()
            
        elif option == '2':
            x = 1
            MainPage()
            
        else:
            x = 0
            input("Error In Input Try Again By Pressing Enter: "); system("cls")

def ExperimentalON():
    
    """
    It's a function that allows the user to turn on the experimental mode.
    """
    
    x = 0; system('cls')
    global Experimental_Toggle
    while(x != 1):
                    
        Extras.PrintPage('Pages/Main/Special_Options/ExpON.txt')
            
        option = input("Type Selected Option and press Enter: ").upper()
        
        if option == '1':
            Experimental_Toggle = False
            x = 1
            ExperimentalOFF()
            
        elif option == '2':
            x = 1
            MainPage()
            
        else:
            x = 0
            input("Error In Input Try Again By Pressing Enter: "); system("cls")
 
           

def Credits():
    
    """
    It prints the credits page and then returns to the main page.
    """
    
    x = 0; system('cls')
    while(x != 1):
        Extras.PrintPage('Pages/Main/Credits.txt')
        
        option = input("Type Selected Option and press Enter: ").upper()
        
        if option == '1':
            x = 1
            MainPage()
            
        else:
            x = 0
            input("Error In Input Try Again By Pressing Enter: "); system("cls")

def HELP():
    
    """
    This function is used to display the introductory page of the HELP function.
    """
    
    x = 0; system('cls')
    global HelpCommand
    
    while(x != 1):
        Extras.PrintPage('Pages/HELP/Introductory_Page.txt')
            
        HelpCommand = input("Type 'X' to Return to Main Menu or\nType 'modules' to know more\nabout the functions of this extension module: ")
        HelpCommand = HelpCommand.upper()
        
        if HelpCommand == "X":
            x = 1; MainPage()
            
        elif HelpCommand == "MODULES": 
            x = 1; MODULES();

def MODULES():
    
    """
    It's a function that helps you to get help with the modules.
    """
    
    x = 0; system("cls")
    global Page,FunctionName,PageRange
    global EastersCollected ,Col_I_Easter

    while(x != 1):
        Extras.PrintPage('Pages/HELP/MODULES.txt')
            
        HelpCommand = int(float(input("Type Selected Option and press Enter: ").upper())//1)
        if HelpCommand > 7 or HelpCommand < 1: MODULES()
        for i in Extras.ModuleDict.items():
            # The items are like this [(ModuleName,[ItemNumber,PageRange]),(ModuleName2,[ItemNumber2,PageRange2]),...]
            if i[1][0] == HelpCommand:
                PageRange = i[1][1]
                FunctionName = i[0]
                
        # A list of strings, which are used to display a message to the user, when the user enters a
        # page number which is out of range.
        EasterSpecialList1 = [f"Page out of Range! Try again, Remember 'Total {PageRange} Pages': ",
                            f"Not again ._. , Remember! 'Total {PageRange} Pages': ",
                            f"And ... You've done it again!\nHow many times should I remind You?\nIn Total there are only {PageRange} of Pages\nNow Type Properly: ",
                            f"You need help ... Go to a doctor and ...\nGet your eyesight checked ... Anyways Do it properly\nOr I shall force it to the First Page,\nOnce Again There are only {PageRange} Pages: "]        

        Page = int(float(input(f"Enter the Page to Get Help with (Total {PageRange} Pages): "))//1)
        Attempt = 0
        
        
        
        while Page > PageRange or Page < 0:
            
            for index in range(4):
                system("cls");Extras.PrintPage('Pages/HELP/MODULES.txt')
                Page = int(float(input(EasterSpecialList1[index]))//1)
                if Page <= PageRange and Page > 0: break
                
            # Checking if the user has entered a valid page number. If the user has entered a valid
            # page number, the program will break out of the while loop. If the user has not entered a
            # valid page number, the program will print the page again and set the page number to 1.
                
            if Page <= PageRange and Page > 0: break
            else:
                
                system("cls");Extras.PrintPage('Pages/HELP/MODULES.txt')
                
                Page = 1;
                
                # Checking if the Easter Egg has been collected or not. If it has not been collected,
                # it will print out a message saying that the Easter Egg has been collected and will
                # add 1 to the amount of Easter Eggs collected. If it has been collected, it will
                # print out a message saying that there are no more options remaining.
                
                if Col_I_Easter == False:
                    input("<<<Easter Egg Collected!>>>\nGo To Special Options For more Info! Press ENTER to Continue! ")
                    EastersCollected += 1
                    Col_I_Easter = True
                else:
                    input("There are no more Options Remaining! Press ENTER to Continue! ")

        x = 1
        Pager(FunctionName,Page)

def Pager(SelectedModule,PageNumber):
    
    """
    It prints the help page of the selected module
    
    :param SelectedModule: The module you want to view
    :param PageNumber: The page number you want to display
    """
    
    x = 0; system("cls")
    
    # Created a New Module list With Proper Case:
    
    CURVE = "Curves"
    ONED = "OneDGS"
    TWOD = "TwoDGS"
    _3D = "ThreeDGS"
    GRAPHS = "Graphs"
    GUI = "Interface"
    EXT = "Extras"
    
    ModulesTuple = (CURVE,ONED,TWOD,_3D,GRAPHS,GUI,EXT)
    
    Path = "Pages/Help/HelpModules/"

    for Module in ModulesTuple:
        if SelectedModule == Module.upper() and Page <= PageRange:

            for number in range(1,PageRange+1):
                if PageNumber == number: Extras.PrintPage(Path + Module + f"_{number}.txt")

    Optioner(Pager)
      
def Optioner(ReturnFunction):
    
    """
    It's a function that takes a function as an argument and returns a function that takes an argument
    
    :param ReturnFunction: This is the function that you want to return to
    """
    
    OptTuple = (Extras.NumbersInStrings, Extras.AlphasInStrings, Extras.PositionsInStrings, Extras.PosInStrings, Extras.RomansInStrings)
    
    print("\t\t\tDo you want to go to the next page? if so\n\t\t\tThen Type the Page Number to Go to that Page.")
    Choice = input("\t\t\tYou can also Type 'X' or 'R' To Return to Main Menu or Module Page: ").upper()
    
    try: Choice = int(Choice)
    except ValueError: pass
    
    while True:
        if Choice == "X": MainPage()
        
        elif Choice == "R": MODULES()
        
        for List in OptTuple:
            if Choice in List[0:PageRange+1]:
                for index in range(PageRange+1):
                    if Choice == List[index]: Choice = index; ReturnFunction(FunctionName, Choice)
                    
def Exit_Program():
    
    """
    It's a function that asks the user if they want to exit the program
    """
    
    x = 0; system('cls')
    
    while(x != 1):
        Extras.PrintPage('Pages/Main/Exit The Program.txt')
        
        option = input("Type Selected Option and press Enter: ").upper()
        
        if option == '1':
            x = 1
            system("cls")
            exit()

        else:
            x = 0
            MainPage()

MainPage()
