
# !IMPORTANT! BY : ADIL : XII-D:2110092 : YARA INTERNATIONAL SCHOOL : JUNE 2022-23
#
#    THIS MODULE CONTAINS ALL THE FUNCTIONS RELATED TO OneDGs:
#                            i.e One-Dimensional-Geometries.
#    ALL THE FUNCTIONS HAVE BEEN MADE FROM SCRATCH WITH NO TYPE OF PLAGERIZING INVOLVED.
#    THIS INCLUDES THE PRINT STATEMENTS AND ALL THE LOGIC USED. HENCE THERE MUST BE NO COMPLAINS
#    IN REGARDS TO THIS MODULE'S CREATION. EXCEPT FOR THE IN-BUILT MODULES


# THIS MODULE WILL HAVE LOGICAL AND CUSTOMIZABLE SHAPES WITH MULTIPLE PARAMETERS

from math import ceil, fabs, floor

FunctionsAvailable = [ "OneLine", "TwoLines"]

Type2 = ''

def OneLine(Direction = 'HORIZONTAL',Length = 2):
    
    """
    It takes two arguments, one for the direction of the line and the other for the length of the line
    
    :param Direction: The direction of the line, defaults to HORIZONTAL (optional)
    :param Length: The length of the line, defaults to 2 (optional)
    """
    
    # Fixing Values for evaluation.
    
    Direction = Direction.upper()
    Length = int(fabs(Length))
    
    # DECLARATIONS
    
    line = ''
    DOT = '* '
    VOID = '  '
    DOTEND = '* \n'

    # ERROR Provider For Invalid Length.
    
    if Length < 2:
        print("ERROR: Invalid length. For a line, There must be Two points to create it.")
        
    else:
        
        if Direction == 'HORIZONTAL':
            for i in range(Length):
                line += DOT

        if Direction == 'VERTICAL':
            for i in range(Length):
                line += DOTEND        
    
        if Direction == 'NE' or Direction == 'SW':
            for i in range(Length-1,-1,-1):
                for j in range(i):
                    line += VOID
                if i == 0:
                    line += DOT
                else:
                    line += DOTEND
         
        if Direction == 'NW'or Direction == 'SE':
            for i in range(Length):
                for j in range(i):
                    line += VOID
                if i == Length-1:
                    line += DOT
                else:
                    line += DOTEND      
                      
        print(line)
        

           
def TwoLines(Direction = 'HORIZONTAL',Length = 2,Sep = 3.0,Type = 'll'):
    
    """
    It takes in the direction, length, separation and type of 2 lines to be drawn and then prints the 2 lines
    
    :param Direction: The direction of the line, defaults to HORIZONTAL (optional)
    :param Length: The length of the line, defaults to 2 (optional)
    :param Sep: Separation between the two lines
    :param Type: This is the type of line you want to draw, defaults to ll (optional)
    """

    # Converting the input to the required format.
    
    Direction = Direction.upper()
    Type = Type.lower()
    Length = int(fabs(Length))
    Sep = fabs(Sep)
    
    DiagnolSep = int(floor(Sep/2))
    Sep = int(Sep)
    
    # DECLARATIONS
    
    lines = ''
    DOT = '* '
    VOID = '  '
    DOTEND = '* \n'
    
    # ERROR Provider For Invalid Length.
    
    if Length < 2:
        print("ERROR: Invalid length. For a line, There must be Two points to create it.")
        
    else:
        if Type == 'll' or Type == 'Parallel':
            
            # Printing the two lines in a horizontal manner.
            if Direction == 'HORIZONTAL':
                
                for i in range(Sep+2):
                    if i == 0:
                        for j in range(Length-1):
                            lines += DOT
                        lines += DOTEND
                    elif i == Sep+1:
                        for j in range(Length-1):
                            lines += DOT
                        lines += DOTEND
                    else:
                        lines += '\n'
            
            # Printing the two lines in a vertical manner.
            if Direction == 'VERTICAL':
                for i in range(Length):
                    lines += DOT
                    for j in range(Sep):
                        lines += VOID
                    lines += DOTEND
            
            # Printing the two lines in a NW or SE direction.
            if Direction == 'NW' or Direction == 'SE':
                TotalLoopLength = Length + DiagnolSep + 1
                for i in range(TotalLoopLength):
                    if i >= 0 and i < DiagnolSep + 1:
                        for j in range(i+1):
                            lines += VOID
                        for j in range(DiagnolSep):
                            lines += VOID
                        lines += DOTEND
                
                    elif i >= DiagnolSep + 1 and i < TotalLoopLength - DiagnolSep - 1:
                        for j in range(i-DiagnolSep-1):
                            lines += VOID
                        lines += DOT
                        if Sep%2 == 0:
                            for j in range(Sep+1):
                                lines += VOID
                            lines += DOTEND
                        else:
                            for j in range(Sep):
                                lines += VOID
                            lines += DOTEND
                        
                    elif i >= TotalLoopLength - DiagnolSep - 1:
                        for j in range(i - DiagnolSep - 1):
                            lines += VOID
                        lines += DOTEND
                        
            # This is the code for the two lines in the NE or SW direction.
            if Direction == 'NE' or Direction == 'SW':        
                TotalLoopLength = Length + DiagnolSep + 1
                for i in range(TotalLoopLength,-1,-1):
                    if i <= TotalLoopLength and i > TotalLoopLength - DiagnolSep - 1:
                        for j in range(i-DiagnolSep-2):
                            lines += VOID
                        lines += DOTEND
                    elif i <= TotalLoopLength - DiagnolSep - 1 and i > DiagnolSep + 1:
                        for j in range(i-DiagnolSep-2):
                            lines += VOID
                        lines += DOT
                        if Sep%2 == 0:
                            for j in range(Sep+1):
                                lines += VOID
                            lines += DOTEND
                        else:
                            for j in range(Sep):
                                lines += VOID
                            lines += DOTEND                        
                    elif i < DiagnolSep + 1:
                        for j in range(i + DiagnolSep + 1):
                            lines += VOID
                        lines += DOTEND                        
        print(lines)           