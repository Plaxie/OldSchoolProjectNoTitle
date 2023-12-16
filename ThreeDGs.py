
# !IMPORTANT! BY : ADIL : XII-D:2110092 : YARA INTERNATIONAL SCHOOL : JULY 2022-23
#
#    THIS MODULE CONTAINS ALL THE FUNCTIONS RELATED TO ThreeDGs:
#                          i.e Three-Dimensional-Geometries.
#    ALL THE FUNCTIONS HAVE BEEN MADE FROM SCRATCH WITH NO TYPE OF PLAGERIZING INVOLVED.
#    THIS INCLUDES THE PRINT STATEMENTS AND ALL THE LOGIC USED. HENCE THERE MUST BE NO COMPLAINS
#    IN REGARDS TO THIS MODULE'S CREATION. EXCEPT FOR THE IN-BUILT MODULES

#       THOUGH ONLY CUBICS WILL BE USED SINCE CREATING SPHERICAL BODIES WITH PURE ASTERISK AND SMALL SIZE
#       IS A BIT DIFFICULT TO CREATE A STAISFIABLE RESULT.

import random
from math import fabs, floor

FunctionsAvailable = ["O_cube", "T_cube", "O_cuboid", "T_cuboid",
                      "Filled_Cube", "Hollow_Cube", "Filled_Cuboid", "Hollow_Cuboid"]

def O_cube(): # Creates an Opaque Cube
    print("* * * * * * * * * *       ")
    print("* *                 *     ")
    print("*   *                 *   ")
    print("*     * * * * * * * * * * ")
    print("*     *                 * ")
    print("*     *                 * ")
    print("*     *                 * ")
    print("*     *                 * ")
    print("*     *                 * ")
    print("*     *                 * ")
    print("  *   *                 * ")
    print("    * *                 * ")
    print("      * * * * * * * * * * ")

def T_cube(): # Creates a Transperant Cube
    print("* * * * * * * * * *       ")
    print("* *               * *     ")
    print("*   *             *   *   ")
    print("*     * * * * * * * * * * ")
    print("*     *           *     * ")
    print("*     *           *     * ")
    print("*     *           *     * ")
    print("*     *           *     * ")
    print("*     *           *     * ")
    print("* * * * * * * * * *     * ")
    print("  *   *             *   * ")
    print("    * *               * * ")
    print("      * * * * * * * * * * ")
        
def O_cuboid():
    print("* * * * * * * * * * * * *")
    print("* *                       *")
    print("*   *                       *")
    print("*     * * * * * * * * * * * * *")
    print("*     *                       *")
    print("*     *                       *")
    print("  *   *                       *")
    print("    * *                       *")
    print("      * * * * * * * * * * * * *")
        
def T_cuboid():
    print("* * * * * * * * * * * * *")
    print("* *                     * *")
    print("*   *                   *   *")
    print("*     * * * * * * * * * * * * *")
    print("*     *                 *     *")
    print("* * * * * * * * * * * * *     *")
    print("  *   *                   *   *")
    print("    * *                     * *")
    print("      * * * * * * * * * * * * *")

# LEFT ON 06 - 06 - 2022

# AT THIS POINT OF TIME I HAD TOHUGHT OF NOT MAKING ACTUAL FUNCTIONS AS THE LOGIC WAS 
# UNCLEAR TO ME AS TO HOW I WOULD BE ABLE TO CONFIGURE THEM. BUT AFTER WORKING A BIT 
# ON THE 2D SHAPES I AM BACK TO GIVE IT A SHOT. THE LOGIC IS STILL TO BE DETERMINED 
# BUT IF THE CUBE IS DONE; THE REST OF THE REMAINING SHAPES SHOULD BE EASIER TO CREATE

# ONCE AGAIN THESE WILL BE EXPERIMENTAL FUNCTIONS THAT WILL NOT BE AVAILABLE BY DEFAULT IN THE INTERFACE.

# START ON 01 - 07 - 2022

