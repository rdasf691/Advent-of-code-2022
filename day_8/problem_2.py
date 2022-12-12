# Same boilerblate code from the last problem
# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
input = open("input.txt", 'r').read().splitlines()

tree_matrix = []

for line_index in range(0, len(input)):
    values = []
    for value_index in range(0, len(input[line_index])):
        values.append(int(input[line_index][value_index]))
    tree_matrix.insert(line_index, values)

# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
# End of the boilerplate 


# This function takes in input:
# - The tree matrix
# - And the coordinates of the tree want to find the scenic score
def find_score(matrix, x, y):
    # Boilerplate again
    # ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
    tree=int(matrix[y][x])
    x_left=matrix[y][:x]
    x_right=matrix[y][x+1:]
    tmp_col=tuple(zip(*matrix))[x]
    y_down = tmp_col[y+1:]
    y_up=tmp_col[:y]
    # ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
    # End of the boilerplate

    # We need to reverse these two because we're watching from the inside to the outside now
    x_left.reverse()
    tmp=[]
    for value in y_up:
        tmp.insert(0,value)
    y_up=tmp

    top=0
    bottom=0
    left=0
    right=0
    score=0
    # This is the main difference:
    # We scroll each of the 4 halves and keep track until we find a bigger tree
    for trees in x_left:
        if trees >= tree:
            left=left+1
            break
        else: left=left+1
    for trees in x_right:
        if trees >= tree:
            right=right+1
            break
        else: right=right+1
    for trees in y_up:
        if trees >= tree:
            top=top+1
            break
        else: top=top+1
    for trees in y_down:
        if trees >= tree:
            bottom=bottom+1
            break
        else: bottom=bottom+1
    score=top*bottom*left*right
    return score

# Find the scenic score of each tree in the inner matrix
scores = []
for y in range(1, len(tree_matrix)-1):
    for x in range(1, len(tree_matrix[y])-1):
        scores.append(find_score(tree_matrix, x, y))
scores.sort(reverse=True)

print(scores[0])
