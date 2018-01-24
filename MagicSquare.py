def MagicSquareGen(n):
    # Generate an empty 2D Matrix
    square = []
    for i in range (n):
        b = []
        for j in range (n):
            b.append(0)
        square.append(b)

    # set the last row of the middle column equal to one
    counter = 1
    ind1 = n-1
    ind2 = n//2
    square[ind1][ind2] = counter

    # run until the counter is equal to n squared
    while (counter < n**2):
        # increment the counter
        counter += 1
        # store indexes of moving right one and down one
        temp1 = ind1 + 1
        temp2 = ind2 + 1

        # check if outside the columns and the rows, move up one only if so
        if (temp1 > n-1 and temp2 > n-1):
            ind1 -= 1
            square[ind1][ind2] = counter

        # check if outside the columns not rows, move to beginning of rows
        elif (temp2 > n-1):
            ind2 = 0
            ind1 = temp1
            square[ind1][ind2] = counter

        # check if outside the rows not columns, move to beginning of columns
        elif (temp1 > n-1):
            ind1 = 0
            ind2 = temp2
            square[ind1][ind2] = counter

        # check if there is already a value there, move up one only if so
        elif (square[temp1][temp2] != 0):
            ind1 -= 1
            square[ind1][ind2] = counter

        # lastly if there are no issues just put the value there
        else:
            ind1 = temp1
            ind2 = temp2
            square[ind1][ind2] = counter

    return square

def main():
    size = int(input("Enter the size of the Matrix: "))
    while (size%2 == 0):
      size = int(input("Enter an odd number: "))

    magic_square = MagicSquareGen(size)
    print(magic_square)

main()
