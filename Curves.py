
# !IMPORTANT! BY : ADIL : XII-D:2110092 : YARA INTERNATIONAL SCHOOL : JUNE 2022-23
#
#    THIS MODULE CONTAINS ALL THE FUNCTIONS RELATED TO Curves:
#                        i.e Curved Structures:
#    ALL THE FUNCTIONS HAVE BEEN MADE FROM SCRATCH WITH NO TYPE OF PLAGERIZING INVOLVED.
#    THIS INCLUDES THE PRINT STATEMENTS AND ALL THE LOGIC USED. HENCE THERE MUST BE NO COMPLAINS
#    IN REGARDS TO THIS MODULE'S CREATION. EXCEPT FOR THE IN-BUILT MODULES

from math import ceil; from Extras import stringRepeater

# A list of all the functions available in this module.
FunctionsAvailable = ["up_regular_parabola", "down_regular_parabola", "left_regular_parabola", "right_regular_parabola",
                      "circle", "up_semi_circle", "down_semi_circle", "UD_regular_hyperbola", "RL_regular_hyperbola",
                      "Custom_parabola_D1"]


def up_regular_parabola():
    #Prints a 'U' type Parabola.
    print("*                          *")
    print(" *                        * ")
    print("  **                   **   ")
    print("    **               **     ")
    print("       ***       ***        ")
    print("           *****            ")

def down_regular_parabola():
    #Prints an 'A' type Parabola.
    print("           *****            ")
    print("       ***       ***        ")
    print("    **               **     ")
    print("  **                   **   ")
    print(" *                        * ")
    print("*                          *")

def left_regular_parabola():
    #Prints a '>' type Parabola.
    print("*          ")
    print("    *      ")
    print("      *    ")
    print("        *  ")
    print("         * ")
    print("          *")
    print("          *")
    print("          *")
    print("         * ")
    print("        *  ")
    print("      *    ")
    print("    *      ")
    print("*          ")
    
def right_regular_parabola():
    #Prints a '<' type Parabola.
    print("          *")
    print("      *    ")
    print("    *      ")
    print("  *        ")
    print(" *         ")
    print("*          ")
    print("*          ")
    print("*          ")
    print(" *         ")
    print("  *        ")
    print("    *      ")
    print("      *    ")
    print("          *")
    
def circle():
    #Prints a Circle.
    print("       * * *       ")
    print("   *           *   ")
    print(" *               * ")
    print("*                 *")
    print("*                 *")
    print("*                 *")
    print(" *               * ")
    print("   *           *   ")
    print("       * * *       ")
    
def up_semi_circle(): 
    #Prints a Semi-Circle with it's top closed.
    print("*  *  *  *  *  *  *") 
    print("*                 *")
    print(" *               * ")
    print("   *           *   ")
    print("       * * *       ")

def down_semi_circle():
    #Prints a Semi-Circle with it's bottom closed.
    print("       * * *       ")
    print("   *           *   ")
    print(" *               * ")
    print("*                 *")
    print("*  *  *  *  *  *  *") 
    
def UD_regular_hyperbola(gap = 0.0):
    x = int(round(gap)) #Confirms the gap variable is an integer.
    
    #Prints the First Half of the Hyperbola.
    print("    *                     *      ")
    print("     *                   *       ")
    print("       *               *         ")
    print("         ***       ***           ")
    print("             *****               ")
    
    #Verfiying the limits of the gap, now x variable.
    if x < 0:x = 0
    elif x > 7:x = 7
    
    #Printing the gap between the Hyperbola.
    for i in range (x):
        print()
    
    #Prints the rest of the Hyperbola
    print("             *****               ")
    print("         ***       ***           ")
    print("       *               *         ")
    print("     *                   *       ")
    print("    *                     *      ")
    
def RL_regular_hyperbola(_gap = 0.0):
    Tgap = ""
    y = int(round(_gap)) #Confirms the _gap variable is an integer.

    #Verfiying the limits of the _gap, now y variable.
    if y < 0: y = 0
    elif y > 7: y = 7
    
    #Calculating the _gap between the Hyperbola.
    for j in range(y):
        Tgap += " "
        
    #Prints 'all' of the Hyperbola together.
    print("*          " + Tgap + "          *  ")
    print("    *      " + Tgap + "      *      ")
    print("       *   " + Tgap + "   *         ")
    print("         * " + Tgap + " *           ")
    print("          *" + Tgap + "*            ")
    print("          *" + Tgap + "*            ")
    print("          *" + Tgap + "*            ")
    print("         * " + Tgap + " *           ")
    print("       *   " + Tgap + "   *         ")
    print("    *      " + Tgap + "      *      ")
    print("*          " + Tgap + "          *  ")




# IF THE INVIGILATOR IS MORE INTERESTED IN PURE CODED PARABOLIC FUNCTIONS ...
# THEN YOU SHALL CONTINUE BUT BE WARNED THEY MAY NOT BE PRACTICALLY PARABOLAS.


