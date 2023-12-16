
# !IMPORTANT! BY : ADIL : XII-D:2110092 : YARA INTERNATIONAL SCHOOL : AUGUST 2022-23
#
#    THIS MODULE CONTAINS ALL THE FUNCTIONS RELATED TO Coordinated_matrixs:

#    ALL THE FUNCTIONS HAVE BEEN MADE FROM SCRATCH WITH NO TYPE OF PLAGERIZING INVOLVED.
#    THIS INCLUDES THE PRINT STATEMENTS AND ALL THE LOGIC USED. HENCE THERE MUST BE NO COMPLAINS
#    IN REGARDS TO THIS MODULE'S CREATION. EXCEPT FOR THE IN-BUILT MODULES


#   THIS MODULE WILL BE A FULLY FUNCTIONING BASE FOR MATRICES AND MAYBE IN THE FUTURE, DETERMINENTS

from random import randint; import Extras

# Matrix is a class that represents a matrix.

# It's a class that can be used to create a matrix object, and perform matrix operations on it
class Matrix():
    
    # some constants
    
    start_index = 0
    
    # attributes
    rows = 0
    columns = 0
    Coordinated_matrix = []
    matrix = []
    unity = False
    
    # dunder methods:
    
    def __init__(self, rows = 0, columns = 0, unity = False):
        
        """
        The function takes in three arguments, rows, columns, and unity. It sets the properties of the
        matrix, and then checks to see if the rows or columns are zero. If they are, it prints a
        message. It then sets the matrix to all zeros
        
        :param rows: The number of rows in the matrix, defaults to 0 (optional)
        :param columns: The number of columns in the matrix, defaults to 0 (optional)
        :param unity: If true, the matrix will be initialized as an identity matrix, defaults to False
        (optional)
        """
        
        self.set_prop(rows,columns)
        self.unity = unity
        if self.rows == 0 or self.columns == 0:
            print("The matrix has undefined rows or columns!")
        self.set_int(0)
        
    def __len__(self):
        
        """
        The function __len__() returns the number of elements in the list
        """
        
        self.size()
        
    def __call__(self):
        
        """
        It prints the matrix in a nice format
        """
        
        border = "|"
        gap = ""
        checkl = 0; _gap = 3
        
        for row in self.matrix:
            
            for item in row:
                if len(str(item)) > checkl:
                    checkl = len(str(item))
        
        for row in self.matrix:
            
            print(border, Extras.stringRepeater(_gap," "), end= "", sep = "")
            for item in row:
                gap = Extras.stringRepeater(checkl + _gap - len(str(item))," ")
                print(item, end= gap)
            print(border)
        
        print()
    
    def __int__(self):
        
        """
        This function takes a matrix and converts all of its elements to integers
        :return: The matrix is being returned.
        """
        
        row_index = 0
        for row in self.matrix:
            item_index = 0
            for item in row:
                self.matrix[row_index][item_index] = int(round(item))
        return self
        
                
       
    # arithemetic operator methods   
    
    def __add__(self, other):
        """
        It takes two matrices, adds them together, and returns the result
        
        :param other: The other matrix to add to this one
        :return: A new matrix object is being returned.
        """
        catched_matrix = []
        
        for row in range(self.rows):
            catched_general_data = []
            
            for item in range(self.columns):
                catched_general_data.append(self.matrix[row][item] + other.matrix[row][item])
            catched_matrix.append(catched_general_data)
        
        index0 = self.start_index
        catched_Coordinated_matrix = []
        
        for row in catched_matrix:
            
            index1 = self.start_index
            catched_data = []
            
            for item in row:
                        
                try: item =  float(item)
                except ValueError:pass

                try: item = int(item)
                except ValueError:pass
                        
                        
                catched_data.append([(index0,index1),(item)])
                index1 += 1
                
            catched_Coordinated_matrix.append(catched_data)
            index0 += 1
            
        ResultantM = Matrix(self.rows,self.columns);
        ResultantM.matrix = catched_matrix
        ResultantM.Coordinated_matrix = catched_Coordinated_matrix
        
        return ResultantM

    def __sub__(self, other):
        
        """
        It takes the difference of two matrices and returns the resultant matrix
        
        :param other: The other matrix to be subtracted from the current matrix
        :return: A new matrix object is being returned.
        """
        
        catched_matrix = []
        
        for row in range(self.rows):
            catched_general_data = []
            
            for item in range(self.columns):
                catched_general_data.append(self.matrix[row][item] - other.matrix[row][item])
            catched_matrix.append(catched_general_data)
        
        index0 = self.start_index
        catched_Coordinated_matrix = []
        
        for row in catched_matrix:
            
            index1 = self.start_index
            catched_data = []
            
            for item in row:
                        
                try: item =  float(item)
                except ValueError:pass

                try: item = int(item)
                except ValueError:pass
                        
                        
                catched_data.append([(index0,index1),(item)])
                index1 += 1
                
            catched_Coordinated_matrix.append(catched_data)
            index0 += 1
            
        ResultantM = Matrix(self.rows,self.columns);
        ResultantM.matrix = catched_matrix
        ResultantM.Coordinated_matrix = catched_Coordinated_matrix
        
        return ResultantM        

    def __mul__(self, other):
        
        """
        The function takes two matrices and multiplies them together
        
        :param other: The other matrix to be multiplied with
        :return: The resultant matrix is being returned.
        """
        
        if self.columns == other.rows:
            catched_matrix = []

            for row in range(self.rows):
                catched_general_data = []
                add = 0
                for columns in range(other.columns):
                    add = 0
                    for index in range(self.columns):

                        add += self.matrix[row][index]*other.matrix[index][columns]
                    catched_general_data.append(add)
                catched_matrix.append(catched_general_data)

            index0 = self.start_index
            catched_Coordinated_matrix = []

            for row in catched_matrix:

                index1 = self.start_index
                catched_data = []

                for item in row:
  
                    try: item =  float(item)
                    except ValueError:pass

                    try: item = int(item)
                    except ValueError:pass


                    catched_data.append([(index0,index1),(item)])
                    index1 += 1

                catched_Coordinated_matrix.append(catched_data)
                index0 += 1

            ResultantM = Matrix(self.rows,self.columns);
            ResultantM.matrix = catched_matrix
            ResultantM.Coordinated_matrix = catched_Coordinated_matrix

            return ResultantM


        else:
            print("ERROR: Given Matrices are Incompatible for Multiplication!\n        Columns of the First ; Don't match with the Rows of the Second")

    def mul(self, constant):
        
        """
        It multiplies the matrix by a constant.
        
        :param constant: The constant to multiply the matrix by
        :return: A matrix object.
        """
        
        catched_matrix = []

        for row in range(self.rows):
            catched_general_data = []

            for columns in range(self.columns):

                catched_general_data.append(self.matrix[row][columns]*constant)

            catched_matrix.append(catched_general_data)

        index0 = self.start_index
        catched_Coordinated_matrix = []

        for row in catched_matrix:

            index1 = self.start_index
            catched_data = []

            for item in row:
                
                try: item =  float(item)
                except ValueError:pass
                
                try: item = int(item)
                except ValueError:pass


                catched_data.append([(index0,index1),(item)])
                index1 += 1

            catched_Coordinated_matrix.append(catched_data)
            index0 += 1

        ResultantM = Matrix(self.rows,self.columns);
        ResultantM.matrix = catched_matrix
        ResultantM.unity = False
        ResultantM.Coordinated_matrix = catched_Coordinated_matrix

        return ResultantM


    # Comparision Methods:
    
    def __eq__(self, other):
        
        """
        It sums up all the values in the matrix and compares them to the sum of the values in the other
        matrix
        
        :param other: The other matrix to compare to
        :return: The sum of all the values in the matrix.
        """
        
        catched_self_value = 0
        for row in self.matrix:
            for item in row:
                catched_self_value += item
        
        catched_other_value = 0
        for row in other.matrix:
            for item in row:
                catched_other_value += item
        
        if catched_self_value == catched_other_value: return True
        else: return False
    
    def __ne__(self, other):
        
        """
        It sums up all the values in the matrix and compares them.
        
        :param other: The other matrix to compare to
        :return: True or False
        """
        
        catched_self_value = 0
        for row in self.matrix:
            for item in row:
                catched_self_value += item
        
        catched_other_value = 0
        for row in other.matrix:
            for item in row:
                catched_other_value += item
        
        if catched_self_value != catched_other_value: return True
        else: return False

    def __lt__(self, other):
        
        """
        It compares the sum of all elements in the matrix of the object that calls the function with the
        sum of all elements in the matrix of the object that is passed as an argument.
        
        :param other: The other matrix to compare to
        :return: The sum of all the values in the matrix.
        """
        
        catched_self_value = 0
        for row in self.matrix:
            for item in row:
                catched_self_value += item
        
        catched_other_value = 0
        for row in other.matrix:
            for item in row:
                catched_other_value += item
        
        if catched_self_value < catched_other_value: return True
        else: return False
    
    def __gt__(self, other):
        
        """
        It takes the sum of all the values in the matrix and compares them to the sum of all the values
        in the other matrix
        
        :param other: The other matrix to compare to
        :return: True or False
        """
        
        catched_self_value = 0
        for row in self.matrix:
            for item in row:
                catched_self_value += item
        
        catched_other_value = 0
        for row in other.matrix:
            for item in row:
                catched_other_value += item
        
        if catched_self_value > catched_other_value: return True
        else: return False
    
    def __le__(self, other):
        
        """
        The function takes two matrices as arguments and returns True if the sum of the first matrix is
        less than or equal to the sum of the second matrix
        
        :param other: The other matrix to compare to
        :return: True or False
        """
        
        catched_self_value = 0
        for row in self.matrix:
            for item in row:
                catched_self_value += item
        
        catched_other_value = 0
        for row in other.matrix:
            for item in row:
                catched_other_value += item
        
        if catched_self_value <= catched_other_value: return True
        else: return False
    
    def __ge__(self, other):
        
        """
        It takes the sum of all the values in the matrix, and compares them to the sum of all the values
        in the other matrix
        
        :param other: The other matrix to compare to
        :return: True or False
        """
        
        catched_self_value = 0
        for row in self.matrix:
            for item in row:
                catched_self_value += item
        
        catched_other_value = 0
        for row in other.matrix:
            for item in row:
                catched_other_value += item
        
        if catched_self_value >= catched_other_value: return True
        else: return False
    
        
    

    # other methods


    def load_data(self, csvfile, deli):
        
        """
        It takes a csv file and converts it into a Coordinated_matrix
        
        :param csvfile: The file to be loaded
        :param deli: The delimiter used in the csv file
        
        """
        
        from csv import reader
        catched_Coordinated_matrix = []; error = False
        with open(csvfile,"r") as File:

            Records = reader(File, delimiter = deli)
            index0 = self.start_index
            
            for data in Records:
                # Verify the data size prescribed:
                if len(data) != self.columns:
                    print("Incompatible Data Size")
                    error = True
                    break
                else:
                    index1 = self.start_index
                    catched_data = []
                    for item in data:
                        
                        try: item =  float(item)
                        except ValueError:pass

                        try: item = int(item)
                        except ValueError:pass
                        
                        
                        catched_data.append([(index0,index1),(item)])
                        index1 += 1
                        
                catched_Coordinated_matrix.append(catched_data)
                index0 += 1
                
            # Verify the file size prescribed:
            if len(catched_Coordinated_matrix) != self.rows and error == False:
                print("Incompatible File Size")
            else: self.Coordinated_matrix = catched_Coordinated_matrix
            
            File.close()

        # Generate the general viewing Coordinated_matrix
        self.generate_general()
    
    
    
    
    def input_items(self):
        
        """
        The function takes the user input and stores it in a list of lists
        """
        
        self.Coordinated_matrix = []
        for row in range(1,self.rows+1):
            row_list = [] # refresh the row_List for every row.

            for column in range(1,self.columns+1):
                
                data = input(f"[M] Enter the Data for ID [{row},{column}] : ")
                
                try: data =  float(data)
                except ValueError:pass
                
                try: data = int(data)
                except ValueError:pass
                
                row_list.append([(row,column),(data)]) # add column data for the rows.
            self.Coordinated_matrix.append(row_list)
        
        # Generate the general viewing Coordinated_matrix
        self.generate_general()

    def set_prop(self, rows, columns):
        
        """
        > The function `set_prop` takes two arguments, `rows` and `columns`, and sets the object's `rows`
        and `columns` properties to those values
        
        :param rows: The number of rows in the grid
        :param columns: The number of columns in the grid
        """
        
        self.rows = rows; self.columns = columns
    
    def get_prop(self):
        
        """
        The function takes in a matrix object and returns a string with the number of rows and columns
        in the matrix
        :return: The number of rows and columns in the matrix.
        """
        
        return f"Rows    : {self.rows}\nColumns : {self.columns}"
    
    def size(self):
        """
        It returns the number of elements in the matrix.
        :return: The number of rows times the number of columns.
        """
        return self.rows * self.columns

    
    def coordinated(self):
        
        """
        It takes the Coordinated_matrix and prints it out in a nice format
        """
        
        border = "|"
        gap = ""
        checkl = 0; _gap = 3
        
        # Check for the longest item print.
        for row in self.Coordinated_matrix:
            
            for item in row:
                if len(str(item)) > checkl:
                    checkl = len(str(item))

        
        # Display the beautified Coordinated_matrix representation:
        for row in self.Coordinated_matrix:
            
            print(border, Extras.stringRepeater(_gap," "), end= "", sep = "")
            for item in row:
                gap = Extras.stringRepeater(checkl + _gap - len(str(item))," ")
                print(item, end= gap)
            print(border)
 
    def set_rand(self,_type,variable_size = 10000):
        
        """
        The function takes in a type of data and a variable size, and then generates a random matrix of
        that type and size
        
        :param _type: The type of data you want to generate
        :param variable_size: This is the maximum value that the random number can be, defaults to 10000
        (optional)
        """
        
        _type = _type.lower()
        self.Coordinated_matrix = []
        for row in range(self.start_index,self.rows+self.start_index):
            row_list = [] # refresh the row_List for every row.

            for column in range(self.start_index,self.columns+self.start_index):
                
                if _type == "integer" or _type == "int":
                    data = randint(0,variable_size)
                
                if _type == "float":
                    from random import random
                    data = random()*randint(0,variable_size)
                
                if _type == "bytes" or _type == "b":
                    from random import randbytes
                    data = randbytes(1)
                
                row_list.append([(row,column),(data)]) # add column data for the rows.
            self.Coordinated_matrix.append(row_list)
        
        # Generate the general viewing Coordinated_matrix
        self.generate_general()
    
    def set_int(self, constant):
        
        """
        It takes a constant and creates a matrix of that constant
        
        :param constant: The constant value to be set for the matrix
        """
        
        self.unity = True
        
        self.Coordinated_matrix = []
        
        for row in range(self.start_index,self.rows+self.start_index):
            row_list = [] # refresh the row_List for every row.

            for column in range(self.start_index,self.columns+self.start_index):
                
                data = constant
                
                row_list.append([(row,column),(data)]) # add column data for the rows.
            self.Coordinated_matrix.append(row_list)
        
        # Generate the general viewing Coordinated_matrix
        self.generate_general()

    def set_diagnol(self, constant):
        
        """
        It takes a constant and sets the diagnol of the matrix to that constant
        
        :param constant: The constant value you want to set the diagnol to
        """
        
        if self.rows == self.columns:
        
            self.Coordinated_matrix = []
            
            for row in range(self.start_index,self.rows+self.start_index):
                row_list = [] # refresh the row_List for every row.

                for column in range(self.start_index,self.columns+self.start_index):
                    if column == row:
                        data = constant
                    else:
                        data = 0
                    
                    row_list.append([(row,column),(data)]) # add column data for the rows.
                self.Coordinated_matrix.append(row_list)
            
            # Generate the general viewing Coordinated_matrix
            self.generate_general()
        
        else:
            print("ERROR: Not a Square Matrix!")
    
    def set_identity(self):
        
        """
        It takes the rows and columns of the matrix and creates a new matrix with the same dimensions,
        but with 1's on the diagonal and 0's everywhere else
        """
        
        if self.rows == self.columns:
        
            self.Coordinated_matrix = []
            
            for row in range(self.start_index,self.rows+self.start_index):
                row_list = [] # refresh the row_List for every row.

                for column in range(self.start_index,self.columns+self.start_index):
                    if column == row:
                        data = 1
                    else:
                        data = 0
                    
                    row_list.append([(row,column),(data)]) # add column data for the rows.
                self.Coordinated_matrix.append(row_list)
            
            # Generate the general viewing Coordinated_matrix
            self.generate_general()
        
        else:
            print("ERROR: Not a Square Matrix!")
    
    def update_item(self, item, position = (0,0)):
        
        """
        It takes in a matrix, an item, and a position, and updates the item in the matrix at the given
        position
        
        :param item: The item you want to update
        :param position: The position of the item you want to update
        """
        
        if len(position) != 2: print("ERROR: Position must have a list or a tuple with two variables!")
        else:
            x,y = position
                
            # For Human Understanding of columns and rows.
            x -= 1; y -= 1
                
            # It's read like this: matrix[x'th row][y'th item]
            self.matrix[x][y] = item
    
    def generate_general(self):
        
        """
        It takes the Coordinated_matrix and extracts the second element of each tuple, which is the
        actual data, and appends it to a new list
        """
        
        # Generate the general viewing matrix
        self.matrix = []
            
        for row in self.Coordinated_matrix:
            catched_data = []
                
            for item in row:
                catched_data.append(item[1])
            self.matrix.append(catched_data)
    
    def transpose(self):
        
        """
        It takes the matrix, creates a new matrix with the rows and columns swapped, and then iterates
        through the original matrix and sets the new matrix's values to the original matrix's values
        :return: A new matrix with the rows and columns swapped.
        """
        
        catched_matrix = Matrix(self.columns,self.rows,self.unity)
        catched_matrix.set_int(0) 
        
        row_index = 0
        
        for row in self.matrix:
            item_index = 0
            
            for item in row:
                
                # Swaps the rows with columns and vice versa.
                catched_matrix.matrix[item_index][row_index] = self.matrix[row_index][item_index]
                item_index += 1
            row_index += 1
            
        return catched_matrix
    
    def symmetric(self):
        
        """
        It checks if the matrix is a square matrix, if it is not, it prints an error message. If it is,
        it returns the symmetric matrix of the given matrix.
        :return: The sum of the matrix and its transpose.
        """
        
        if self.rows != self.columns: print("ERROR: Not a Square Matrix!")
        else:
            t_self = self.transpose()
            
            catched_matrix = self + t_self
            return catched_matrix
    
    def skew_symmetric(self):
        
        """
        It checks if the matrix is a square matrix, if it is not, it prints an error message. If it is,
        it returns the skew-symmetric matrix of the given matrix.
        :return: The difference between the matrix and its transpose.
        """
        
        if self.rows != self.columns: print("ERROR: Not a Square Matrix!")
        else:
            t_self = self.transpose()
            
            catched_matrix = self - t_self
            return catched_matrix
     