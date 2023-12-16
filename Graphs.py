
# !IMPORTANT! BY : ADIL : XII-D:2110092 : YARA INTERNATIONAL SCHOOL : JULY 2022-23
#
#    THIS MODULE CONTAINS ALL THE FUNCTIONS RELATED TO Graphs:

#    ALL THE FUNCTIONS HAVE BEEN MADE FROM SCRATCH WITH NO TYPE OF PLAGERIZING INVOLVED.
#    THIS INCLUDES THE PRINT STATEMENTS AND ALL THE LOGIC USED. HENCE THERE MUST BE NO COMPLAINS
#    IN REGARDS TO THIS MODULE'S CREATION. EXCEPT FOR THE IN-BUILT MODULES


# THIS MODULE WILL ALSO HAVE LOGICAL AND CUSTOMIZABLE GRAPH SIZES AND VARIANTS WITH MULTIPLE PARAMETERS.

# A list of all the functions available in this module.

FunctionsAvailable = ["NumberLine","XYGraph"]

from Extras import digitCounter

def NumberLine(Axis = 1,Dir = 'HORIZONTAL'):
    
    """
    It takes in two arguments, the first one is the number of units you want to plot on the number line,
    and the second one is the direction of the number line, either horizontal or vertical
    
    :param Axis: The number of units you want to plot, defaults to 1 (optional)
    :param Dir: Direction of the number line, defaults to HORIZONTAL (optional)
    """
    
    DOT = '*'
    STLine = '|'
    MidLine = 'i'
    VGrap = ''
    SLLine = '---'

    if Axis < 1 : Axis = 1;
    elif Axis > 98: Axis = 98; # Specifically A logical limitation.

    
    # Must be atleast 1 unit and less than 99 units

    # Now total length =>
    
    T_Axis = 2*Axis+1 

    VGrap += ' '
    
    # Generate the horizontal Line.
    if Dir == 'HORIZONTAL':
    
        for i in range(8*Axis+1):
            if i%4 == 0:
                VGrap += STLine
            elif i%2 == 0:
                VGrap += MidLine
            else:
                VGrap += DOT
        
        VGrap += '\n'
    
        # Generate The Coordinates.
    
        for i in range(Axis,0,-1):
            if digitCounter(i) == 1:
                VGrap += str(-i) + '  '
            elif digitCounter(i) == 2:
                VGrap += str(-i) + ' '

        VGrap += " 0   "

        for i in range(1,Axis+1):
            if digitCounter(i+1) == 1:
                VGrap += str(i) + '   '
            elif digitCounter(i+1) == 2:
                VGrap += str(i) + '  '
    
    VGrap = ''
    
    # Generate the Vertical Line.
    if Dir == 'VERTICAL':
        
        for i in range(2*Axis,0,-1):
            # -ve Part
            if i % 2 != 0:
                VGrap += ' ' + DOT + '\n'
            else:
                if digitCounter(i/2) == 2:
                    VGrap += SLLine + ' ' + str(int(-i/2)) + '\n'
                elif digitCounter(i/2) == 1:
                    VGrap += SLLine + '  ' + str(int(-i/2)) + '\n'
            
        for i in range(2*Axis+1):
            # +ve Part
            if i % 2 != 0:
                VGrap += ' ' + DOT + '\n'
            else:
                if i == 0:
                    VGrap += SLLine + '   ' + str(int(i)) + '\n'
                if digitCounter(i/2) == 2:
                    VGrap += SLLine + '   ' + str(int(i/2)) + '\n'
                elif digitCounter(i/2) == 1:
                    VGrap += SLLine + '   ' + str(int(i/2)) + '\n'
                 
            
    
    print(VGrap)    


