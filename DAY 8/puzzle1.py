DEBUG = True

# open the file
with open("input.txt") as f:
    # read the file and initialize the matrix
    matrix = [list(map(int, line.strip())) for line in f]

    # initialize the count of visible trees
    count = 0

    # loop through the matrix and check if the tree is visible
    # (i.e. if the number is greater than the number in every
    # cell of the matrix to the right, left, up, and down of it)
    for i in range(1, len(matrix) - 1):
        for j in range(1, len(matrix[0]) - 1):
            if DEBUG:
                print(matrix[i][j], "i = ", i, "j = ", j)

            # get all the elements before
            # and after the element in the row
            row_before = matrix[i][:j]
            row_after = matrix[i][j + 1:len(matrix[0])]
            if DEBUG:
                print("row_before", row_before, "\nrow_after", row_after)

            # get all the elements before and after the
            # element in the column of the current element
            column_before = [row[j] for row in matrix[:i]]
            column_after = [row[j] for row in matrix[i + 1:len(matrix)]]
            if DEBUG:
                print("column_before", column_before, "\ncolumn_after", column_after, "\n")

            # check if the element is greater than all the elements in the row and column
            if matrix[i][j] > max(row_before) \
                    or matrix[i][j] > max(row_after) \
                    or matrix[i][j] > max(column_before) \
                    or matrix[i][j] > max(column_after):
                # if it is, increment the count
                count += 1
                if DEBUG:
                    print("FOUND VISIBLE TREE: ", matrix[i][j], "\n")

# add to the count the border elements
count += 2 * (len(matrix) + len(matrix[0]) - 2)

# print the answer
print(count)