# THE LOGIC HAS BEEN CREATED AND WILL BE AVAILABLE IN THE LOGIC FOLDER

def Filled_Cube(Length = 3.0, FILLER = '  '): # We will use 5 as length here FOR TESTING
    
    """
    It takes a length and a filler and prints a cube with the given length and the given filler
    
    :param Length: The length of the cube
    :param FILLER: The filler is the character that will be used to fill the cube, defaults to   
    (optional)
    """


    # The code below is checking if the length is less than 2. If it is, it will print a message and
    # change the length to 2.
    Length = int(fabs(Length))
    if Length < 2:
        print("Must have atleast two points to form a Cube. Therefore Changed to length 2.")
        Length = 2

    FILLER = FILLER.upper()

    CUBE = ""
    VOID = '  '
    DOT = '* '
    DOTEND = DOT + '\n'  
    
    
    gen = random.randint(0, 1)
    if gen == 0:    
        FILLER = FILLER[:2]
        
    elif gen == 1:
        FILLER = FILLER[0] + FILLER[-1]
    
    if len(FILLER) < 2:
        FILLER = "  "
    
    Diagnol = int(floor(Length / 2.0)) # DIA = floor of 2.5 = 2.0 = 2
    Height = int(Length + Diagnol)          # HEIGHT = 5 + 2 = 7  
    Length = int(Length)
    
    # The above code is creating a cube with the given dimensions.    
    
    for i in range(1,Height+1,1):
        
        if i == 1:                              # THE FIRST LINE
            for j in range(Length):
                CUBE += DOT
            CUBE += "\n"
    
        elif i == Diagnol+1:                    # THE FRONT TOP EDGE
            CUBE += DOT
            for j in range(Diagnol - 1):
                CUBE += FILLER
            for j in range(Length):
                CUBE += DOT
            CUBE += "\n"
                
        elif i == Height:                       # THE BOTTOM EDGE
            for j in range(Diagnol):
                CUBE += VOID
            for j in range(Length):
                CUBE += DOT
            CUBE += "\n"
        
        elif i < Diagnol+1 and i > 1:           # THE LEFT FACE TOP EDGE
            CUBE += DOT
            for j in range(i-2):
                CUBE += FILLER
            CUBE += DOT    
            for J in range(Length - 2):
                CUBE += FILLER
            CUBE += DOTEND
        
        elif i > Diagnol and i < Length+1:      # THE MIDDLE Height EDGES
            CUBE += DOT
            for j in range(Diagnol - 1):
                CUBE += FILLER
            CUBE += DOT
            for J in range(Length - 2):
                CUBE += FILLER
            CUBE += DOTEND
        
        elif i > Length and i != Height:        # THE LEFT FACE BOTTOM EDGE
            gap = i - Length
            for j in range(gap):
                CUBE += VOID
            CUBE += DOT
            for j in range(Diagnol - gap - 1):
                CUBE += FILLER
            CUBE += DOT
            for j in range(Length - 2):
                CUBE += FILLER
            CUBE += DOTEND                  
                
    print(CUBE)
    