def XYGraph(Xaxis = 3,Yaxis = 3,Shift = 3,LineX = ' * ',LineY = '*',unitLength = 1):
    
    """
    It takes in the X and Y axis length, the shift, the line character, the unit length and prints out a
    graph
    
    :param Xaxis: The number of units on the X-axis, defaults to 3 (optional)
    :param Yaxis: The number of units on the Y-axis, defaults to 3 (optional)
    :param Shift: The number of spaces to shift the graph, defaults to 3 (optional)
    :param LineX: The line that is drawn in the middle of the graph, defaults to  *  (optional)
    :param LineY: The character that is used to draw the X-axis, defaults to * (optional)
    :param unitLength: The length of the unit, defaults to 1 (optional)
    """
    
    # Declared a few variables
    
    DOT = '*'
    VGrap = ''
    ENDSpace = '\n '
    ShiftGraph = ''
    ValueChanged = False
    
    # Generate the shifted void.
    
    for j in range(Shift):
        ShiftGraph += ' '

    if Xaxis < 1 : Xaxis = 1;
    elif Xaxis > 98: Xaxis = 98;  # Specifically A logical limitation.

    if Yaxis < 1 : Yaxis = 1;
    elif Yaxis > 98: Yaxis = 98; 

    if unitLength * Xaxis > 98: 
        unitLength = 98//Xaxis
        ValueChanged = True
    if unitLength * Yaxis > 98: 
        unitLength = 98//Yaxis
        ValueChanged = True
        
    
    # Must be atleast 1 unit and less than 99 units

    # Now total length =>
    
    T_Xaxis = 2*Xaxis+1 

    for j in range(5): # This divids it into multiple sections.
        
        # part 0: the X-axis Co-ordinates
        if j == 0:
            VGrap += ShiftGraph
            
            # Generate The Co-ordinates.
            for i in range(Xaxis,0,-1):
                if digitCounter(unitLength*i) == 1:
                    VGrap += str(unitLength*-i) + '  '
                elif digitCounter(unitLength*i) == 2:
                    VGrap += str(unitLength*-i) + ' '

            VGrap += " 0   "

            for i in range(1,Xaxis+1):
                if digitCounter(unitLength*i+1) == 1:
                    VGrap += str(unitLength*i) + '   '
                elif digitCounter(unitLength*i+1) == 2:
                    VGrap += str(unitLength*i) + '  '
            VGrap += ENDSpace

        # part 1: the +ve Y axis
        if j == 1:
            
            for i in range(Yaxis,0,-1):
                VGrap += ENDSpace
                VGrap += ShiftGraph
                for k in range(2*Xaxis+1):
                    if k == 2*Xaxis:
                        if digitCounter(unitLength*i) == 1:
                            VGrap += DOT + '   ' + str(unitLength*i)
                        elif digitCounter(unitLength*i+1) == 2:
                            VGrap += DOT + '  ' + str(unitLength*i)
                    
                    # If in any case want to change the mid sign
                    elif k == Xaxis-1:
                        VGrap += DOT + '  ' 
                    elif k == Xaxis:
                        VGrap += LineX + '  ' # <-- Modify the first string to change the mid sign
                        
                        
                    else:
                        VGrap += DOT + '   '
                VGrap += ENDSpace
                VGrap += ShiftGraph
                for k in range(Xaxis):
                    VGrap += '    '
                VGrap += '*'
            VGrap += ENDSpace
        
        # part 2: the X axis number line.
        if j == 2:
            VGrap += ShiftGraph
            
            # Generate the Line.
    
            for i in range(8*Xaxis+1):
                if i == 4*Xaxis:
                    VGrap += '0'
                elif i%4 == 0:
                    VGrap += LineY # <-- Can modify DOT to any one character
                elif i%2 != 0:
                    VGrap += ' '
                else:
                    VGrap += DOT
            VGrap += '   ' +  str(0) + '\n'
        
        # part 3: the -ve Y axis
        if j == 3:
            VGrap += ShiftGraph
            for i in range(Xaxis):
                VGrap += '    '
            VGrap += ' *'            
            for i in range(1,Yaxis+1):
                VGrap += ENDSpace
                VGrap += ShiftGraph
                for k in range(2*Xaxis+1):
                    if k == 2*Xaxis:
                        if digitCounter(unitLength*i) == 1:
                            VGrap += DOT + '   ' + str(unitLength*i)
                        elif digitCounter(unitLength*i+1) == 2:
                            VGrap += DOT + '  ' + str(unitLength*i)
                    
                    # If in any case want to change the mid sign
                    elif k == Xaxis-1:
                        VGrap += DOT + '  ' 
                    elif k == Xaxis:
                        VGrap += LineX + '  ' # <-- Modify LineX to change the mid sign
                        
                        
                    else:
                        VGrap += DOT + '   '
                if i != Yaxis: 
                    VGrap += ENDSpace
                    VGrap += ShiftGraph
                    for k in range(Xaxis):
                        VGrap += '    '
                    VGrap += '*'
            VGrap += ENDSpace
                            
    
    print(VGrap)
    if ValueChanged:
        print("Given Value of unit Size Was\nLarger than the Limit created\nAnd hence was adjusted accordingly.\n")    

   