# THIS MODULE IS SOLELY USED BY THE DEVELOPER(S) OF THIS MODULE PACK.

from Extras import ReadFileReplaceByte

page_paths = ["Pages\HELP\Introductory_Page.txt",
              "Pages\HELP\MODULES.txt",
              "Pages\Main\Special_Options\ExpOFF.txt",
              "Pages\Main\Special_Options\ExpON.txt",
              "Pages\Main\ThreeDG\_Cubes.txt",
              "Pages\Main\ThreeDG\_Cuboids.txt",
              "Pages\Main\ThreeDG\Opt3DGs.txt",
              "Pages\Main\TwoDG\_Rectangle.txt",
              "Pages\Main\TwoDG\_Square.txt",
              "Pages\Main\TwoDG\_Triangle.txt", 
              "Pages\Main\TwoDG\Opt2DGs.txt",
              "Pages\Main\Arithemetic.txt",
              "Pages\Main\Credits.txt",
              "Pages\Main\Exit The Program.txt",
              "Pages\Main\Main Page.txt",
              "Pages\Main\Shapes Or Arithemetic.txt",
              "Pages\Main\Shapes.txt",
              "Pages\Main\Special_Options_EGGS.txt",
              "Pages\Main\Special_Options.txt",
              "Pages\Main\Arithemetic\SimpleCalc.txt",
              "Pages\Main\Arithemetic\Robust Calculator.txt",
              "Pages\Main\Arithemetic\Matrices\Matrices.txt",
              "Pages\Main\Arithemetic\Matrices\Modify_M.txt"]

def UpdateVersion(Version):
    """
    It takes a version number as a string, and then it updates the version number in the file
    
    :param Version: The version number to update to
    """
    string = str(Version)

    for FilePath in page_paths:
        for index in range(len(string)):
            ReadFileReplaceByte(FilePath, (22,10+(index+1)),string[index])

UpdateVersion("1.11c")
    