def Hollow_Cube(Length = 3.0,FILLER = '  '):
    
    """
    It takes the length of the cube and the filler as input and prints a hollow cube of the given length
    
    :param Length: The length of the cube
    :param FILLER: The filler is the character that will be used to fill the cube, defaults to   
    (optional)
    """

    # Checking if the length is less than 2 and if it is, it changes it to 2.
    Length = int(fabs(Length))
    if Length < 2:
        print("Must have atleast two points to form a Cube. Therefore Changed to length 2.")
        Length = 2


    FILLER = FILLER.upper()
    CUBE = ""  
    VOID = '  '
    DOT = '* '
    DOTEND = DOT + '\n'  
    
    # Generating a random number between 0 and 1, and then using that number to determine which
    # characters to use in the FILLER variable.
    gen = random.randint(0, 1)
    if gen == 0:    
        FILLER = FILLER[:2]
    elif gen == 1:
        FILLER = FILLER[0] + FILLER[-1]
    if len(FILLER) < 2:
        FILLER = "  "
    
    Diagnol = int(floor(Length / 2.0)) # DIA = floor of 2.5 = 2.0 = 2
    Height = int(Length + Diagnol)          # HEIGHT = 5 + 2 = 7  
    Length = int(Length)
    
    # The code below is creating a cube with the given dimensions.
    for i in range(1,Height+1,1):
        
        if i == 1:                              # THE FIRST LINE
            for j in range(Length):
                CUBE += DOT
            CUBE += "\n"
    
        elif i == Diagnol+1:                    # THE FRONT TOP EDGE
            CUBE += DOT
            for j in range(Diagnol - 1):
                CUBE += FILLER
            for j in range(Length):
                CUBE += DOT
            CUBE += "\n"
                
        elif i == Height:                       # THE BOTTOM EDGE
            for j in range(Diagnol):
                CUBE += VOID
            for j in range(Length):
                CUBE += DOT
            CUBE += "\n"
        
        elif i < Diagnol+1 and i > 1:           # THE LEFT FACE TOP EDGE
            
            CUBE += DOT
            for j in range(i-2):
                CUBE += FILLER
            CUBE += DOT 
            midSpace = (Length-2) - (i-2) - 1
            for j in range(midSpace):
                CUBE += FILLER   
            CUBE += DOT
            for j in range(i-2):
                CUBE += FILLER
            CUBE += DOTEND

        elif i > Diagnol and i < Length:      # THE MIDDLE Height EDGES
            
            # FOR EVEN LENGTH
            if Length % 2 == 0:
                CUBE += DOT
                for j in range(Diagnol - 1):
                    CUBE += FILLER
                CUBE += DOT    
                for j in range(Length - Diagnol - 2):
                    CUBE += FILLER
                CUBE += DOT
                for j in range(Diagnol - 1):
                    CUBE += FILLER            
                CUBE += DOTEND
            
            # FOR ODD LENGTH
            if Length % 2 != 0:
                for j in range(7):
                    if j % 2 == 0:
                        CUBE += DOT
                        if j == 6:
                            CUBE += "\n"
                    else:
                        for k in range(Diagnol - 1):
                            CUBE += FILLER
            
        elif i == Length:
            for j in range(Length):
                CUBE += DOT
            for j in range(Diagnol - 1):
                CUBE += FILLER
            CUBE += DOTEND
        
        elif i > Length and i != Height:        # THE LEFT FACE BOTTOM EDGE
            gap = i - Length
            triangleSpace = Diagnol - gap - 1
            for j in range(gap):
                CUBE += VOID
            CUBE += DOT
            for j in range(triangleSpace):
                CUBE += FILLER
            CUBE += DOT
            for j in range(Length - triangleSpace - 3):
                CUBE += FILLER
            CUBE += DOT
            for j in range(triangleSpace):
                CUBE += FILLER
            CUBE += DOTEND                                                 
                
    print(CUBE)
             
