DEBUG = True

# open the file
with open("input.txt") as f:
    # read the file and initialize the matrix
    matrix = [list(map(int, line.strip())) for line in f]

    # initialize the count of visible trees
    count = 0

    # initialize the array of the scores
    score = []

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

            # initialize the variables for the scores
            count_row_before = 0
            count_row_after = 0
            count_column_before = 0
            count_column_after = 0

            # reverse the row before and the column before
            # (because we want to check if the element is
            # greater than the elements to the left and up
            # and to do that we need to reverse the lists)
            row_before.reverse()
            column_before.reverse()

            # loop through the row before and count the
            # number of elements that are greater than the
            # current element (i.e. the number of visible trees)
            for k in range(len(row_before)):
                if row_before[k] < matrix[i][j]:
                    count_row_before += 1
                else:
                    count_row_before += 1
                    break

            # loop through the row after and count the
            # number of elements that are greater than the
            # current element (i.e. the number of visible trees)
            for k in range(len(row_after)):
                if row_after[k] < matrix[i][j]:
                    count_row_after += 1
                else:
                    count_row_after += 1
                    break

            # loop through the column before and count the
            # number of elements that are greater than the
            # current element (i.e. the number of visible trees)
            for k in range(len(column_before)):
                if column_before[k] < matrix[i][j]:
                    count_column_before += 1
                else:
                    count_column_before += 1
                    break

            # loop through the column after and count the
            # number of elements that are greater than the
            # current element (i.e. the number of visible trees)
            for k in range(len(column_after)):
                if column_after[k] < matrix[i][j]:
                    count_column_after += 1
                else:
                    count_column_after += 1
                    break

            if DEBUG:
                print("count_row_before", count_row_before, "\ncount_row_after", count_row_after,
                      "\ncount_column_before", count_column_before, "\ncount_column_after", count_column_after)
                print("moltiplication", count_row_before * count_row_after * count_column_before * count_column_after, "\n")

            # add the score (multiplication of the number of visible trees in every direction) to the array
            score.append(count_row_before * count_row_after * count_column_before * count_column_after)

# get the highest score
highest_score = max(score)

# print the answer
print(highest_score)
