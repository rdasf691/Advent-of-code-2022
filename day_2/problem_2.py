input=open('input.txt','r').readlines()

A=1 # Rock
B=2 # Paper
C=3 # Scissors

X=1 # Lose
Y=2 # Draw
Z=3 # Win

score=0

for line in input:
        # Case 1: IF it needs to be a draw
    if line[0] == 'A' and line[2] == 'Y': score=score+X+3
    elif line[0] == 'B' and line[2] == 'Y': score=score+Y+3
    elif line[0] == 'C' and line[2] == 'Y': score=score+Z+3
        # Case 2: IF it needs to be a victory
    elif line[0] == 'A' and line[2] == 'Z': score=score+Y+6
    elif line[0] == 'B' and line[2] == 'Z': score=score+Z+6
    elif line[0] == 'C' and line[2] == 'Z': score=score+X+6
        # Case 3: IF it needs to be a lost
    elif line[0] == 'A' and line[2] == 'X': score=score+Z+0
    elif line[0] == 'B' and line[2] == 'X': score=score+X+0
    elif line[0] == 'C' and line[2] == 'X': score=score+Y+0
 
print(score)