def Filled_Cuboid(Length = 10.0,Width = 6.0, High = 4.0, FILLER = '  '):# Now we just adjust it for the three axies
    
    """
    It takes the length, width and height of the cuboid and the filler to be used to fill the cuboid
    
    :param Length: The length of the cuboid
    :param Width: The width of the cuboid
    :param High: The height of the cuboid
    :param FILLER: The filler for the cuboid, defaults to    (optional)
    """
    
    # THE HEIGHT AXIS HAS BEEN FIXED BUT CAN BE CHANGED 
    # DUE TO LOGICAL ISSUES, I AM NOT INTERESTED IN FIXING THE CODE
    # I WILL JUST ISSUE SOME CHEAT IN IT INSTEAD.
    # ANYWAYS THIS WILL BE IN THE EXPERIMENTAL OPTIONS 
    # SO NO NEED TO WORRY MUCH.
    
   # The code below is checking if the length is less than 2 and if it is, it will change the length
   # to 2.
   
    Length = int(fabs(Length))
    if Length < 2:
        print("Must have atleast two points to form a Cuboid. Therefore Changed to length 2.")
        Length = 2    
    
    FILLER = FILLER.upper()
    CUBE = ""
    VOID = '  '
    DOT = '* '
    DOTEND = DOT + '\n'  
    
    # The code below is generating a random number between 0 and 1. If the number is 0, the FILLER
    # variable is set to the first two characters of the FILLER variable. If the number is 1, the
    # FILLER variable is set to the first and last characters of the FILLER variable. If the length of
    # the FILLER variable is less than 2, the FILLER variable is set to two spaces.
    
    gen = random.randint(0, 1)
    if gen == 0:    
        FILLER = FILLER[:2]
    elif gen == 1:
        FILLER = FILLER[0] + FILLER[-1]
    if len(FILLER) < 2:
        FILLER = "  "
    
    Diagnol = int(floor(Width / 2.0)) # DIA = floor of 2.5 = 2.0 = 2
    
    h = 0                   # Mark if the height value was switched
    if High < Diagnol+1:
        h = 1
        High = Diagnol+1     # <------- THE CHEAT 
    elif High == Diagnol+1:
        h = 2
                
    Height = int(High + Diagnol)          # HEIGHT = 5 + 2 = 7  
    Length = int(Length)
    
    # The code below is creating a 3D cube with the given dimensions.
    
    for i in range(1,Height+1,1):
        
        if i == 1:                              # THE FIRST LINE
            for j in range(Length):
                CUBE += DOT
            CUBE += "\n"
    
        elif i == Diagnol+1:                    # THE FRONT TOP EDGE
            CUBE += DOT
            for j in range(Diagnol - 1):
                CUBE += FILLER
            for j in range(Length):
                CUBE += DOT
            CUBE += "\n"
                
        elif i == Height:                       # THE BOTTOM EDGE
            for j in range(Diagnol):
                CUBE += VOID
            for j in range(Length):
                CUBE += DOT
            CUBE += "\n"
        
        elif i < Diagnol+1 and i > 1:           # THE LEFT FACE TOP EDGE
            CUBE += DOT
            for j in range(i-2):
                CUBE += FILLER
            CUBE += DOT    
            for J in range(Length - 2):
                CUBE += FILLER
            CUBE += "* \n"
            
        elif i > Diagnol and i < High:      # THE MIDDLE Height EDGES
            CUBE += DOT
            for j in range(Diagnol - 1):
                CUBE += FILLER
            CUBE += DOT
            for J in range(Length - 2):
                CUBE += FILLER
            CUBE += "* \n"
        
        elif i > High and i != Height:        # THE LEFT FACE BOTTOM EDGE
            gap = int(i - High)
            for j in range(gap):
                CUBE += VOID
            CUBE += DOT
            for j in range(Diagnol - gap - 1):
                CUBE += FILLER
            CUBE += DOT
            for j in range(Length - 2):
                CUBE += FILLER
            CUBE += "* \n"                               
                
    print(CUBE)
    if h == 1:
        print("\"The given Height value does not imply with the Minimum Required!\"\n\"Therefore was modified to the Minimum ",Diagnol+1,".\"", sep = '') 

