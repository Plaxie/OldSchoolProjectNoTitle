
# !IMPORTANT! BY : ADIL : XII-D:2110092 : YARA INTERNATIONAL SCHOOL : JUNE 2022-23
#
#    THIS MODULE CONTAINS ALL THE FUNCTIONS RELATED TO TwoDGs:
#                            i.e Two-Dimensional-Geometries.
#    ALL THE FUNCTIONS HAVE BEEN MADE FROM SCRATCH WITH NO TYPE OF PLAGERIZING INVOLVED.
#    THIS INCLUDES THE PRINT STATEMENTS AND ALL THE LOGIC USED. HENCE THERE MUST BE NO COMPLAINS
#    IN REGARDS TO THIS MODULE'S CREATION. EXCEPT FOR THE IN-BUILT MODULES


# THIS MODULE WILL HAVE MORE LOGICAL AND CUSTOMIZABLE SHAPES WITH MULTIPLE PARAMETERS

from math import fabs

FunctionsAvailable = ["Square","Rectangle","Triangle"]

def Square(Xside = 2,FillValue = False):
    
    """
    This function creates a square of a given size and fills it with a given value
    
    :param Xside: The length of the side of the square, defaults to 2 (optional)
    :param FillValue: If True, the square will be opaque. If False, the square will be hollow, defaults
    to False (optional)
    """
    
    Xside = int(round(fabs(Xside)))
    
    sqr = ""
    
    #Convert to int if not.
    x = Xside
     #Minimum value is 2
    if x < 2: x = 2
    
    #To create a hollow square
    if FillValue == False:
        
        for i in range(x):
            if i == 0 or i == x-1:
                sqr += "\n"
                
                for j in range (x):
                    sqr += "* "
            else:
                sqr += "\n"
                sqr += "* "
                
                for j in range (x-2):
                    sqr += "  "
                
                sqr += "* "
    
    #To create a opaque square
    else:
        for i in range(x):
                sqr += "\n"
                for j in range (x):
                    sqr += "* "
    #Prints the Created Square
    print(sqr)

def Rectangle(Xside = 3, Yside = 2,FillValue = False):
    
    """
    This function creates a rectangle with the given dimensions and fills it with the given value
    
    :param Xside: The length of the rectangle, defaults to 3 (optional)
    :param Yside: The height of the rectangle, defaults to 2 (optional)
    :param FillValue: If True, the rectangle will be filled with *'s. If False, the rectangle will be
    hollow, defaults to False (optional)
    """
    
    Xside = int(round(fabs(Xside)))
    Yside = int(round(fabs(Yside)))

    
    rect = ""
    
    #Convert to int if not.
    x = Xside
    y = Yside
     #Minimum value is 2
    if x < 2: x = 2; 
    elif y < 2: y = 2;
    
    #To create a hollow rectangle
    if FillValue == False:
        
        for i in range(x):
            if i == 0 or i == x-1:
                rect += "\n"
                
                for j in range (y):
                    rect += "* "
            else:
                rect += "\n"
                rect += "* "
                
                for j in range (y-2):
                    rect += "  "
                
                rect += "* "
    
    #To create a opaque rectangle
    else:
        for i in range(y):
                rect += "\n"
                for j in range (x):
                    rect += "* "
    #Prints the Created Rectangle
    print(rect)    

def Triangle(Xside = 3, _type = 'up', FillValue = False):
    
    """
    It takes in 3 arguments, the first one being the size of the triangle, the second one being the type
    of triangle, and the third one being whether or not the triangle is filled
    
    :param Xside: The length of the triangle, defaults to 3 (optional)
    :param _type: The type of triangle you want to draw, defaults to up (optional)
    :param FillValue: If True, the triangle will be filled with the character, defaults to False
    (optional)
    """
    
    Xside = int(round(fabs(Xside)))
    
    tri1 = ""
    
    #Convert to int if not.
    x = Xside
    #Minimum value is 3
    if x < 3: x = 3 
    
    if _type == 'tr':
        if FillValue == False:

            for i in range(x):
                if i == 0 or i == x-1:
                    tri1 += "\n* "

                    for j in range (i):
                        tri1 += "* "
                else:
                    tri1 += "\n* "

                    for j in range (i-1):
                        tri1 += "  "

                    tri1 += "* "
        else:
            for i in range(x):
                tri1 += "\n* "
                for j in range (i):
                    tri1 += "* "
    
    elif _type == 'dr':
        x -= 1
        
        if FillValue == False:

            for i in range(x,0,-1):
                if i == x:
                    tri1 += "\n"

                    for j in range (i):
                        tri1 += "* "
                    tri1 += "* "
                    
                else:
                    tri1 += "\n* "

                    for k in range (i-1):
                        tri1 += "  "

                    tri1 += "* "
            tri1 += "\n* "
            
        else:
            for i in range(x,0,-1):
                tri1 += "\n"
                for j in range(i):
                    tri1 += "* "
    
    elif _type == 'tl':

        if FillValue == False:
            
            for i in range (x,0,-1):
                
                
                tri1 += "\n  "
                for k in range (i):
                    tri1 += "  "


                if i == 1 or i == x:
                    for k in range((x+1)-i):
                        tri1 += "* "
                else:
                    tri1 += "* "
                    for k in range(int(fabs(i-(x-1)))):
                        tri1 += "  "
                    tri1 += "* "
    
        else:
            for i in range (x,0,-1):
                tri1 += "\n  "

                for k in range (i):
                    tri1 += "  "

                for j in range ((x+1)-i):
                    tri1 += "* "

    elif _type == 'dl':
        
        x -= 1
        spaceHAX = "" # WILL NEED LATER ON FOR REUSABILITY OF THE CODE FROM LAST FUNCTION.
        
        if FillValue == False:
            
            for i in range (x):
                
                tri1 += "\n  "
                for k in range (i):
                    tri1 += "  "
                    
                if i == 0 or i == x:
                    for k in range((x+1)-i):
                        tri1 += "* "
                else:
                    tri1 += "* "
                    for k in range(int(fabs(i-(x-1)))):
                        tri1 += "  "
                    tri1 += "* "
                tri1 +=""
            for X in range (x+1,0,-1):
                spaceHAX += "  "
            tri1 += "\n" + spaceHAX + "* "
  
        else:
            for i in range (0,x+1,1):
                tri1 += "\n  "

                for k in range (i):
                    tri1 += "  "

                for j in range ((x+1)-i):
                    tri1 += "* "
       
    elif _type == 'up':
        TRI = ''
        y = 0
        
        MIDSPC = ' '

        x = range(Xside,0,-1)       # 3,2,1

        for i in x: # 3,2,1
            
            SPC = ''
            DOT = '*'
            
            y += 1

            if i == Xside: # 3
                
                for j in range(i): #3 = 0,1,2 = 3 times
                    SPC += " "
                
                    if j == Xside-1:
                        TRI += (SPC + DOT + SPC + "\n") 
                        
            elif i == 1:
                
                    for k in range(1,2*Xside+2): # 1,2,3,4,5,6,7
                        
                        if k % 2 != 0:
                            TRI += " "
                            
                        elif k % 2 == 0:
                            TRI += DOT
                    TRI += "\n"
            else:
                    
                for j in range(i):
                    SPC += " "
                                            

                if y > 2:
                    if FillValue == False:MIDSPC += "  "
                    else:                 MIDSPC += "* "
                    
                TRI += (SPC + DOT + MIDSPC + DOT + SPC + "\n")
                
        tri1 = TRI          
        
    print(tri1)
