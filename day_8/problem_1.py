# Neat! now i know how to directly read a file without those pesky newlines
input = open("input.txt", 'r').read().splitlines()

# Matrix or as normal people call it: bidimensional array to store the tree grid
tree_matrix = []

# Convert the raw input into a bidimensional array of int
for line_index in range(0, len(input)):
    values = []
    for value_index in range(0, len(input[line_index])):
        values.append(int(input[line_index][value_index]))
    tree_matrix.insert(line_index, values)

# The edges are: (the height + the width )*2 - 4 (the angles)
height = len(tree_matrix)
width = len(tree_matrix[0])
edges = (height+width)*2-4

# This function takes in input:
# - The tree matrix
# - And the coordinates of the tree want to test


def is_viewable(matrix, x, y):
    viewable_from_top = True
    viewable_from_bottom = True
    viewable_from_left = True
    viewable_from_right = True
    # First we save the tree we want to check
    tree = int(matrix[y][x])
    # Then we split the arrays x and y in half
    # We basically want to test if the tree in x,y is bigger than ALL the trees in at least one of the 4 halves
    x_left = matrix[y][:x]
    x_right = matrix[y][x+1:]
    tmp_col = tuple(zip(*matrix))[x]
    y_down = tmp_col[y+1:]
    y_up = tmp_col[:y]
    # Then we do all the checks and IF the tree is viewable from at least one of the 4 halves return true
    if any(heights >= tree for heights in x_left):
        viewable_from_left = False
    if any(heights >= tree for heights in x_right):
        viewable_from_right = False
    if any(heights >= tree for heights in y_up):
        viewable_from_top = False
    if any(heights >= tree for heights in y_down):
        viewable_from_bottom = False
    viewable_from_one_side = viewable_from_left or viewable_from_right or viewable_from_bottom or viewable_from_top
    return viewable_from_one_side


# Find how many trees are viewable from at least one side of the inner matrix
viewable = 0
for y in range(1, len(tree_matrix)-1):
    for x in range(1, len(tree_matrix[y])-1):
        if is_viewable(tree_matrix, x, y):
            viewable = viewable+1

print(viewable+edges)