def Hollow_Cuboid(Length = 10.0,Width = 6.0, High = 4.0, FILLER = '  '): # We will use 5 as length here FOR TESTING
    
    """
    This function takes in the length, width, and height of a cuboid and prints out a hollow cuboid of
    the given dimensions.
    
    :param Length: The length of the cuboid
    :param Width: The width of the cuboid
    :param High: The height of the cuboid
    :param FILLER: This is the character that will be used to fill the cuboid, defaults to    (optional)
    """

    w = 0
    if Width >= 2*Length:
        w = 1
        Width = 2*Length - 1
        
    Diagnol = int(floor(Width / 2.0)) # DIA = floor of 2.5 = 2.0 = 2
    
    h = 0                   # Mark if the height value was switched
    if High < Diagnol+1:
        h = 1
        High = Diagnol+1     # <------- THE CHEAT 
    elif High == Diagnol+1:
        h = 2

    
        

    Length = int(fabs(Length))
    if Length < 2:
        print("Must have atleast two points to form a Cube. Therefore Changed to length 2.")
        Length = 2

    FILLER = FILLER.upper()

    CUBE = ""  
    VOID = '  '
    DOT = '* '
    DOTEND = DOT + '\n'  
    
    gen = random.randint(0, 1)
    if gen == 0:    
        FILLER = FILLER[:2]
    elif gen == 1:
        FILLER = FILLER[0] + FILLER[-1]
    if len(FILLER) < 2:
        FILLER = "  "

    Height = int(High + Diagnol)          # HEIGHT = 5 + 2 = 7  
    Length = int(Length)
    
    # The code below is creating a cube with the given dimensions.
    for i in range(1,Height+1,1):
        
        if i == 1:                              # THE FIRST LINE
            for j in range(Length):
                CUBE += DOT
            CUBE += "\n"
    
        elif i == Diagnol+1:                    # THE FRONT TOP EDGE
            if h == 0:
                CUBE += DOT
                for j in range(Diagnol - 1):
                    CUBE += FILLER
                for j in range(Length):
                    CUBE += DOT
                CUBE += "\n"
            elif h == 2 or h == 1:
                for j in range(Length + Diagnol):
                    CUBE += DOT
                CUBE += "\n"
                
        elif i == Height:                       # THE BOTTOM EDGE
            for j in range(Diagnol):
                CUBE += VOID
            for j in range(Length):
                CUBE += DOT
            CUBE += "\n"
        
        elif i < Diagnol+1 and i > 1:           # THE LEFT FACE TOP EDGE
            
            CUBE += DOT
            for j in range(i-2):
                CUBE += FILLER
            CUBE += DOT 
            midSpace = (Length-2) - (i-2) - 1
            for j in range(midSpace):
                CUBE += FILLER   
            CUBE += DOT
            for j in range(i-2):
                CUBE += FILLER
            CUBE += DOTEND

        elif i > Diagnol and i < High:      # THE MIDDLE Height EDGES
            
            CUBE += DOT
            for j in range(Diagnol - 1):
                CUBE += FILLER
            CUBE += DOT    
            for j in range(Length - Diagnol - 2):
                CUBE += FILLER
            CUBE += DOT
            for j in range(Diagnol - 1):
                CUBE += FILLER            
            CUBE += DOTEND
            
        elif i == High:
            for j in range(Length):
                CUBE += DOT
            for j in range(Diagnol - 1):
                CUBE += FILLER
            CUBE += DOTEND
        
        elif i > High and i != Height:        # THE LEFT FACE BOTTOM EDGE
            gap = int(i - High)
            triangleSpace = Diagnol - gap - 1
            for j in range(gap):
                CUBE += VOID
            CUBE += DOT
            for j in range(triangleSpace):
                CUBE += FILLER
            CUBE += DOT
            for j in range(Length - triangleSpace - 3):
                CUBE += FILLER
            CUBE += DOT
            for j in range(triangleSpace):
                CUBE += FILLER
            CUBE += DOTEND                                                 
                
    
    print(CUBE)

    # The code below is checking if the given values of width and height are equal to 1. If they are
    # equal to 1, then the code will print the message that the given values are not equal to the
    # minimum required.

    if h == 1 and w == 1:
        print("\"The given Width and Height value does not imply with the Minimum Required!\"\n\"Therefore were modified to the Minimum ",Width," and ",High,".\"", sep = '')
    
    elif h == 1 or w == 1:
        if h == 1:
            print("\"The given Height value does not imply with the Minimum Required!\"\n\"Therefore was modified to the Minimum ",High,".\"", sep = '') 
        if w == 1:
            print("\"The given Width value does not imply with the Minimum Required!\"\n\"Therefore was modified to the Minimum ",Width,".\"", sep = '')

