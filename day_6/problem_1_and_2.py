input = open("input.txt",'r').read()

step=4 # The "chunk" size we want to read and check
# Just change this to solve the second part too

# NOTE: This better find the solution before approaching the end of the input because if not it'll crash for out of range
# Scroll ALL the characters in the input
for i in range(0, len(input)-1):
    buffer=[] # The chunk will be stored here
    # Store it..
    for character in range(i,step+i):
        buffer.append(input[character])
    # We check IF the buffer is unique by comparing lenght of it with the lenght of a unique set of it
    if(len(set(buffer)) == len(buffer)):
        print(i+step) # Print the index
        break
