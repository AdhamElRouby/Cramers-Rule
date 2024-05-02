# importing Numpy package (used to calculate the determinant of the matrices)
import numpy as np # type: ignore

# creating the coefficient and constant terms matrix 
coeff_matrix = []
constants = []

# Ask the user to enter the size of the system
n = input("Enter the size of the system: ")
try:
    n = int(n)
    # take the user input of the system
    print("Enter the augmented matrix of the system:")
    for i in range(n):
        coeff_matrix.append([])
        line = input().split()
        # make sure the user entered the right number of variables
        if(len(line) != n + 1):
            print("Error: invalid number of inputs")
            exit()
        # fill the coeff_matrix and constans matrix
        for j in range(n):
            coeff_matrix[i].append(int(line[j]))
        constants.append(int(line[-1]))

    # calculate the determinant of the coefficient matrix
    matrix_det = np.linalg.det(coeff_matrix).round(2)

    # if the determinant is zero, stop the program
    if(matrix_det == 0):
        print("Error: the coefficient matrix is not invertible!")
        exit()

    # create a list of ans that will store the solutions of the sytems
    ans = []

    # apply cramer's rule
    for c in range(n):
        temp_matrix = np.copy(coeff_matrix) # create a copy of the coeff_matrix at each iteration
        for r in range(n):
            # temp_matrix is the coeff_matrix but change the cth column by the constant terms
            temp_matrix[r][c] = constants[r]
        # measure the determinant of temp_matrix
        new_det = np.linalg.det(temp_matrix).round(2)
        # add new_det/matrix_det to the array of answers
        ans.append(new_det/matrix_det)

    # print the answers
    print("Solutions:")
    for i in range(n):
        print("x" + str(i+1) + " =", ans[i])
except ValueError:
    print("This is not a valid integer")