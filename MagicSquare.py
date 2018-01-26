#  File: MagicSquare.py
#  Description: Create an accurate magic square of desired size
#  Student Name: Matthew Frangos
#  Student UT EID: msf955
#  Partner Name: Braeden Conrad
#  Partner UT EID: bsc875
#  Course Name: CS 303E
#  Unique Number: 51335
#  Date Created: 1/23/2018
#  Date Last Modified: 1/25/2018

def make_square(n):
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

def print_square(square):
	length=len(square)
	formatable=length-2
	print()
	print("Here is a", length, "x", length, "magic square:")
	print()
	for i in range (length):
		for j in range (length):
			print ('{:4}'.format(square[i][j]), end="")
		print()
	return

def check_square(square):
	# Check for sum of rows
	sum=0
	sum1=0
	for i in range (len(square)):
		sum+=square[0][i]
	for i in range (len(square)):
		for j in range (len(square)):
			sum1+=square[i][j]
		if(sum==sum1):
			sum1=0
			continue
		else:
			print("Not all rows are equal.")
	print()
	print("Sum of row = ", sum)
	# Check for sum of columns
	sum=0
	sum1=0
	for i in range (len(square)):
		sum+=square[i][0]
	for i in range (len(square)):
		for j in range (len(square)):
			sum1+=square[j][i]
		if(sum==sum1):
			sum1=0
		else:
			sum1=0
			print("Not all columns are equal.")
			break
	print("Sum of Column = ", sum)
	# Check for sum of left to right diagonal
	sum1=0
	for i in range (len(square)):
		sum1+=square[i][i]
	print("Sum of Diagonal (UL to LR) = ", sum1)
	# Check for sum of right to left diagonal
	sum1=0
	for k in range(len(square)):
		sum1+=square[k][(len(square)-1-k)]
	print("Sum of Diagonal (UR to LL) = ", sum1)
	return

def main():
    size = int(input("Enter the size of the desired magic square: "))
    while (size%2 == 0):
      size = int(input("Enter an odd number: "))
    magic_square = make_square(size)
    print_square(magic_square)
    check_square(magic_square)

main()