# !NOTE!
#
#    ALL THE REGULAR FUNCTIONS (RATHER SIMPLE) HAVE BEEN DONE.
#    FROM THIS POINT ONWARDS IT IS ALL EXPERIMENTAL.
#    THEY MAY OR MAY NOT WORK PROPERLY.
#    PROCEED WITH CAUTION.

# !SECOND NOTE! 
#
#    ALL OF THE AFOREMENTIONED AND BELOW PRESENT CODE HAS BEEN WRITTEN WITHOUT THE
#    PRESENCE OF INTERNET. SINCE IT WAS OUT OF REACH AT THE MOMENT
#    THEREFORE COULD NOT SEARCH UP A PROPER PARABOLIC FUNCTION


# FUNCTION USED : x^3 + 2x^2 -5x - 6 : Can be changed

def Generate_Curve(size = 3, detail = 1,degree = 0):
    
    """
    It takes a function, and plots it on a graph.
    
    :param size: The size of the graph, defaults to 3 (optional)
    :param detail: The amount of points on the x-axis, defaults to 1 (optional)
    :param degree: The degree of the polynomial, defaults to 0 (optional)
    """
    
    # Define style:
    
    DOT = "0"
    VOID = " "
    LINE = "|"
    
    if size <3: size = 3
    if detail < 1: detail == 1
    size += 1
    
    points = {0} # A set of unique x values
    
    # Generate a list of both negative and positive values:
    for number in range(size*detail):
        points.add(-number/detail); points.add(number/detail)
    
    points = list(points)
    points.sort()
    points = tuple(points)

    ### FUNCTIONS THAT CAN BE CHANGED ###

    def _0D_Function(x):
        return int(round(x**0))
    
    def _1D_Function(x):
        return int(round(x*10))
    
    def _2D_Function(x):
        return int(round(2*(x**2) - 10))
    
    def _3D_Function(x):
        return int(round((x**3) + (2*(x**2)) - (5*x) - 6))
    
    def _4D_Function(x):
        return int(round((x**4)/2 + (x**3)/2 - 9*(x**2) + x + 13))
    
    #####################################
    
    
    def difference(x,y):
        
        res = int(x - y)
        return res
    
    def CheckForMaximum(Function):
        
        """
        "CheckForMaximum" is a function that takes a function as an argument, and returns the maximum value
        of that function.
        
        :param Function: The function you want to find the maximum of
        :return: The maximum value of the function.
        """
        
        Maximum = 0
        for x in points:
            constant = Function(x)
            if constant > Maximum: Maximum = constant
        return Maximum
            
    def CheckForMinimum(Function):
        
        """
        "CheckForMinimum" takes a function as an argument, and returns the minimum value of that function
        over the range of points.
        
        :param Function: The function you want to find the minimum of
        :return: The minimum value of the function.
        """
        
        Minimum = 0
        for x in points:
            constant = Function(x)
            if constant < Minimum: Minimum = constant
        return Minimum

    
    def Curve(Function):
        """
        It takes a function and plots it on the terminal
    
        :param Function: The function you want to graph
        """
    
        MAX = CheckForMaximum(Function)
        MIN = CheckForMinimum(Function)
        
        for point in points:
            coord = Function(point)
            if coord < 0:
                first_gap = difference(coord, MIN)
                second_gap = -difference(MIN, -first_gap)
                
                third_gap = difference(MAX,first_gap)
                
                
                _ = stringRepeater(first_gap, VOID)
                __ = stringRepeater(second_gap-1, VOID)
                ___ = stringRepeater(third_gap, VOID)
                

                print(_ + DOT + __ + LINE + ___)
            elif coord == 0:
                first_gap = difference(coord, MIN)
                second_gap = -difference(MIN, -first_gap)
                
                third_gap = difference(MAX,first_gap)
                
                
                _ = stringRepeater(first_gap, VOID)
                __ = stringRepeater(second_gap, VOID)
                ___ = stringRepeater(third_gap, VOID)
                

                print(_ + DOT + __)

            else:
                first_gap = difference(coord, MIN)
                mid_gap = first_gap + MIN
                third_gap = difference(MAX,first_gap)
                
                
                _ = stringRepeater(-MIN, VOID)
                __ = stringRepeater(mid_gap-1, VOID)
                ___ = stringRepeater(third_gap, VOID)
                

                print(_ + LINE + __ + DOT + ___)
    if degree == 0:
        Curve(_0D_Function)
    elif degree == 1:
        Curve(_1D_Function)
    elif degree == 2:
        Curve(_2D_Function)
    elif degree == 3:
        Curve(_3D_Function)
    elif degree == 4:
        Curve(_4D_Function)
    else:
        print("ERROR: Degree is undefined!")


#Generate_Curve(3,4,3)
